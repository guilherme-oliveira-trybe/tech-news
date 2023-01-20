from tech_news.database import search_news
from tech_news.analyzer.search_engine import resumed_news
from collections import Counter


# Requisito 10
def top_5_news():
    news_found = search_news(
        {"$query": {}, "$orderby": {"comments_count": -1, "title": 1}}
    )
    filtered_news = news_found[:5]
    return resumed_news(filtered_news)


# Requisito 11
def top_5_categories():
    news_found = search_news({"$query": {}, "$orderby": {"category": 1}})
    count_category = Counter([news["category"] for news in news_found])
    return sorted(count_category, key=count_category.get, reverse=True)[:5]
