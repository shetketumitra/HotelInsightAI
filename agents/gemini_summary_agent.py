import google.generativeai as genai


class GeminiSummaryAgent:

    def __init__(
        self,
        api_key
    ):

        genai.configure(
            api_key=api_key
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate_summary(
        self,
        average_score,
        health_score,
        strengths,
        improvement_areas
    ):

        prompt = f"""
You are a hotel business consultant.

Create a professional executive summary.

Average Review Score:
{average_score}

Health Score:
{health_score}/100

Top Strengths:
{strengths}

Top Improvement Areas:
{improvement_areas}

Write:
1. Overall hotel performance
2. Key strengths
3. Key weaknesses
4. Management recommendations

Maximum 200 words.
"""

        response = (
            self.model.generate_content(
                prompt
            )
        )

        return response.text