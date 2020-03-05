from sitescraper import SiteScraper

if __name__ == "__main__":
    destructoid = SiteScraper(
        "Destructoid",
        "https://www.destructoid.com",
        "h2",
        "sparticle_title",
        ["a", "text"]
        )
    print(destructoid.print_article_list())