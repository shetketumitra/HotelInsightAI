class SchemaAgent:

    def detect_columns(self, df):

        score_column = None
        review_column = None

        positive_review_column = None
        negative_review_column = None

        score_candidates = [
            "reviewer_score",
            "overall",
            "rating",
            "score",
            "review_score",
            "hotel_rating"
        ]

        review_candidates = [
            "review_text",
            "review",
            "comment",
            "feedback",
            "guest_review"
        ]

        for column in df.columns:

            column_lower = column.lower()

            if column_lower in score_candidates:

                score_column = column

                break

        # Generic review column

        for column in df.columns:

            column_lower = column.lower()

            if column_lower in review_candidates:

                review_column = column

                break

        # Positive review column

        for column in df.columns:

            if column.lower() == "positive_review":

                positive_review_column = column

                break

        # Negative review column

        for column in df.columns:

            if column.lower() == "negative_review":

                negative_review_column = column

                break

        return {

            "score_column": score_column,

            "review_column": review_column,

            "positive_review_column":
                positive_review_column,

            "negative_review_column":
                negative_review_column
        }

    def validate_dataset(self, schema):

        if schema["score_column"] is None:

            return (
                False,
                "No score/rating column detected."
            )

        # Dataset can be valid if:
        #
        # 1. review_column exists
        # OR
        # 2. positive + negative review columns exist

        generic_review = (
            schema["review_column"]
            is not None
        )

        hotel_reviews_format = (

            schema["positive_review_column"]
            is not None

            and

            schema["negative_review_column"]
            is not None
        )

        if not (
            generic_review
            or
            hotel_reviews_format
        ):

            return (
                False,
                "No review text column detected."
            )

        return (
            True,
            "Dataset validated successfully."
        )