import google.generativeai as genai


class GeminiCompetitorAgent:

    def __init__(self, api_key):

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def compare(
        self,
        hotel_a,
        hotel_b
    ):

        prompt = f"""
You are a hotel strategy consultant.

Hotel A

{hotel_a}

Hotel B

{hotel_b}

Compare:

• Strengths

• Weaknesses

• Competitive advantages

• Business recommendations

Return an executive comparison.
"""

        response = self.model.generate_content(
            prompt
        )

        return response.text