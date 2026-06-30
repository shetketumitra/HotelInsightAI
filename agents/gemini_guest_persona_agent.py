import google.generativeai as genai


class GeminiGuestPersonaAgent:

    def __init__(self, api_key):

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def identify_personas(
        self,
        reviews
    ):

        prompt = f"""
You are a hospitality consultant.

Guest Reviews

{reviews}

Identify the major guest personas.

Examples:

• Business Travellers

• Families

• Couples

• Solo Travellers

• Luxury Guests

• Budget Travellers

For each persona explain:

• Percentage (estimate)

• Expectations

• Satisfaction

Keep the answer concise.
"""

        response = self.model.generate_content(
            prompt
        )

        return response.text