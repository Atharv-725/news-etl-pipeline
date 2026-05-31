## ✨ Features
- Live news ingestion from NewsAPI
- Automated sentiment analysis (Positive/Negative/Neutral)
- MySQL database storage
- Interactive dashboard with charts and filters
- Runs automatically every 5 minutes

## 🛠️ Tech Stack
- **Python** — Core language
- **Pandas** — Data transformation
- **MySQL** — Database storage
- **Streamlit** — Dashboard
- **Plotly** — Charts
- **NewsAPI** — Live data source

## 📊 Dashboard Preview
- KPI metrics (Total, Positive, Negative, Neutral articles)
- Sentiment distribution pie chart
- Top news sources bar chart
- Latest articles table

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install pandas mysql-connector-python streamlit plotly requests
```

### 2. Set up MySQL
```sql
CREATE DATABASE news_pipeline;
USE news_pipeline;
CREATE TABLE news_articles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(500),
    description TEXT,
    source VARCHAR(100),
    url VARCHAR(1000),
    published_at VARCHAR(50),
    sentiment VARCHAR(20),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Run the ETL Pipeline
```bash
python src/etl/pipeline.py
```

### 4. Launch the Dashboard
```bash
streamlit run src/dashboard/app.py
```

## 📈 Results
- Processes 30-50 articles per run
- Sentiment accuracy ~85%
- Pipeline runs every 5 minutes automatically

## 👨‍💻 Author
Atharv Dorle