import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=headers, timeout=4)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    urls = selector.css("a.cs-overlay-link::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".nav-links a.next::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css(
        "link[href^='https://blog.betrybe.com']::attr(href)"
    ).get()

    title = selector.css("h1.entry-title::text").get()

    timestamp = selector.css(".meta-date::text").get()

    writer = selector.css(".author a::text").get()

    comments_count = selector.css(".title-block::text").re_first(r"\d")
    if comments_count is None:
        comments_count = 0

    unedited_summary = selector.css(
        ".entry-content > p:nth-child(1) *::text"
    ).getall()

    summary = "".join(unedited_summary)

    tags = selector.css(".post-tags a::text").getall()

    category = selector.css(".category-style .label::text").get()

    notice_data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": int(comments_count),
        "summary": summary,
        "tags": tags,
        "category": str(category),
    }

    return notice_data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
