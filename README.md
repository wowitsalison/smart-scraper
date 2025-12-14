# Smart Scraper
Helpers for web scraping functions I find myself reusing regularly.

## How to use
1. **Navigate to project directory** `cd /projects/smart-scraper`
2. **Run command** `pip install -e .`
3. **Import to any project** `from smart-scraper.py import SmartScraper`
4. **Initialize a scraper** `scraper = SmartScraper(url)`

## Functions
### `fetch_content(self)`
Fetches the html from the given url


### `extract links(self, contains=None, starts_with=None, ends_with=None)`
Extracts all links from the url with the option to filter

**Filter by:**
- `contains`
- `starts_with`
- `ends_with`

`fetch_content` is called within `extract_links`, so there's no need to call both.
