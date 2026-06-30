class RootCauseAgent:

    def collect_reviews(
        self,
        df,
        review_column,
        aspect,
        limit=50
    ):

        reviews = []

        for review in (
            df[review_column]
            .fillna("")
            .astype(str)
        ):

            text = review.lower()

            if aspect.lower() in text:

                reviews.append(review)

            if len(reviews) >= limit:
                break

        return reviews