import google.generativeai as genai


class GeminiRootCauseAgent:

    def __init__(self, api_key):

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def analyze(
        self,
        aspect,
        reviews
    ):

        prompt = f"""
You are an experienced hotel management consultant.

The following guest reviews relate to the hotel aspect:

{aspect}

Guest Reviews:

{reviews}

Identify the five most likely root causes behind guest dissatisfaction.

Return only concise bullet points.

Example:

• Slow WiFi speed
• Weak signal on higher floors
• Difficult login portal
• Frequent disconnections
• Paid premium WiFi
"""

        response = self.model.generate_content(prompt)

        return response.text