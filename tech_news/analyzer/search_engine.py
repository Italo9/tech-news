from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    caracter_min = title.lower()
    result_database = search_news({"title": {"$regex": caracter_min}})
    result_lista = list()
    for new in result_database:
        result_lista.append((new["title"], new["url"]))
    return result_lista


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
