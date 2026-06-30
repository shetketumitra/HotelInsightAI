class SummaryAgent:

    def generate_summary(
        self,
        average_score,
        improvement_areas
    ):

        if len(improvement_areas) < 3:

            return (
                f"Average guest satisfaction score is "
                f"{average_score}/10."
            )

        summary = f"""
Average guest satisfaction score is {average_score}/10.

Top operational concerns identified:

1. {improvement_areas[0][0]}
2. {improvement_areas[1][0]}
3. {improvement_areas[2][0]}

Management should prioritize these areas to improve guest satisfaction and operational performance.
"""

        return summary.strip()

    def get_priority_ranking(
        self,
        improvement_areas
    ):

        ranking = []

        for item in improvement_areas:

            ranking.append(
                (
                    item[0],
                    item[1]
                )
            )

        return ranking[:3]