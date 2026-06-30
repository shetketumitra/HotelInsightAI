class ReviewAgent:

    def analyze_reviews(
        self,
        df,
        score_column
    ):

        total_reviews = len(df)

        average_score = round(
            df[score_column]
            .fillna(0)
            .mean(),
            2
        )

        highest_score = round(
            df[score_column]
            .fillna(0)
            .max(),
            2
        )

        lowest_score = round(
            df[score_column]
            .fillna(0)
            .min(),
            2
        )

        return {

            "total_reviews": total_reviews,

            "average_score": average_score,

            "highest_score": highest_score,

            "lowest_score": lowest_score
        }