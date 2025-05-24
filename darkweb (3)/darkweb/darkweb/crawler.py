from bs4 import BeautifulSoup
from utils import get_tor_session

def crawl_site(url):
    session = get_tor_session()
    response = session.get(url, timeout=40)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return text 