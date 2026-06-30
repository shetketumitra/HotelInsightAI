class ConsultantAgent:

    def generate_recommendations(
        self,
        themes
    ):

        recommendations = []

        sorted_themes = sorted(
            themes.items(),
            key=lambda x: x[1],
            reverse=True
        )

        top_themes = sorted_themes[:5]

        recommendation_map = {

            "Room":
            "Improve room quality, maintenance standards, and guest comfort.",

            "Food":
            "Review food quality, breakfast offerings, and menu variety.",

            "Staff":
            "Enhance customer service training and guest engagement programs.",

            "Cleanliness":
            "Strengthen housekeeping inspections and cleanliness standards.",

            "Location":
            "Improve transportation information and local area guidance.",

            "Value":
            "Review pricing strategy and strengthen value-for-money offerings.",

            "WiFi":
            "Upgrade internet speed, reliability, and guest connectivity.",

            "Sleep Quality":
            "Reduce noise levels and improve guest sleep comfort.",

            "Check-In":
            "Streamline check-in and check-out processes.",

            "Amenities":
            "Invest in guest facilities such as gym, pool, and spa services.",

            "Parking":
            "Improve parking availability and accessibility.",

            "Business Services":
            "Enhance meeting facilities and business traveler services.",

            "Security":
            "Strengthen guest safety and security measures.",

            "Family Experience":
            "Improve family-friendly services and children's facilities.",

            "Accessibility":
            "Improve accessibility features and inclusive guest experiences."
        }

        for theme, count in top_themes:

            if theme in recommendation_map:

                recommendations.append(
                    recommendation_map[theme]
                )

        return recommendations