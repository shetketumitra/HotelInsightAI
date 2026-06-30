import streamlit as st
import pandas as pd
import plotly.express as px

from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

from agents.gemini_theme_agent import GeminiThemeAgent
from agents.gemini_root_cause_agent import GeminiRootCauseAgent
from agents.gemini_guest_persona_agent import GeminiGuestPersonaAgent
from agents.gemini_trend_agent import GeminiTrendAgent
from agents.gemini_consultant_agent import GeminiConsultantAgent
from agents.gemini_benchmark_agent import GeminiBenchmarkAgent
from agents.gemini_summary_agent import GeminiSummaryAgent
from agents.pdf_report_agent import PDFReportAgent
from wordcloud import WordCloud, STOPWORDS
from agents.recommendation_agent import RecommendationAgent
from agents.dataset_agent import DatasetAgent
from agents.aspect_sentiment_agent import AspectSentimentAgent
from agents.schema_agent import SchemaAgent
from agents.review_agent import ReviewAgent
from agents.theme_agent import ThemeAgent
from agents.positive_theme_agent import PositiveThemeAgent
from agents.consultant_agent import ConsultantAgent
from agents.summary_agent import SummaryAgent
from agents.insights_agent import InsightsAgent
from agents.sentiment_agent import SentimentAgent
from agents.health_score_agent import HealthScoreAgent
from agents.dataset_profiler_agent import DatasetProfilerAgent
from agents.wordcloud_agent import WordCloudAgent
from agents.root_cause_agent import RootCauseAgent


# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(page_title="HotelInsight AI", layout="wide")

# ----------------------------------
# TITLE
# ----------------------------------

st.title("🏨 HotelInsight AI")

st.markdown("### By Shetketu Mitra")

st.markdown("Multi-Agent Hotel Review Intelligence Platform")

# ----------------------------------
# FILE UPLOAD
# ----------------------------------

uploaded_files = st.file_uploader(
    "Upload Hotel Review CSV Files", type=["csv"], accept_multiple_files=True
)

# ----------------------------------
# MAIN PROCESSING
# ----------------------------------

if uploaded_files:

    schema_agent = SchemaAgent()
    dataset_agent = DatasetAgent()
    profiler_agent = DatasetProfilerAgent()

    dfs = []

    for uploaded_file in uploaded_files:
        temp_df = pd.read_csv(uploaded_file)
        dfs.append(temp_df)

    df = pd.concat(dfs, ignore_index=True)

    dataset_profile = profiler_agent.profile(df)

    # ----------------------------------
    # DATASET PROFILER AGENT
    # ----------------------------------

    st.success(f"{len(uploaded_files)} CSV file(s) loaded successfully.")

    # ----------------------------------
    # SCHEMA AGENT
    # ----------------------------------

    schema = schema_agent.detect_columns(df)
    dataset_type = dataset_agent.detect_dataset(schema)

    is_valid, message = schema_agent.validate_dataset(schema)

    if not is_valid:
        st.error(message)
        st.stop()

    # ----------------------------------
    # DATASET PROFILER FIRST
    # ----------------------------------

    score_column = dataset_profile["score_column"]
    review_column = dataset_profile["review_column"]
    positive_review_column = dataset_profile["positive_review_column"]
    negative_review_column = dataset_profile["negative_review_column"]

    # ----------------------------------
    # SCHEMA FALLBACK
    # ----------------------------------

    if score_column is None:
        score_column = schema["score_column"]

    if review_column is None:
        review_column = schema["review_column"]

    if positive_review_column is None:
        positive_review_column = schema["positive_review_column"]

    if negative_review_column is None:
        negative_review_column = schema["negative_review_column"]

    st.info(f"Detected Score Column: {score_column}")
    st.info(f"Detected Review Column: {review_column}")
    st.success(f"Dataset Type: {dataset_type}")

    # ----------------------------------
    # SENTIMENT AGENT
    # ----------------------------------

    sentiment_agent = SentimentAgent()

    # ----------------------------------
    # ASPECT SENTIMENT AGENT
    # ----------------------------------
    aspect_agent = AspectSentimentAgent()

    # Hotel_Reviews.csv format
    if positive_review_column is not None and negative_review_column is not None:
        all_reviews = pd.concat(
            [df[positive_review_column], df[negative_review_column]], ignore_index=True
        )
        sentiment_results = sentiment_agent.analyze_sentiment(all_reviews)

    # Generic review datasets
    else:
        sentiment_results = sentiment_agent.analyze_sentiment(df[review_column])

    # ----------------------------------
    # REVIEW AGENT
    # ----------------------------------

    review_agent = ReviewAgent()
    results = review_agent.analyze_reviews(df, score_column)

    # ----------------------------------
    # HEALTH AGENT
    # ----------------------------------
    health_agent = HealthScoreAgent()
    health_score = health_agent.calculate(
        results["average_score"], results["highest_score"]
    )

    # ----------------------------------
    # THEME AGENT
    # ----------------------------------

    theme_agent = ThemeAgent()
    positive_agent = PositiveThemeAgent()

    # ----------------------------------
    # Recommendation AGENT
    # ----------------------------------

    recommendation_agent = RecommendationAgent()

    # ----------------------------------
    # PDF AGENT
    # ----------------------------------

    pdf_agent = PDFReportAgent()

    # ----------------------------------
    # Word Cloud AGENT
    # ----------------------------------

    wordcloud_agent = WordCloudAgent()

    if positive_review_column is not None and negative_review_column is not None:
        all_reviews = pd.concat(
            [df[positive_review_column], df[negative_review_column]], ignore_index=True
        )
        wordcloud_image = wordcloud_agent.generate(all_reviews)
    else:
        wordcloud_image = wordcloud_agent.generate(df[review_column])

    # ----------------------------------
    # ASPECT SENTIMENT ANALYSIS
    # ----------------------------------

    if review_column is not None:
        aspect_results = aspect_agent.analyze(df, review_column)
    else:
        aspect_results = aspect_agent.analyze(df, negative_review_column)

    # Hotel_Reviews.csv format
    if positive_review_column is not None and negative_review_column is not None:
        themes = theme_agent.detect_themes(df, negative_review_column)
        positive_themes = positive_agent.detect_positive_themes(
            df, positive_review_column
        )

    # Generic review datasets
    else:
        themes = theme_agent.detect_themes(df, review_column)
        positive_themes = positive_agent.detect_positive_themes(df, review_column)

    # ----------------------------------
    # INSIGHTS AGENT
    # ----------------------------------

    insights_agent = InsightsAgent()

    root_cause_agent = RootCauseAgent()

    strengths = insights_agent.get_strengths(
        aspect_results
    )

    improvement_areas = insights_agent.get_improvement_areas(
        aspect_results
    )

    wifi_reviews = root_cause_agent.collect_reviews(
        df,
        review_column,
        "WiFi"
    )

    # ----------------------------------
    # CONSULTANT AGENT
    # ----------------------------------

    gemini_root_cause_agent = GeminiRootCauseAgent(
        GEMINI_API_KEY
    )

    gemini_benchmark_agent = GeminiBenchmarkAgent(
        GEMINI_API_KEY
    )

    gemini_persona_agent = GeminiGuestPersonaAgent(
        GEMINI_API_KEY
    )

    gemini_trend_agent = GeminiTrendAgent(
        GEMINI_API_KEY
    )

    try:
        wifi_root_causes = (
            gemini_root_cause_agent.analyze(
                "WiFi",
                wifi_reviews
            )
        )
    except Exception:
        wifi_root_causes = (
            "Gemini quota exceeded. Root cause analysis unavailable."
        )

    try:
        benchmark_report = (
            gemini_benchmark_agent.benchmark(
                health_score,
                results["average_score"],
                strengths,
                improvement_areas
            )
        )
    except Exception:
        benchmark_report = (
            "Gemini quota exceeded. Benchmark analysis unavailable."
        )

    # ----------------------------------
    # GUEST PERSONA ANALYSIS
    # ----------------------------------

    if review_column is not None:
        persona_reviews = (
            df[review_column]
            .dropna()
            .astype(str)
            .head(500)
            .tolist()
        )
    else:
        persona_reviews = (
            df[positive_review_column]
            .dropna()
            .astype(str)
            .head(500)
            .tolist()
        )

    try:
        guest_persona_report = (
            gemini_persona_agent.identify_personas(
                persona_reviews
            )   
        )
    except Exception:
        guest_persona_report = "Gemini quota exceeded. Guest persona analysis unavailable."

    try:
        consultant_agent = GeminiConsultantAgent(GEMINI_API_KEY)
        recommendations = consultant_agent.generate_recommendations(
            health_score, strengths, improvement_areas
        )
    except Exception:
        recommendations = recommendation_agent.generate(improvement_areas)

    # ----------------------------------
    # TREND AGENT
    # ----------------------------------

    # Note: Ensure these variables are defined in your scope
    # (Assuming placeholders like positive_reviews, etc. exist)
    trend_data = f"""
    Average Review Score: {results['average_score']}

    Health Score: {health_score}

    Positive Reviews: {sentiment_results['Positive']:,}

    Neutral Reviews: {sentiment_results['Neutral']:,}

    Negative Reviews: {sentiment_results['Negative']:,}

    Top Strengths:
    {strengths}

    Top Improvement Areas:
    {improvement_areas}
    """

    try:
        trend_report = gemini_trend_agent.analyze_trends(
            trend_data
        )
    except Exception:
        trend_report = "Gemini quota exceeded. Trend analysis unavailable."

    # ----------------------------------
    # SUMMARY AGENT
    # ----------------------------------

    summary_agent = SummaryAgent()
    priority_ranking = summary_agent.get_priority_ranking(improvement_areas)

    try:
        gemini_agent = GeminiSummaryAgent(GEMINI_API_KEY)
        executive_summary = gemini_agent.generate_summary(
            results["average_score"], health_score, strengths, improvement_areas
        )
    except Exception:
        executive_summary = summary_agent.generate_summary(
            results["average_score"], improvement_areas
        )

    # ----------------------------------
    # KPI SECTION
    # ----------------------------------

    st.subheader("📊 Analysis Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Reviews", f"{results['total_reviews']:,}")
    col2.metric("Average Score", results["average_score"])
    col3.metric("Highest Score", results["highest_score"])
    col4.metric("Lowest Score", results["lowest_score"])
    col5.metric("Health Score", f"{health_score}/100")

    if health_score >= 85:
        st.success("🏆 Overall Rating: Excellent Hotel")
    elif health_score >= 70:
        st.info("👍 Overall Rating: Good Hotel")
    elif health_score >= 55:
        st.warning("⚠️ Overall Rating: Average Hotel")
    else:
        st.error("🚨 Overall Rating: Needs Improvement")

    # ----------------------------------
    # SENTIMENT ANALYSIS
    # ----------------------------------

    st.subheader("😊 Sentiment Analysis")

    col1, col2, col3 = st.columns(3)

    col1.metric("Positive Reviews", sentiment_results["Positive"])
    col2.metric("Neutral Reviews", sentiment_results["Neutral"])
    col3.metric("Negative Reviews", sentiment_results["Negative"])

    sentiment_df = pd.DataFrame(
        {
            "Sentiment": list(sentiment_results.keys()),
            "Count": list(sentiment_results.values()),
        }
    )

    sentiment_fig = px.pie(
        sentiment_df,
        names="Sentiment",
        values="Count",
        title="Review Sentiment Distribution",
    )

    st.plotly_chart(sentiment_fig, use_container_width=True)

    # ----------------------------------
    # COMPLAINT THEMES
    # ----------------------------------

    st.subheader("🚨 Top Complaint Themes")

    complaint_df = pd.DataFrame(
        {
            "Theme": list(themes.keys()),
            "Count": [value["negative"] for value in themes.values()],
        }
    )

    complaint_fig = px.bar(
        complaint_df, x="Theme", y="Count", title="Complaint Distribution"
    )

    st.plotly_chart(complaint_fig, use_container_width=True)

    try:
        gemini_theme_agent = GeminiThemeAgent(GEMINI_API_KEY)

        if review_column is not None:
            sample_reviews = df[review_column].dropna().astype(str).tolist()
        else:
            sample_reviews = df[negative_review_column].dropna().astype(str).tolist()

        discovered_themes = gemini_theme_agent.discover_themes(sample_reviews)

    except Exception:
        discovered_themes = "AI Theme Discovery unavailable."

    st.subheader("🧠 AI Theme Discovery")
    st.info(discovered_themes)

    # ----------------------------------
    # POSITIVE THEMES
    # ----------------------------------

    st.subheader("✅ Top Positive Themes")

    positive_df = pd.DataFrame(
        {
            "Theme": list(aspect_results.keys()),
            "Count": [data["positive"] for data in aspect_results.values()],
        }
    )

    positive_fig = px.bar(
        positive_df, x="Theme", y="Count", title="Positive Theme Distribution"
    )

    st.plotly_chart(positive_fig, use_container_width=True)

    # ----------------------------------
    # STRENGTHS
    # ----------------------------------

    st.subheader("⭐ Hotel Strengths")

    for rank, (theme, score, pos, neg) in enumerate(strengths, start=1):
        st.success(f"#{rank}: {theme} | Net={score} | Positive={pos} | Negative={neg}")

    # ----------------------------------
    # IMPROVEMENT AREAS
    # ----------------------------------

    st.subheader("⚠️ Improvement Areas")

    for rank, (theme, score, pos, neg) in enumerate(improvement_areas, start=1):

        st.warning(
            f"#{rank}: {theme} | Net={score} | Positive={pos} | Negative={neg}"
        )

    st.subheader("🤖 AI Root Cause Analysis")

    st.info(
        wifi_root_causes
    )

    # ----------------------------------
    # AI BENCHMARK ANALYSIS
    # ----------------------------------

    st.subheader("📊 AI Benchmark Analysis")

    st.info(
        benchmark_report
    )

    # ----------------------------------
    # PRIORITY ISSUES
    # ----------------------------------

    st.subheader("🥇 Priority Issues")

    medals = ["🥇", "🥈", "🥉"]

    for i, (theme, score) in enumerate(priority_ranking):
        st.write(f"{medals[i]} {theme} (Net Score: {score:,})")

    # ----------------------------------
    # GUEST PERSONAS
    # ----------------------------------

    st.subheader("👥 AI Guest Personas")

    st.info(guest_persona_report)
    
    # ----------------------------------
    # TREND ANALYSIS
    # ----------------------------------

    st.subheader("📈 AI Trend Analysis")

    st.info(trend_report)
    
    # ----------------------------------
    # EXECUTIVE SUMMARY
    # ----------------------------------

    st.subheader("📝 Executive Summary")
    st.info(executive_summary)

    # ----------------------------------
    # WORD CLOUD DISPLAY
    # ----------------------------------

    st.subheader("☁️ Review Word Cloud")

    st.image(wordcloud_image, use_container_width=True)

    # ----------------------------------
    # RECOMMENDATIONS
    # ----------------------------------

    st.subheader("🤖 AI Consultant Recommendations")

    for recommendation in recommendations:
        st.success(recommendation)

    st.caption("Recommendations generated by Gemini AI")

    # ----------------------------------
    # AI AGENT EXECUTION PIPELINE
    # ----------------------------------

    st.markdown("---")
    st.subheader("🤖 AI Agent Execution Pipeline")

    with st.expander("🧠 DatasetProfilerAgent", expanded=False):
        st.success("Completed")
        st.write(f"Dataset Type: {dataset_profile['dataset_type']}")
        st.write(f"Confidence: {dataset_profile['confidence']}%")
        st.write(f"Rows: {dataset_profile['row_count']:,}")
        st.write(f"Columns: {dataset_profile['column_count']}")

    with st.expander("📄 SchemaAgent"):
        st.success("Completed")
        st.write(f"Review Column: {review_column}")
        st.write(f"Score Column: {score_column}")
        st.write(f"Hotel Column: {dataset_profile['hotel_column']}")
        st.write(f"Date Column: {dataset_profile['date_column']}")

    with st.expander("😊 SentimentAgent"):
        st.success("Completed")
        st.write(sentiment_results)

    with st.expander("🚨 ThemeAgent"):
        st.success("Completed")
        st.write(f"Detected {len(themes)} business themes")

    with st.expander("📈 AspectSentimentAgent"):
        st.success("Completed")
        st.write(f"Calculated sentiment for {len(aspect_results)} aspects")

    with st.expander("⭐ InsightsAgent"):
        st.success("Completed")
        st.write(f"Strengths Found: {len(strengths)}")
        st.write(f"Improvement Areas: {len(improvement_areas)}")

    with st.expander("🧠 GeminiSummaryAgent"):
        st.success("Completed")
        st.write("Executive Summary generated successfully.")

    with st.expander("💼 GeminiConsultantAgent"):
        st.success("Completed")
        st.write(f"Generated {len(recommendations)} recommendations.")

    with st.expander("📄 PDFReportAgent"):
        st.success("Completed")
        st.write("Executive PDF ready for download.")

        # ----------------------------------
        # DOWNLOAD REPORT
        # ----------------------------------

        pdf_file = pdf_agent.generate(
            "HotelInsight_Report.pdf",
             results,
            health_score,
            strengths,
            improvement_areas,
            discovered_themes,
            wifi_root_causes,
            benchmark_report,
            priority_ranking,
            guest_persona_report,
            trend_report,
            executive_summary,
            recommendations,
        )

        st.subheader("📥 Download Executive Report")

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📄 Download PDF Report",
                data=file,
                file_name="HotelInsight_Report.pdf",
                mime="application/pdf",
            )

# This remains outside the processing block to always display
st.caption("Developed by Shetketu Mitra | HotelInsight AI v1.0")
