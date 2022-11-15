import time

import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code == 200:
            return response.text
        return None
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_novidades(html_content):
    lista_url = list()
    lista_url = Selector(html_content).css(
        ".cs-overlay-link::attr(href)").getall()
    return lista_url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
