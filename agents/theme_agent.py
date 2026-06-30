from textblob import TextBlob


class ThemeAgent:

    def detect_themes(
        self,
        df,
        review_column
    ):

        themes = {

            "Staff": [
                "staff",
                "employee",
                "manager",
                "service",
                "reception",
                "receptionist",
                "front desk",
                "concierge",
                "housekeeping",
                "waiter",
                "waitress",
                "host",
                "hostess",
                "team"
            ],

            "Room": [
                "room",
                "bed",
                "bathroom",
                "mattress",
                "pillow",
                "suite",
                "shower",
                "toilet",
                "air conditioning",
                "ac",
                "heating",
                "window",
                "balcony",
                "furniture",
                "lighting",
                "noise"
            ],

            "Cleanliness": [
                "clean",
                "dirty",
                "smell",
                "dust",
                "stain",
                "hygiene",
                "spotless"
            ],

            "Food": [
                "food",
                "breakfast",
                "lunch",
                "dinner",
                "restaurant",
                "buffet",
                "coffee",
                "tea",
                "menu",
                "meal",
                "dessert",
                "bar",
                "drinks"
            ],

            "Location": [
                "location",
                "metro",
                "transport",
                "airport",
                "station",
                "walking distance"
            ],

            "Value": [
                "value",
                "price",
                "expensive",
                "cheap",
                "cost",
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
                "quiet",
                "noise",
                "loud",
                "peaceful"
            ],

            "Check-In": [
                "check in",
                "check-in",
                "check out",
                "checkout",
                "arrival",
                "departure"
            ],

            "Amenities": [
                "gym",
                "pool",
                "spa",
                "sauna",
                "fitness",
                "facility",
                "facilities"
            ],

            "Parking": [
                "parking",
                "car park",
                "garage"
            ],

            "Business Services": [
                "business",
                "meeting",
                "conference",
                "event",
                "workspace"
            ],

            "Security": [
                "security",
                "safe",
                "safety"
            ],

            "Family Experience": [
                "family",
                "kids",
                "children"
            ],

            "Accessibility": [
                "wheelchair",
                "accessible",
                "disabled",
                "accessibility"
            ]
        }

        counts = {}

        for theme in themes:

            counts[theme] = {
                "total": 0,
                "positive": 0,
                "negative": 0
            }

        reviews = (
            df[review_column]
            .fillna("")
            .astype(str)
            .str.lower()
        )

        for review in reviews:

            polarity = (
                TextBlob(review)
                .sentiment
                .polarity
            )

            for theme, keywords in themes.items():

                if any(
                    keyword in review
                    for keyword in keywords
                ):

                    counts[theme]["total"] += 1

                    if polarity > 0:

                        counts[theme]["positive"] += 1

                    elif polarity < 0:

                        counts[theme]["negative"] += 1

        return counts