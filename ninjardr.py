from sitescraper import SiteScraper

if __name__ == "__main__":
    destructoid = SiteScraper(
        "Destructoid",
        "https://www.destructoid.com",
        "h2",
        "sparticle_title",
        ["a", "text"],
        ["a"]
        )
    
    #print(destructoid.get_article_list())
    print(destructoid.print_articles())