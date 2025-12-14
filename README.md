# Smart Scraper
Helpers for web scraping functions I find myself reusing regularly.

## How to use
1. **Navigate to project directory** `cd /projects/smart-scraper`
2. **Run command** `pip install -e .`
3. **Import to any project** `from scraper.py import SmartScraper`
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

## Example
```python
from scraper.py import SmartScraper

capablanca_url = "https://www.chessgames.com/perl/ezsearch.pl?search=capablanca"
carlsen_url = "https://www.chessgames.com/perl/ezsearch.pl?search=carlsen"
scraper = SmartScraper(capablanca_url)

capablanca_games = scraper.extract_links(starts_with="www.chessgames.com/perl/chessgame?gid=")

print("Take a look at Capablanca's first 25 games:")
for game in capablanca_games:
  print(game)

scraper.url = carlsen_url
carlsen_games = scraper.extract_links(starts_with="www.chessgames.com/perl/chessgame?gid=")

print("Take a look at Carlsen's first 25 games:")
for game in carlsen_games:
  print(game)
```
