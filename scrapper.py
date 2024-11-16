import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class Scraper:
    def __init__(self, site, keyword=""):
        self.site = site
        self.keyword = keyword

    def scrape(self):
        try:
            # Attempt to open the URL and read HTML content
            print("Attempting to open the site...\n")
            r = urllib.request.urlopen(self.site)
            html = r.read()
            print("Successfully fetched the HTML content.\n")

            # Parse HTML with BeautifulSoup
            sp = BeautifulSoup(html, "html.parser")
            print("Parsing the HTML content...\n")

            # Track if any URLs are found
            urls_found = False

            # Loop through all anchor tags
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url is None:
                    continue

                # Apply keyword filtering if specified
                if self.keyword and self.keyword not in url:
                    continue

                # Convert relative URLs to absolute URLs
                full_url = urljoin(self.site, url)
                print("Found URL:", full_url)
                urls_found = True

            # Check if no URLs were found
            if not urls_found:
                print("No URLs matching the criteria were found.")

        except Exception as e:
            print(f"An error occurred: {e}")


# Prompt user for site URL and optional keyword
news = input("Enter site URL: ").strip()
keyword = input("Enter keyword to filter URLs (leave blank to get all URLs): ").strip()

if news.startswith("http"):
    Scraper(news, keyword).scrape()
else:
    print("Please enter a valid URL starting with http or https.")
