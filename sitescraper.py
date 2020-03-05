import requests
import urllib.request
from bs4 import BeautifulSoup


class SiteScraper:
    """Base scraper class

    Class Variables:
    site_name           -- Website title
    url                 -- url address for the site
    article_tag         -- parent tag type that all articles are under (div, etc.)
    article_class_id    -- class or id of tag
    child_tags          -- list of child tags and attributes from parent class to get to an article title

    """

    def __init__(self, site_name, url, article_tag, article_class, child_tags):
        self.site_name = site_name
        self.url = url
        self.article_tag = article_tag
        self.article_class = article_class
        self.child_tags = child_tags

    def get_site_html(self):
        #response = requests.get(self.url)
        with open("destruct.txt") as f: 
            return BeautifulSoup(f, "html.parser")

    def get_article_list(self):
        return self.get_site_html().findAll(self.article_tag, self.article_class)

    def print_article_list(self):
        for i, article in enumerate(self.get_article_list()):
            for tag in self.child_tags:
                article = getattr(article, tag)
            print(f"{i}) {article}")
        
