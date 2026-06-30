class HealthScoreAgent:

    def calculate(
        self,
        average_score,
        max_score
    ):

        return round(
            (
                average_score / max_score
            ) * 100,
            1
        )