import requests

NEWS_API_KEY = "ff0ddc5c977c4447b5fda54a07f3775a"

def fetch_news(topic="technology", page_size=50):
    url = (
        "https://newsapi.org/v2/top-headlines"
        f"?language=en&pageSize={page_size}&apiKey={NEWS_API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok":
        print(f"❌ API Error: {data.get('message')}")
        return []

    articles = data.get("articles", [])
    print(f"✅ Fetched {len(articles)} articles from NewsAPI")
    return articles