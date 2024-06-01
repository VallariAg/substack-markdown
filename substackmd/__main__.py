from sys import argv
from substackmd import convert, scrape


if __name__ == "__main__":
    url = argv[1]
    html = scrape.scraped_html(url)
    convert.process_substack_html(html)
