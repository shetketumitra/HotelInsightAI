import google.generativeai as genai


class GeminiConsultantAgent:

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

    def generate_recommendations(
        self,
        health_score,
        strengths,
        improvement_areas
    ):

        prompt = f"""
You are a senior hotel operations consultant.

Hotel Health Score:
{health_score}/100

Hotel Strengths:
{strengths}

Improvement Areas:
{improvement_areas}

Generate:

1. Five executive recommendations
2. Practical and actionable
3. Hotel industry focused
4. Short bullet points

Return only the recommendations.
"""

        response = self.model.generate_content(
            prompt
        )

        recommendations = []

        for line in response.text.split("\n"):

            line = line.strip()

            if len(line) > 10:

                recommendations.append(
                    line
                )

        return recommendations