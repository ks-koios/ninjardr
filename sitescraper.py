import requests
import urllib.request
import pickle
import os

from datetime import datetime
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

    def __init__(self,
                site_name,
                url,
                articles_tags,
                articles_class,
                child_tags,
                link_tags,
                url_pre,
                article_tag,
                article_hasID,
                article_class):
        self.site_name = site_name
        self.url = url
        self.articles_tags = articles_tags
        self.articles_class = articles_class
        self.child_tags = child_tags
        self.link_tags = link_tags
        self.url_pre = url_pre
        self.article_tag = article_tag
        self.article_hasID = article_hasID
        self.article_class = article_class

    def get_site_html(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.text, "html.parser")

    def write_to_cache(self, site, article_list, date):
        with open(f"cache/{site}_{date}", "wb+") as f:
            pickle.dump(article_list, f)

    def is_site_cached(self, site, date):
        if os.path.exists(f"cache/{site}_{date}"):
            return True
        else:
            return False

    def get_cache(self, site, date):
        with open(f"cache/{site}_{date}", "rb") as f:
            articles = pickle.load(f)

        return articles

    def get_articles(self):
        date = datetime.today().strftime("%Y-%m-%d")
        if self.is_site_cached(self.site_name, date):
                articles = self.get_cache(self.site_name, date)
        else:
            articles = []
            for art_tag in self.articles_tags:
                article_html_list = self.get_site_html(self.url).findAll(art_tag, self.articles_class)
                for article in article_html_list:
                    for tag in self.link_tags:
                        link = getattr(article, tag)

                    link = link["href"]

                    for tag in self.child_tags:
                        article = getattr(article, tag)

                    articles.append((article, link))
            self.write_to_cache(self.site_name, articles, date)
        return articles
        
    def print_articles(self):
        for i, article in enumerate(self.get_articles(), 1):
            print(f"{i}) {article[0]}")

    def get_article(self, choice):
        articles = self.get_articles()
        article_name = articles[choice][0]
        article_url = self.url_pre + articles[choice][1]
        if self.article_hasID == True:
            article_html = self.get_site_html(article_url).find(self.article_tag, id=self.article_class)
        else:
            article_html = self.get_site_html(article_url).find(self.article_tag, self.article_class)
        paragraphs = article_html.findAll("p")

        return (article_name, article_url, paragraphs)
    
    def print_article(self, choice):
        article_name, article_url, paragraphs = self.get_article(choice)
        print(f"=== {article_name} ==\n\n")
        for p in paragraphs:
            print(f"{p.text}")
        print("\n")
        print(f"From: {article_url}")
        

        
        
