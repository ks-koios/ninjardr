import json
import sys
import os


from sitescraper import SiteScraper

def create_scrapers(site_list_file):
    with open(site_list_file) as f:
        site_list = f.read()

    sites = json.loads(site_list)

    scrapers = []
    for _, site in sites.items():
        scrapers.append(SiteScraper(
            site["name"],
            site["url"],
            site["articles_tags"],
            site["articles_class"],
            site["child_tags"],
            site["link_tags"],
            site["url_pre"],
            site["article_tag"],
            site["article_hasID"],
            site["article_class"],
        ))

    return scrapers         
    

if __name__ == "__main__":
    hr = "------------------------------"
    scrapers = create_scrapers("site-list.json")

    while True:
        _ = os.system('cls')
        print(f"\nWelcome to ninja reader!\n{hr}")
        print(f"\nSite List:\n{hr}")
        for i, scraper in enumerate(scrapers, 1):
            print(f"{i}) {scraper.site_name}")

        print(hr)
        choice = input("Select a site (q to quit): ")

        if choice.isdigit() is True:
            choice = int(choice) - 1
            while True:
                _ = os.system('cls')
                print(f"\n{scrapers[choice].site_name}")
                print(hr)
                print(scrapers[choice].print_articles())
                print(hr)
            
                article_choice = input("Select an article (q to quit, b to go back): ")

                if article_choice.isdigit() is True:
                    article_choice = int(article_choice) - 1
                    _ = os.system('cls')
                    scrapers[choice].print_article(article_choice)
                elif article_choice.lower() == 'b':
                    break
                elif article_choice.lower() == 'q':
                    _ = os.system('cls')
                    sys.exit(0)
          
        elif choice.lower() == 'q':
            _ = os.system('cls')
            break