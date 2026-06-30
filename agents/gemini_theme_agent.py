import google.generativeai as genai


class GeminiThemeAgent:

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

    def discover_themes(
        self,
        reviews
    ):

        sample_reviews = "\n".join(
            reviews[:100]
        )

        prompt = f"""
You are a hotel review analyst.

Analyze the reviews below.

Identify the 10 most important
themes being discussed.

Return only a bullet list.

Reviews:

{sample_reviews}
"""

        response = (
            self.model.generate_content(
                prompt
            )
        )

        return response.text