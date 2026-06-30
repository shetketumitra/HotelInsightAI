class DatasetAgent:

    def detect_dataset(
        self,
        schema
    ):

        if (
            schema["positive_review_column"]
            is not None
            and
            schema["negative_review_column"]
            is not None
        ):

            return "hotel_reviews"

        return "generic_reviews"