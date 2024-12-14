import re

import requests
from colorama import Fore, init

init()  # colorama initialize


def get_html(url):
    response = requests.get(url)
    return response.text


def get_readme_link(repo_url):
    repo_page_url = f"https://github.com/{repo_url}"

    html_data = get_html(repo_page_url)

    readme_regex = r"<a.*href=\"(/[^/]+/[^/]+/blob/[^/]+/README\.md)\">"
    match = re.search(readme_regex, html_data)

    if match:
        raw_path = match.group(1).replace("/blob/", "/")
        readme_url = f"https://raw.githubusercontent.com{raw_path}"
        return readme_url
    return None


def check_link_status(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.RequestException as e:
        return False, str(e)


def extract_links_from_readme(repo_url):
    readme_url = get_readme_link(repo_url)

    if not readme_url:
        print(f"{Fore.RED}README.md not found for repository {repo_url}{Fore.RESET}")
        return

    print(f"{Fore.GREEN}Fetching README from: {readme_url}{Fore.RESET}")

    readme_content = get_html(readme_url)

    link_regex = r"https?://[^\s<>\`()\[\]]+"
    links = re.findall(link_regex, readme_content)

    if links:
        print(f"{Fore.YELLOW}Links found in README.md:{Fore.RESET}")
        for link in links:
            print(f"{Fore.CYAN}{link}{Fore.RESET}")

            is_valid, status = check_link_status(link)
            if is_valid:
                print(f"{Fore.GREEN}✔️ Link is valid!{Fore.RESET}")
            else:
                print(
                    f"{Fore.RED}❌ Link is broken or unreachable. Status Code: {status}{Fore.RESET}"
                )
    else:
        print(f"{Fore.RED}No links found in README.md.{Fore.RESET}")


username = input("Enter GitHub username: ")

url = f"https://github.com/{username}?tab=repositories"

html_data = get_html(url)

repo_regex = r'<a href="/([^/]+/[^"]+)" itemprop="name codeRepository" >'
matches = re.findall(repo_regex, html_data)

for match in matches:
    repo_name = match.split("/")[-1]
    repo_url = f"{match}"
    print(
        f"{Fore.MAGENTA}Repo Name: {repo_name}; Repo URL: https://github.com/{repo_url}{Fore.RESET}"
    )

    extract_links_from_readme(repo_url)
