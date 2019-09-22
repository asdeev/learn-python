import bs4
import requests


def get_amazon_price(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#mediaNoAccordian> div.a-row > div.a-column')
    return elems[0].text.strip()


price = get_amazon_price('http://price.com')
print(price)


# from something import something_else -> learn about why this is
