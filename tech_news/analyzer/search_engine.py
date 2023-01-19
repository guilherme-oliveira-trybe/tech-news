from tech_news.database import search_news
from datetime import datetime


def resumed_news(news_found):
    resumed_news_info = []
    for news in news_found:
        resumed_news_info.append((news["title"], news["url"]))
    return resumed_news_info


# https://pt.stackoverflow.com/questions/377579/valida%C3%A7%C3%A3o-de-data-testes-com-python
def validy_date(date):
    try:
        is_validy_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        return is_validy_date
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 6
def search_by_title(title):
    news_found = search_news({"title": {"$regex": title, "$options": "i"}})
    # resumed_news_info = [(news["title"], news["url"]) for news in news_found]
    return resumed_news(news_found)


# Requisito 7
def search_by_date(date):
    new_date = validy_date(date)
    news_found = search_news({"timestamp": new_date})
    return resumed_news(news_found)


# Requisito 8
def search_by_tag(tag):
    news_found = search_news(
        {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
    )
    return resumed_news(news_found)


# Requisito 9
def search_by_category(category):
    news_found = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return resumed_news(news_found)
