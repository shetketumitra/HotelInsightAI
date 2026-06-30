import google.generativeai as genai


class GeminiBenchmarkAgent:

    def __init__(self, api_key):

        genai.configure(
            api_key=api_key
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def benchmark(

        self,

        health_score,

        average_score,

        strengths,

        improvement_areas

    ):

        prompt = f"""
You are a senior hospitality consultant.

Hotel Performance

Health Score:
{health_score}/100

Average Rating:
{average_score}/10

Strengths:
{strengths}

Improvement Areas:
{improvement_areas}

Compare this hotel against an average 4-star hotel.

Explain:

1. Overall Benchmark

2. Competitive Position

3. Biggest Competitive Advantage

4. Biggest Competitive Weakness

Keep the answer concise.
"""

        response = self.model.generate_content(
            prompt
        )

        return response.text