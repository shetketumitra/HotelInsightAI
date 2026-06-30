# 🏨 HotelInsight AI

**HotelInsight AI** is a Multi-Agent AI-powered Hotel Review Intelligence Platform that analyzes hotel guest reviews to generate actionable business insights for hospitality managers.

Developed by **Shetketu Mitra**

---

# Project Overview

HotelInsight AI processes thousands of hotel reviews and automatically discovers:

- Guest sentiment
- Complaint themes
- Positive themes
- Hotel strengths
- Improvement areas
- Guest personas
- Root cause analysis
- Trend analysis
- Executive summaries
- Management recommendations

The platform combines traditional NLP techniques with Generative AI (Google Gemini) to produce consultant-level hospitality reports.

---

# Key Features

### Dataset Profiling
- Automatic dataset detection
- Review column detection
- Rating column detection

### Sentiment Analysis
- Positive
- Neutral
- Negative review classification

### Theme Discovery
Automatically identifies major guest discussion topics.

### Hotel Health Score
Calculates an overall hotel performance score.

### Strength Analysis
Highlights the hotel's strongest operational areas.

### Improvement Analysis
Identifies key guest pain points.

### AI Root Cause Analysis
Uses Gemini AI to identify possible operational causes behind guest complaints.

### AI Benchmark Analysis
Benchmarks hotel performance against industry standards.

### AI Guest Persona Discovery
Identifies the major guest segments visiting the hotel.

### AI Trend Analysis
Analyzes operational performance and business trends.

### Executive Summary
Generates management-ready summaries.

### AI Consultant Recommendations
Produces practical recommendations for hotel managers.

### PDF Report Generation
Exports the analysis as a professional PDF report.

---

# Multi-Agent Architecture

The system consists of multiple specialized AI agents:

- DatasetProfilerAgent
- SchemaAgent
- SentimentAgent
- ThemeAgent
- AspectSentimentAgent
- InsightsAgent
- HealthScoreAgent
- GeminiThemeAgent
- GeminiRootCauseAgent
- GeminiBenchmarkAgent
- GeminiGuestPersonaAgent
- GeminiTrendAgent
- GeminiSummaryAgent
- GeminiConsultantAgent
- PDFReportAgent

Each agent performs one specific responsibility, making the architecture modular and scalable.

---

# Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- WordCloud
- TextBlob
- Google Gemini API
- ReportLab

---

# Installation

Clone the repository

```bash
git clone <repository_url>
```

Navigate into the project

```bash
cd HotelInsightAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# Project Structure

```
HotelInsightAI/

agents/
data/
reports/

app.py
requirements.txt
README.md
.env
```

---

# Sample Output

The application generates:

- Hotel Health Score
- Sentiment Dashboard
- Theme Analysis
- AI Theme Discovery
- AI Root Cause Analysis
- AI Benchmark Report
- Guest Persona Analysis
- Trend Analysis
- Executive Summary
- AI Consultant Recommendations
- Downloadable PDF Report

---

# Future Enhancements

- Competitor benchmarking
- Multi-hotel comparison
- Interactive dashboards
- RAG-based hotel knowledge base
- Multi-language review analysis
- Predictive guest satisfaction
- Real-time review monitoring
- Cloud deployment
- Advanced LLM orchestration

---

# Author

**Shetketu Mitra**

Data Analytics Capstone Project

HotelInsight AI v1.0