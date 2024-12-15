# Link Checker

A Python script to analyze GitHub repositories. Extracts stars, forks, descriptions, and languages. Validates README.md links and logs broken links for review.

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
