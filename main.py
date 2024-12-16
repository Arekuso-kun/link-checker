import os
import re
import sys
from datetime import datetime

import requests
from colorama import Fore, init

init()  # initialize colorama


def get_html(url):
    try:
        response = requests.get(url, timeout=10)
        return response.text
    except requests.RequestException as e:
        print(f"{Fore.RED}Error fetching URL {url}:{Fore.RESET} {e}")
    return ""


def get_readme_link(repo_url):
    repo_page_url = f"https://github.com/{repo_url}"

    html_data = get_html(repo_page_url)

    readme_regex = r"<a .*?href=\"(/[^/]+/[^/]+/blob/[^/]+/README\.md)\">"
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
        return False, None


def extract_links_from_readme(repo_url, username):
    readme_url = get_readme_link(repo_url)

    if not readme_url:
        print(f"{Fore.RED}README.md not found{Fore.RESET}")
        return

    print(
        f"{Fore.YELLOW}README.md URL:{Fore.RESET} {Fore.CYAN}{readme_url}{Fore.RESET}"
    )

    readme_content = get_html(readme_url)

    link_regex = r"https?://[^\s<>`\"()\[\]]+"
    links = re.findall(link_regex, readme_content)

    bad_links = []

    if links:
        print(f"{Fore.YELLOW}Links in README.md:{Fore.RESET} {len(links)}")
        for link in links:
            print(f"{Fore.CYAN}{link}{Fore.RESET}")

            is_valid, status = check_link_status(link)
            if is_valid:
                print(f"{Fore.GREEN}✓ Link is valid!{Fore.RESET}")
            else:
                if status is None:
                    print(f"{Fore.RED}✗ Link may be broken or unreachable.{Fore.RESET}")
                else:
                    print(
                        f"{Fore.RED}✗ Link may be broken or unreachable. Status Code: {status}{Fore.RESET}"
                    )

                bad_links.append((link, status))
    else:
        print(f"{Fore.RED}No links found in README.md{Fore.RESET}")

    if bad_links:

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        log_filename = f"{log_dir}/{username}.log"

        with open(log_filename, "a") as log_file:
            log_file.write(
                f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            log_file.write(f"Repository: {repo_url}\n")
            for link, status in bad_links:
                log_file.write(f"Bad Link: {link} - Status: {status}\n")
            log_file.write("\n")

        print(f"Bad links logged to {Fore.YELLOW}{log_filename}{Fore.RESET}")

    print()


def extract_repo_details(repo_url):
    repo_page_url = f"https://github.com/{repo_url}"
    html_data = get_html(repo_page_url)

    # extract stars
    stars_regex = r"<span .*?id=\"repo-stars-counter-star\" .*?title=\"([0-9,]+)\".*?>.*?</span>"
    stars_match = re.search(stars_regex, html_data)
    stars = stars_match.group(1).replace(",", "") if stars_match else "?"

    # extract forks
    forks_regex = r"<span .*?id=\"repo-network-counter\" .*?title=\"([0-9,]+)\".*?>.*?</span>"
    forks_match = re.search(forks_regex, html_data)
    forks = forks_match.group(1).replace(",", "") if forks_match else "?"

    # extract description
    description_regex = r"<p .*?class=\"f4 my-3\".*?>(.*?)</p>"
    description_match = re.search(description_regex, html_data, re.DOTALL)
    about = (
        description_match.group(1).strip()
        if description_match
        else "No description provided."
    )

    # extract languages
    languages_regex = r"<span .*?aria-label=\"([^\"]+ [0-9\.]+)\".*?>.*?</span>"
    languages_match = re.findall(languages_regex, html_data)
    languages = (
        ", ".join([f"{lang}%" for lang in languages_match])
        if languages_match
        else "No languages detected."
    )

    print(f"{Fore.YELLOW}Stars:{Fore.RESET} {stars}")
    print(f"{Fore.YELLOW}Forks:{Fore.RESET} {forks}")
    print(f"{Fore.YELLOW}About:{Fore.RESET} {about}")
    print(f"{Fore.YELLOW}Languages:{Fore.RESET} {languages}")


def main():
    args = sys.argv[1:]  # command-line arguments, excluding the script name

    if args:
        username = args[0]
    else:
        username = input("Enter GitHub username: ").strip()

    url = f"https://github.com/{username}?tab=repositories"

    html_data = get_html(url)

    repo_regex = (
        r"<a .*?href=\"/([^/]+/[^\"]+)\" .*?itemprop=\"name codeRepository\".*?>"
    )
    matches = re.findall(repo_regex, html_data)

    if not matches:
        print(f'{Fore.RED}No repositories found for user "{username}"{Fore.RESET}')
        return
    
    print(f'{Fore.MAGENTA}Total repositories found:{Fore.RESET} {len(matches)}')

    for match in matches:
        repo_name = match.split("/")[-1]
        repo_url = f"{match}"
        print(f"{Fore.YELLOW}Repo Name:{Fore.RESET} {repo_name}")
        print(
            f"{Fore.YELLOW}Repo URL:{Fore.RESET} {Fore.CYAN}https://github.com/{repo_url}{Fore.RESET}"
        )

        extract_repo_details(repo_url)
        extract_links_from_readme(repo_url, username)


if __name__ == "__main__":
    main()
