import requests
from bs4 import BeautifulSoup

class GithubRepoScraper:
    """
    Github Repo Scraper class for scraping github repos from the given URL
    """

    def __init__(self):
        self.base_url = "https://github.com/luckysher"
        self.save_file_path = "repo.json"

    def scrape_repos(self):
        pass