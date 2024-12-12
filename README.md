# search all url
This tool allows you to extract URLs from websites using two different sources: the [Wayback Machine](https://web.archive.org/) and the [GAU](https://github.com/lc/gau) tool. The tool can help you gather all available URLs for a given website, and you can choose to store them in one combined file or separate files based on the website.
## Features

- Extract URLs from the [Wayback Machine](https://web.archive.org/).
- Extract URLs from the GAU tool.
- Filter out URLs with unwanted file extensions.
- Save extracted URLs in either a combined file or separate files for each website.
- Simple command-line interface.
  ## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- The [GAU tool](https://github.com/lc/gau) (for extracting URLs from `gau`).
- `requests` Python package (for sending HTTP requests).
- `subprocess` library (included with Python).

You can install the necessary Python package by running:

```bash
pip install requests
```
## Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/wayback-url-extractor.git](https://github.com/mohammaddalieft/sAllUrl.git
cd sAllUrl
```

## Usage
### 1. Extract URLs from Websites

The tool allows you to extract URLs from one or more websites by providing a list of websites as input. You can specify whether you want all URLs to be saved in one combined file or in separate files for each website.
#### Running the script
You can run the script with the following command:
```bash
python seachallurl.py <option>

```
`<option>` can be either `y` or `n`:

- `y`: Save URLs in separate files for each website.
- `n`: Save all URLs in a single file called `combined_urls.txt`.
#### For example:
```bash
python seachallurl.py y  # Save in separate files for each website
python seachallurl.py n  # Save in a single combined file

```
#### Input Format
The script expects a list of websites provided via standard input. You can provide the list either manually or by using a text file. Here’s an example:
```bash
echo -e "example.com1\example.com2" | python seachallurl.py y

```
Alternatively, you can store the websites in a file and use the following:
```bash
cat websites.txt | python seachallurl.py n

```
### 2. How It Works

- The tool first queries the [Wayback Machine API](https://web.archive.org/) to retrieve the URLs for each website.
- It also uses the GAU tool to extract URLs from various HTTP requests made to the website.
- It filters out URLs with unwanted extensions (e.g., `.json`, `.jpg`, `.exe`, etc.) based on a predefined list.
- The URLs are then saved in the specified output file format.

### 3. Sample Output

- If you choose `y`, the URLs will be saved in a file named after the website (e.g., `voorivex.academy_urls.txt`).
- If you choose `n`, all URLs from all websites will be saved in a single file: `combined_urls.txt`.
