import time
from extract import fetch_news
from transform import transform_articles
from load import load_to_mysql

def run_pipeline():
    print("=" * 50)
    print("🚀 ETL Pipeline Started!")
    print("=" * 50)

    print("\n📰 EXTRACT — Fetching news...")
    articles = fetch_news()

    print("\n⚙️  TRANSFORM — Cleaning & analyzing...")
    df = transform_articles(articles)

    print("\n💾 LOAD — Saving to MySQL...")
    load_to_mysql(df)

    print("\n✅ Pipeline run complete!")

if __name__ == "__main__":
    run_pipeline()