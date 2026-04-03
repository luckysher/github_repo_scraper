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
        """
        Method for scraping repos
        :return:
        """
        url = f"{self.base_url}?tab=repositories"
        print(f"[GithubRepoScraper] Scraping repos from url: {url}")
        res = requests.get(url=url)
        bs = BeautifulSoup(res.content, features="html.parser")

        # all repos
        div = bs.find("div", id="user-repositories-list")
        repos_infos = div.find_all('li')
        repos = []