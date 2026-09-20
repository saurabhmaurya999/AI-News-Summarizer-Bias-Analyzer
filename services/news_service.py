import requests

from config import NEWS_API_KEY, NEWS_API_URL, MAX_ARTICLES


def search_news(query):
    if not NEWS_API_KEY:
        raise RuntimeError(
            "NEWS_API_KEY is missing. Add it to your .env file."
        )

    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": MAX_ARTICLES,
    }

    response = requests.get(
        NEWS_API_URL,
        params=params,
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    if data.get("status") != "ok":
        raise RuntimeError(
            data.get("message", "NewsAPI request failed.")
        )

    articles = []

    for article in data.get("articles", []):

        articles.append({
            "title": article.get("title") or "Untitled",

            "description": (
                article.get("description") or ""
            ),

            "url": article.get("url"),

            "source": (
                (article.get("source") or {}).get("name")
                or "Unknown"
            ),

            "published_at": (
                article.get("publishedAt") or ""
            ),

            "image": article.get("urlToImage"),
        })

    return articles