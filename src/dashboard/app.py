import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

DB_CONFIG = {
    "host": "mysql",
    "user": "root",
    "password": "root",
    "database": "news_pipeline"
}

def get_data():
    conn = mysql.connector.connect(**DB_CONFIG)
    df = pd.read_sql("SELECT * FROM news_articles ORDER BY processed_at DESC", conn)
    conn.close()
    return df

# ── Page Config ──────────────────────────────────────
st.set_page_config(page_title="News ETL Dashboard", layout="wide")
st.title("📰 Real-Time News ETL Pipeline Dashboard")
st.markdown("Live news data processed by our ETL pipeline")

# ── Load Data ────────────────────────────────────────
df = get_data()

# ── KPI Metrics ──────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Articles",  len(df))
col2.metric("Positive News",   len(df[df["sentiment"] == "positive"]))
col3.metric("Negative News",   len(df[df["sentiment"] == "negative"]))
col4.metric("Neutral News",    len(df[df["sentiment"] == "neutral"]))

st.divider()

# ── Charts ───────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("😊 Sentiment Distribution")
    sentiment_counts = df["sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["sentiment", "count"]
    fig = px.pie(sentiment_counts, values="count", names="sentiment",
                 color_discrete_map={"positive": "green",
                                     "negative": "red",
                                     "neutral": "gray"})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📡 Top News Sources")
    source_counts = df["source"].value_counts().head(10).reset_index()
    source_counts.columns = ["source", "count"]
    fig2 = px.bar(source_counts, x="count", y="source", orientation="h")
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ── Latest Articles Table ────────────────────────────
st.subheader("📋 Latest Articles")
st.dataframe(df[["title", "source", "sentiment", "published_at"]].head(20),
             use_container_width=True)