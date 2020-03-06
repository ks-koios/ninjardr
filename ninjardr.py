import json

from sitescraper import SiteScraper

def scraper_factory(site_list_file):
    with open(site_list_file) as f:
        site_list = f.read()

    sites = json.loads(site_list)

    scrapers = []
    for _, site in sites.items():
        scrapers.append(SiteScraper(
            site["name"],
            site["url"],
            site["articles_tag"],
            site["articles_class"],
            site["child_tags"],
            site["link_tags"]
        ))

    return scrapers

if __name__ == "__main__":
    scrapers = scraper_factory("site-list.json")
      
    for scraper in scrapers:
        print(scraper.print_articles())