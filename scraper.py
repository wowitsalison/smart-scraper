from bs4 import BeautifulSoup
import requests

class SmartScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
        }

    def fetch_content(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Error fetching url content: {e}")
            self.soup = None

    def extract_links(self, contains=None, starts_with=None, ends_with=None):
        self.fetch_content()
        
        if not self.soup:
            return []
        
        all_links = self.soup.find_all("a")
        filtered_links = []

        for link in all_links:
            href = link.get('href')

            if not href:
                continue
            if contains and contains in href:
                filtered_links.append(href)
            elif starts_with and href.startswith(starts_with):
                filtered_links.append(href)
            elif ends_with and href.endswith(ends_with):
                filtered_links.append(href)
            elif not contains and not starts_with and not ends_with:
                filtered_links.append(href)

        return filtered_links