# NewsLens – AI News Summarizer & Bias Analyzer

NewsLens is an AI-powered web application that collects news articles based on a user's search topic, summarizes the articles, and analyzes their language for potential bias.

The application provides a simple web interface where users can enter a news topic and get processed news results.

---

## Features

- Search news articles using a topic or keyword
- Fetch recent news using NewsAPI
- Extract article content
- Generate AI-based summaries
- Analyze articles for potential linguistic bias
- Display news source and publication information
- Simple and responsive web interface
- Flask-based backend
- HTML, CSS and JavaScript frontend

---

## How It Works

The application follows this workflow:

User enters a topic
        ↓
NewsAPI searches for related articles
        ↓
Article content is extracted
        ↓
AI generates a summary
        ↓
Bias detection is performed
        ↓
Results are displayed on the website

---

## Example Input

Users only need to enter a topic or keyword.

Examples:

- Artificial Intelligence
- AI regulation in India
- Climate change
- India economy
- Space technology
- Electric vehicles

You do not need to paste a complete news article.

---

## Project Structure

```text
news-bias-analyzer/
│
├── data/
│   └── cache.json
│
├── services/
│   ├── __init__.py
│   ├── article_service.py
│   ├── bias_detector.py
│   ├── embeddings.py
│   ├── news_service.py
│   └── summarizer.py
│
├── static/
│   ├── scripts/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── .env
├── .gitignore
├── app.py
├── config.py
├── README.md
└── requirements.txt"# AI-News-Summarizer-Bias-Analyzer" 
