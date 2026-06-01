import os
import mysql.connector

DB_CONFIG = {
    "host":     os.environ.get("DB_HOST", "127.0.0.1"),
    "user":     "root",
    "password": "root",
    "database": "news_pipeline"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def load_to_mysql(df):
    if df.empty:
        print("   No data to load.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    inserted = 0
    skipped = 0

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO news_articles (title, description, source, url, published_at, sentiment)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (row["title"], row["description"], row["source"],
                  row["url"], row["published_at"], row["sentiment"]))
            inserted += 1
        except mysql.connector.errors.IntegrityError:
            skipped += 1

    conn.commit()
    cursor.close()
    conn.close()

    print(f"✅ Loaded {inserted} articles into MySQL")
    print(f"   Skipped {skipped} duplicates")