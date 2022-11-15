from tech_news.database import search_news
import datetime


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
    try:
        data = datetime.date.fromisoformat(date)
        modela_data_em_formato_valido = data.strftime("%d/%m/%Y")
        result_database = search_news(
            {"timestamp": {"$regex": modela_data_em_formato_valido}}
        )
        result_lista = list()
        for new in result_database:
            result_lista.append((new["title"], new["url"]))
        return result_lista
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    caracter_min = tag.lower()
    result_database_busca_tag = search_news(
        {"tags": {"$elemMatch": {"$regex": caracter_min, "$options": "i"}}}
    )
    result_lista = list()
    for new in result_database_busca_tag:
        result_lista.append((new["title"], new["url"]))
    return result_lista


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
