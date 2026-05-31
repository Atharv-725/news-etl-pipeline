import pandas as pd

POSITIVE_WORDS = ["good", "great", "best", "win", "up", "high",
                  "growth", "success", "positive", "rise", "gain", "top"]
NEGATIVE_WORDS = ["bad", "worst", "crash", "down", "low", "loss",
                  "fail", "negative", "drop", "kill", "dead", "crisis"]

def analyze_sentiment(text):
    if not text:
        return "neutral"
    text = text.lower()
    pos = sum(1 for w in POSITIVE_WORDS if w in text)
    neg = sum(1 for w in NEGATIVE_WORDS if w in text)
    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    else:
        return "neutral"

def transform_articles(articles):
    if not articles:
        return pd.DataFrame()

    df = pd.DataFrame(articles)

    # Keep only needed columns
    df = df[["title", "description", "source", "url", "publishedAt"]].copy()

    # Extract source name
    df["source"] = df["source"].apply(
        lambda x: x.get("name", "Unknown") if isinstance(x, dict) else str(x)
    )

    # Rename columns
    df.rename(columns={"publishedAt": "published_at"}, inplace=True)

    # Clean nulls
    df["title"]       = df["title"].fillna("No Title")
    df["description"] = df["description"].fillna("No Description")

    # Add sentiment
    df["sentiment"] = df["title"].apply(analyze_sentiment)

    # Remove duplicates
    df.drop_duplicates(subset=["title"], inplace=True)

    print(f"✅ Transformed {len(df)} articles")
    print(f"   Positive: {len(df[df['sentiment']=='positive'])}")
    print(f"   Negative: {len(df[df['sentiment']=='negative'])}")
    print(f"   Neutral:  {len(df[df['sentiment']=='neutral'])}")

    return df