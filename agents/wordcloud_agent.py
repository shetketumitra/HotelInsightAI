from wordcloud import WordCloud, STOPWORDS


class WordCloudAgent:

    def generate(self, reviews):

        text = " ".join(
            reviews
            .fillna("")
            .astype(str)
        )

        stopwords = set(STOPWORDS)
        stopwords.update(
            {
                "hotel",
                "room",
                "rooms",
                "stay",
                "stayed",
                "good",
                "great",
                "nice",
                "bed",
                "night",
                "really",
                "very",
                "one",
                "would",
                "also",
                "get",
                "got",
                "even",
                "much",
                "well",
                "could",
                "hotelroom"
            }
        )

        wordcloud = WordCloud(
            width=1200,
            height=600,
            background_color="white",
            stopwords=stopwords,
            max_words=150
        ).generate(text)

        return wordcloud.to_array()