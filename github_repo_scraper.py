import requests
from bs4 import BeautifulSoup
import json
import time

class GithubRepoScraper:
    """
    Github Repo Scraper class for scraping github repos from the given URL
    """

    def __init__(self):
        self.base_url = "https://github.com/luckysher"
        self.save_file_path = "repo.json"

    def scrape_repos(self):
        url = f"{self.base_url}?tab=repositories"
        print(f"[GithubRepoScraper] Scraping repos from url: {url}")
        res = requests.get(url=url)
        bs = BeautifulSoup(res.content, features="html.parser")

        # all repos
        div = bs.find("div", id="user-repositories-list")
        repos_infos = div.find_all('li')
        repos = []
        for repo in repos_infos:
            try:
                # Extract repo name
                repo_name = repo.find("h3").find("a").text

                # repo access type
                repo_access_type = repo.find("h3").find_all("span")[1].text

                # Extract programing language
                lang_tag = repo.find("span", itemprop="programmingLanguage")
                programming_lang = lang_tag.text if lang_tag else ""

                # description
                desc_tag = repo.find("p", itemprop="description")
                description = desc_tag.text if desc_tag else ""
                repo_data = {'repo_name': repo_name, 'programing_language': programming_lang, 'repo_type': repo_access_type, 'description': description}

                print(repo_data)
                repos.append(repo_data)
                print("-----------")
            except Exception as e:
                print("[Exception] Got Exception while extracting repo name ")
                print(e)

        with open(self.save_file_path, 'w') as w:
            json.dump(repos, w)
            print(f"[GithubRepoScraper]: saved scraped data at: {self.save_file_path}")
            w.close()



