# Link Checker

A Python script to analyze GitHub repositories. Extracts stars, forks, descriptions, and languages. Checks README.md links and logs broken links for review.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Arekuso-kun/link-checker.git
   cd link-checker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line:

```bash
python main.py <github-username>
```

For example:

```bash
python main.py Arekuso-kun
```

Alternatively, you can run the script without any arguments, and it will prompt you to enter a GitHub username interactively.

### Input

- **GitHub Username**: Specify the GitHub username whose repositories you want to analyze.

### Output

- **Repository Details**: Stars, forks, description, and languages.
- **Links in README**: Checks all links in the repository's `README.md` for all repositories of that user.
- **Log File**: Saves broken links in the `logs` directory.

## Requirements

- Python
- Modules: `requests`, `colorama`

Install dependencies using:

```bash
pip install -r requirements.txt
```
