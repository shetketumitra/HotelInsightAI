import google.generativeai as genai


class GeminiTrendAgent:

    def __init__(self, api_key):

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def analyze_trends(
        self,
        trend_data
    ):

        prompt = f"""
You are a senior hospitality business consultant.

The following represents hotel performance over time.

{trend_data}

Analyze:

1. Overall trend

2. Whether guest satisfaction is improving or declining

3. Possible business reasons

4. Management recommendations

Keep the answer concise.
"""

        response = self.model.generate_content(
            prompt
        )

        return response.text