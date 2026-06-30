from textblob import TextBlob


class AspectSentimentAgent:

    def analyze(
        self,
        df,
        review_column
    ):

        themes = {

            "Staff": [
                "staff",
                "service",
                "reception",
                "receptionist",
                "employee",
                "manager",
                "concierge",
                "front desk",
                "housekeeping"
            ],

            "Room": [
                "room",
                "bed",
                "bathroom",
                "suite",
                "shower",
                "toilet",
                "mattress",
                "pillow",
                "furniture",
                "balcony"
            ],

            "Cleanliness": [
                "clean",
                "dirty",
                "dust",
                "stain",
                "smell",
                "hygiene"
            ],

            "Food": [
                "food",
                "breakfast",
                "lunch",
                "dinner",
                "buffet",
                "restaurant",
                "meal",
                "coffee"
            ],

            "Location": [
                "location",
                "metro",
                "station",
                "airport",
                "transport"
            ],

            "Value": [
                "value",
                "price",
                "expensive",
                "cheap",
                "money",
                "worth"
            ],

            "WiFi": [
                "wifi",
                "internet",
                "network",
                "connection"
            ],

            "Sleep Quality": [
                "sleep",
                "noise",
                "quiet",
                "peaceful"
            ],

            "Check-In": [
                "check in",
                "check-in",
                "checkout",
                "check out"
            ],

            "Amenities": [
                "pool",
                "gym",
                "spa",
                "fitness",
                "facility"
            ]
        }

        results = {}

        for theme in themes:

            results[theme] = {
                "positive": 0,
                "negative": 0
            }

        reviews = (
            df[review_column]
            .fillna("")
            .astype(str)
        )

        for review in reviews:

            try:

                sentences = (
                    TextBlob(review)
                    .sentences
                )

            except:

                sentences = [review]

            for sentence in sentences:

                sentence_text = (
                    str(sentence)
                    .lower()
                )

                polarity = (
                    TextBlob(sentence_text)
                    .sentiment
                    .polarity
                )

                for theme, keywords in themes.items():

                    if any(
                        keyword in sentence_text
                        for keyword in keywords
                    ):

                        if polarity > 0:

                            results[theme][
                                "positive"
                            ] += 1

                        elif polarity < 0:

                            results[theme][
                                "negative"
                            ] += 1

        return results