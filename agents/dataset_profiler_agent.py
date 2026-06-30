import pandas as pd


class DatasetProfilerAgent:

    def profile(self, df):

        profile = {
            "dataset_type": "unknown",
            "review_column": None,
            "score_column": None,
            "positive_review_column": None,
            "negative_review_column": None,
            "hotel_column": None,
            "hotel_id_column": None,
            "country_column": None,
            "city_column": None,
            "location_column": None,
            "date_column": None,
            "user_column": None,
            "room_type_column": None,
            "trip_type_column": None,
            "language_column": None,
            "source_column": None,
            "row_count": len(df),
            "column_count": len(df.columns),
            "columns": list(df.columns)
        }

        # -------------------------
        # REVIEW COLUMNS
        # -------------------------

        review_candidates = [
            "review_text", "reviews", "review_body", "review_content",
            "content", "comment", "comments", "text", "description",
            "guest_review", "customer_review", "review_title", "full_review",
            "reviews_text"
        ]

        for candidate in review_candidates:
            for col in df.columns:
                if candidate in col.lower():
                    profile["review_column"] = col
                    break
            if profile["review_column"]:
                break

        # -------------------------
        # BOOKING DATASETS
        # -------------------------

        for col in df.columns:
            lower = col.lower()
            if "positive_review" in lower:
                profile["positive_review_column"] = col
            if "negative_review" in lower:
                profile["negative_review_column"] = col

        # ----------------------------------
        # BOOKING REVIEW COLUMN FALLBACK
        # ----------------------------------

        if (
            profile["positive_review_column"]
            and
            profile["negative_review_column"]
        ):
            profile["review_column"] = profile["positive_review_column"]

        # -------------------------
        # SCORE COLUMNS
        # -------------------------

        score_candidates = [
            "score", "rating", "review_score", "reviewer_score", "hotel_score",
            "overall", "overall_score", "stars", "star_rating", "guest_rating",
            "customer_rating", "review_rating", "rank"
        ]

        for candidate in score_candidates:
            for col in df.columns:
                if candidate in col.lower():
                    profile["score_column"] = col
                    break
            if profile["score_column"]:
                break

        # -------------------------
        # HOTEL NAME
        # -------------------------

        hotel_candidates = [
            "hotel_name", "hotel", "property", "property_name", "accommodation",
            "resort", "hotel_title", "hotelname", "name"
        ]

        for candidate in hotel_candidates:
            for col in df.columns:
                if candidate in col.lower():
                    profile["hotel_column"] = col
                    break
            if profile["hotel_column"]:
                break

        # -------------------------
        # HOTEL ID
        # -------------------------

        hotel_id_candidates = ["hotel_id", "property_id", "listing_id", "hotelid"]

        for candidate in hotel_id_candidates:
            for col in df.columns:
                if candidate in col.lower():
                    profile["hotel_id_column"] = col
                    break
            if profile["hotel_id_column"]:
                break

        # -------------------------
        # COUNTRY
        # -------------------------

        country_candidates = ["country", "reviewer_country", "guest_country", "nationality"]

        for candidate in country_candidates:
            for col in df.columns:
                if candidate in col.lower():
                    profile["country_column"] = col
                    break
            if profile["country_column"]:
                break

        # -------------------------
        # CITY / LOCATION / DATE / USER / ROOM / TRIP
        # -------------------------

        # -------------------------
        # DATE COLUMN
        # -------------------------

        date_candidates = [
            "review_date",
            "date",
            "reviewdate",
            "created_at",
            "created",
            "timestamp",
            "stay_date",
            "travel_date"
        ]

        for candidate in date_candidates:
            for col in df.columns:
                if candidate in col.lower():
                    profile["date_column"] = col
                    break
            if profile["date_column"]:
                break

        # -------------------------
        # EXTRA STATISTICS
        # -------------------------

        profile["missing_values"] = df.isna().sum().to_dict()

        confidence = 0
        if (
            profile["review_column"]
            or (
                profile["positive_review_column"]
                and profile["negative_review_column"]
            )
        ):
            confidence += 20
        if profile["score_column"]:
            confidence += 20
        if profile["hotel_column"]:
            confidence += 20
        if profile["country_column"]:
            confidence += 20
        if profile["date_column"]:
            confidence += 20

        profile["confidence"] = confidence

        # -------------------------
        # DATASET TYPE LOGIC
        # -------------------------

        # BOOKING
        if profile["positive_review_column"] and profile["negative_review_column"]:
            profile["dataset_type"] = "Booking Reviews"

        # TRIPADVISOR
        elif any("rating" in c.lower() for c in df.columns):
            profile["dataset_type"] = "TripAdvisor Reviews"

        # DATAFINITI
        elif any("reviews." in c.lower() for c in df.columns):
            profile["dataset_type"] = "Datafiniti Reviews"

        # GENERIC
        else:
            profile["dataset_type"] = "Generic Reviews"

        profile["dataset_signature"] = "|".join(
            sorted([c.lower() for c in df.columns])
        )

        return profile