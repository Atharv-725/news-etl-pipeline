import time
from extract import fetch_news
from transform import transform_articles
from load import load_to_mysql

def run_pipeline():
    print("=" * 50)
    print("🚀 ETL Pipeline Started!")
    print("=" * 50)

    while True:
        print("\n📰 EXTRACT — Fetching news...")
        articles = fetch_news()

        print("\n⚙️  TRANSFORM — Cleaning & analyzing...")
        df = transform_articles(articles)

        print("\n💾 LOAD — Saving to MySQL...")
        load_to_mysql(df)

        print("\n✅ Pipeline run complete!")
        print("⏳ Waiting 5 minutes before next run...\n")
        time.sleep(300)

if __name__ == "__main__":
    run_pipeline()