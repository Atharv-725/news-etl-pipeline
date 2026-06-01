# 📰 Real-Time News ETL Pipeline

![GitHub Actions](https://github.com/Atharv-725/news-etl-pipeline/actions/workflows/etl.yml/badge.svg)

A production-grade ETL pipeline that fetches live news, performs sentiment analysis, stores data in MySQL, and visualizes it on a Streamlit dashboard — fully containerized with Docker and automated with GitHub Actions.

## 🏗️ Architecture


## ⚙️ Tech Stack
- **Python** — ETL logic
- **MySQL** — Data storage
- **Streamlit + Plotly** — Dashboard
- **Docker + docker-compose** — Containerization
- **GitHub Actions** — Automated hourly pipeline

## 🚀 Quick Start

### Option 1 — Run with Docker (Recommended)
```bash
git clone https://github.com/Atharv-725/news-etl-pipeline.git
cd news-etl-pipeline
docker-compose up --build
```
Open http://localhost:8501

### Option 2 — Run Locally
```bash
pip install -r requirements.txt
cd src/etl
python pipeline.py
streamlit run src/dashboard/app.py
```

## 📊 Results
- Fetches 30 articles per run
- Sentiment analysis (Positive / Negative / Neutral)
- Auto-refreshing dashboard
- Pipeline runs every hour via GitHub Actions

## 🤖 CI/CD
GitHub Actions workflow runs the ETL pipeline every hour automatically.

## 👨‍💻 Author
**Atharv Dorle**