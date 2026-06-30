class RecommendationAgent:

    def generate(
        self,
        improvement_areas
    ):

        recommendations = []

        recommendation_map = {

            "Room":
                "Renovate rooms and improve room maintenance standards.",

            "Staff":
                "Conduct staff training focused on customer service excellence.",

            "Cleanliness":
                "Strengthen housekeeping inspections and cleanliness audits.",

            "Food":
                "Review menu quality, breakfast variety and restaurant operations.",

            "Location":
                "Provide transportation support and local area guidance.",

            "Value":
                "Review pricing strategy and improve value-added services.",

            "WiFi":
                "Upgrade internet infrastructure and monitor connectivity issues.",

            "Sleep Quality":
                "Improve soundproofing and reduce guest room noise levels.",

            "Check-In":
                "Streamline check-in/check-out procedures and reduce wait times.",

            "Amenities":
                "Upgrade and maintain hotel facilities and guest amenities."
        }

        for theme_data in improvement_areas:

            theme = theme_data[0]

            if theme in recommendation_map:

                recommendations.append(
                    recommendation_map[theme]
                )

        return recommendations