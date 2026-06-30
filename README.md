# 🏨 HotelInsight AI

**Author:** Shetketu Mitra

HotelInsight AI is a **Multi-Agent Hotel Review Intelligence Platform** that transforms thousands of hotel reviews into actionable business insights using Natural Language Processing (NLP), Sentiment Analysis, Data Analytics, and Google's Gemini AI.

The application automatically analyzes hotel review datasets, discovers customer sentiments, identifies strengths and weaknesses, generates executive summaries, recommends business improvements, and produces downloadable PDF reports.

---

# 🚀 Features

- 📂 Upload hotel review CSV datasets
- 📊 Automatic dataset profiling
- 😊 Sentiment Analysis
- 📈 Hotel Health Score
- 🏆 Hotel Strength Identification
- ⚠️ Improvement Area Detection
- 🧠 AI Theme Discovery
- 🔍 AI Root Cause Analysis
- 📊 AI Benchmark Analysis
- 👥 AI Guest Persona Generation
- 📈 AI Trend Analysis
- 📝 Executive Summary Generation
- 💼 AI Consultant Recommendations
- ☁️ Word Cloud Visualization
- 📄 PDF Report Generation
- 🤖 Multi-Agent AI Pipeline

---

# 🧠 Multi-Agent Architecture

HotelInsight AI is built using multiple specialized AI agents.

| Agent | Responsibility |
|--------|----------------|
| DatasetProfilerAgent | Profiles uploaded dataset |
| SchemaAgent | Detects review and score columns |
| SentimentAgent | Performs sentiment analysis |
| ThemeAgent | Detects complaint themes |
| PositiveThemeAgent | Detects positive themes |
| AspectSentimentAgent | Calculates aspect-level sentiment |
| HealthScoreAgent | Computes Hotel Health Score |
| InsightsAgent | Identifies strengths and improvement areas |
| GeminiThemeAgent | AI Theme Discovery |
| GeminiRootCauseAgent | AI Root Cause Analysis |
| GeminiBenchmarkAgent | AI Benchmark Analysis |
| GeminiGuestPersonaAgent | AI Guest Persona Generation |
| GeminiTrendAgent | AI Trend Analysis |
| GeminiSummaryAgent | Executive Summary Generation |
| GeminiConsultantAgent | AI Consultant Recommendations |
| WordCloudAgent | Generates review word cloud |
| PDFReportAgent | Generates downloadable PDF report |

---

# 📸 Application Screenshots

## Dashboard

![Dashboard](images/dashboard.png)

---

## Theme Analysis

![Theme Analysis](images/themes.png)

---

## Strengths, Benchmark & Root Cause Analysis

![Strength Analysis](images/strengths.png)

---

## AI Guest Personas

![Guest Personas](images/guest_personas.png)

---

## AI Trend Analysis & Executive Summary

![Trend Analysis](images/trends.png)

---

## AI Consultant Recommendations

![Recommendations](images/recommendations.png)

---

## Multi-Agent Execution Pipeline

![Pipeline](images/pipeline.png)

---

# 📄 Generated Business Insights

The platform automatically generates:

- Executive Summary
- Hotel Health Score
- Strength Analysis
- Improvement Areas
- Complaint Themes
- Positive Themes
- AI Theme Discovery
- AI Root Cause Analysis
- AI Benchmark Report
- Priority Issues
- Guest Personas
- Trend Analysis
- Consultant Recommendations
- Word Cloud
- Downloadable PDF Report

---

# 🛠️ Technology Stack

## Programming

- Python 3.12

## Frontend

- Streamlit

## Data Processing

- Pandas

## Visualization

- Plotly
- WordCloud

## Natural Language Processing

- TextBlob

## AI

- Google Gemini API

## Reporting

- ReportLab

---

# 📂 Project Structure

```
HotelInsightAI/
│
├── agents/
│   ├── aspect_sentiment_agent.py
│   ├── consultant_agent.py
│   ├── dataset_agent.py
│   ├── dataset_profiler_agent.py
│   ├── gemini_benchmark_agent.py
│   ├── gemini_competitor_agent.py
│   ├── gemini_consultant_agent.py
│   ├── gemini_guest_persona_agent.py
│   ├── gemini_root_cause_agent.py
│   ├── gemini_summary_agent.py
│   ├── gemini_theme_agent.py
│   ├── gemini_trend_agent.py
│   ├── health_score_agent.py
│   ├── insights_agent.py
│   ├── pdf_report_agent.py
│   ├── positive_theme_agent.py
│   ├── recommendation_agent.py
│   ├── review_agent.py
│   ├── root_cause_agent.py
│   ├── schema_agent.py
│   ├── sentiment_agent.py
│   ├── summary_agent.py
│   ├── theme_agent.py
│   └── wordcloud_agent.py
│
├── data/
├── reports/
├── images/
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/shetketumitra/HotelInsightAI.git
```

Go into the project directory.

```bash
cd HotelInsightAI
```

Create a virtual environment (recommended).

```bash
conda create -n hotelinsight python=3.12
conda activate hotelinsight
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root.

```text
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application.

```bash
streamlit run app.py
```

---

# 📊 Dataset

The application accepts hotel review datasets containing:

- Hotel Reviews
- Ratings / Scores
- Positive Reviews
- Negative Reviews

The application automatically detects the appropriate review and score columns.

---

# 📈 Sample Outputs

The platform produces:

- Sentiment Distribution
- Hotel Health Score
- Complaint Analysis
- Theme Discovery
- Business Benchmarking
- Root Cause Analysis
- Guest Personas
- Executive Summary
- Consultant Recommendations
- Downloadable PDF Report

---

# 🎯 Future Improvements

- Real-time review monitoring
- Competitor benchmarking dashboard
- Hotel comparison mode
- Interactive chatbot
- Predictive sentiment forecasting
- Vector database integration
- RAG-powered hotel intelligence
- Multi-language review analysis
- Cloud deployment
- REST API integration

---

# 👨‍💻 Author

**Shetketu Mitra**

Data Analyst | AI Enthusiast | Hospitality Professional

GitHub:
https://github.com/shetketumitra

---

# ⭐ If you found this project interesting, please consider giving it a Star.
