class InsightsAgent:

    def get_strengths(
        self,
        aspect_results
    ):

        scores = []

        for theme, data in aspect_results.items():

            net_score = (
                data["positive"]
                - data["negative"]
            )

            scores.append(
                (
                    theme,
                    net_score,
                    data["positive"],
                    data["negative"]
                )
            )

        scores = sorted(
            scores,
            key=lambda x: x[1],
            reverse=True
        )

        return scores[:3]


    def get_improvement_areas(
        self,
        aspect_results
    ):

        scores = []

        for theme, data in aspect_results.items():

            net_score = (
                data["positive"]
                - data["negative"]
            )

            scores.append(
                (
                    theme,
                    net_score,
                    data["positive"],
                    data["negative"]
                )
            )

        scores = sorted(
            scores,
            key=lambda x: x[1]
        )

        return scores[:3]