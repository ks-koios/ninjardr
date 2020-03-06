import requests
import urllib.request
from bs4 import BeautifulSoup


class SiteScraper:
    """
    Class Variables:
    site_name           -- Website title
    url                 -- url address for the site
    article_tag         -- parent tag type that all articles are under (div, etc.)
    article_class_id    -- class or id of tag
    child_tags          -- list of child tags and attributes from parent class to get to article title
    link_tags           -- list of child tags and attributes from parent class to get to article <a> tag
    """

    def __init__(self, site_name, url, articles_tag, articles_class, child_tags, link_tags):
        self.site_name = site_name
        self.url = url
        self.articles_tag = articles_tag
        self.articles_class = articles_class
        self.child_tags = child_tags
        self.link_tags = link_tags

    def get_site_html(self):
        #response = requests.get(self.url)
        with open("destruct.txt") as f: 
            return BeautifulSoup(f, "html.parser")

    def get_articles(self):
        articles = []
        article_html_list = self.get_site_html().findAll(self.articles_tag, self.articles_class)
        for article in article_html_list:
            for tag in self.link_tags:
                link = getattr(article, tag)

            link = link["href"]

            for tag in self.child_tags:
                article = getattr(article, tag)

            articles.append((article, link))

        return articles
        
    def print_articles(self):
        for i, article in enumerate(self.get_articles(), 1):
            print(f"{i}) {article[0]}")

    def print_article(self, choice):
        articles = self.get_articles()
        print(articles[choice])