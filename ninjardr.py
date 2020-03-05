import requests
import urllib.request
from bs4 import BeautifulSoup


class SiteScraper:
    def __init__(self, site_name, url, article_tag, article_class):
        self.site_name = site_name
        self.url = url
        self.article_tag = article_tag
        self.article_class = article_class

    def get_site_html(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")

    def get_article_list(self):
        self.articles = self.get_site_html().findAll(self.article_tag, self.article_class)

    @abstractmethod
    def print_article_list(self):
        pass