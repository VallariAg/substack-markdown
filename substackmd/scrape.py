from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def scraped_html(url):
    # url = 'https://vallariagrawal.substack.com/p/curious-minds-1-why-do-pricing-usually'

    req = Request(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    html = urlopen(req).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup
