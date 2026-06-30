class PositiveThemeAgent:

    def detect_positive_themes(
        self,
        df,
        review_column
    ):

        themes = {

            "Staff": [
                "staff",
                "service",
                "reception",
                "employee",
                "manager",
                "helpful",
                "friendly"
            ],

            "Room": [
                "room",
                "bed",
                "bathroom",
                "suite",
                "comfortable",
                "shower"
            ],

            "Cleanliness": [
                "clean",
                "spotless",
                "hygiene",
                "tidy"
            ],

            "Food": [
                "food",
                "breakfast",
                "restaurant",
                "meal",
                "buffet"
            ],

            "Location": [
                "location",
                "metro",
                "transport",
                "airport",
                "station"
            ],

            "Value": [
                "value",
                "worth",
                "price"
            ],

            "WiFi": [
                "wifi",
                "internet",
                "connection"
            ],

            "Sleep Quality": [
                "sleep",
                "quiet",
                "peaceful"
            ],

            "Amenities": [
                "pool",
                "gym",
                "spa",
                "fitness"
            ],

            "Parking": [
                "parking",
                "garage"
            ],

            "Security": [
                "safe",
                "security",
                "safety"
            ]
        }

        counts = {}

        reviews = (
            df[review_column]
            .fillna("")
            .astype(str)
            .str.lower()
        )

        for theme, keywords in themes.items():

            count = 0

            for review in reviews:

                if any(
                    keyword in review
                    for keyword in keywords
                ):
                    count += 1

            counts[theme] = count

        return counts