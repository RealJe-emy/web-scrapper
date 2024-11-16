Web Scraper

A simple Python web scraper that retrieves URLs from a given website and optionally filters them based on a specified keyword. The scraper uses BeautifulSoup to parse HTML content and urllib to handle URL requests.
Features

    Scrape Links: Fetches all anchor (<a>) tags from a webpage and prints each URL.
    Keyword Filtering: Optionally filters URLs containing a specified keyword.
    Relative URL Handling: Converts relative URLs to absolute URLs for easy navigation.
    Error Handling: Catches and reports errors if the URL is invalid or the page cannot be accessed.

Requirements

    Python 3.x
    BeautifulSoup: Install via pip install beautifulsoup4

Usage
1. Clone the Repository

git clone <repository-url>
cd web-scraper

2. Install Dependencies

Make sure BeautifulSoup is installed:

pip install beautifulsoup4

3. Run the Scraper

Run the script with:

python scraper.py

4. Provide Input

When prompted:

    Enter the full URL of the website you want to scrape. For example: https://example.com
    Optionally, enter a keyword to filter URLs. Only URLs containing this keyword will be printed. Leave blank to fetch all URLs.

Example

Enter site URL: https://example.com
Enter keyword to filter URLs (leave blank to get all URLs): articles

This will print only URLs containing the word "articles" on https://example.com.
Code Overview

The scraper.py script is structured as follows:

    Scraper Class: Handles all scraping operations, including opening the URL, parsing HTML, filtering URLs by keyword, and converting relative URLs to absolute URLs.
    scrape Method: Contains the core logic, including error handling and the URL filtering mechanism.

Main Components

    __init__: Initializes the scraper with a site URL and optional keyword.
    scrape: Opens the URL, fetches HTML, parses for <a> tags, and filters based on the keyword.

Example Output

After providing the URL and keyword, you’ll see output similar to:

Attempting to open the site...

Successfully fetched the HTML content.

Parsing the HTML content...

Found URL: https://example.com/articles/1
Found URL: https://example.com/articles/2

No URLs matching the criteria were found.

Troubleshooting

    No URLs Displayed: Ensure the website URL is correct and accessible.
    Connection Error: Some sites may block automated scraping. Try another site or add a delay between requests.
    Invalid URL Error: Verify the URL starts with http or https.

License

This project is licensed under the MIT License.
