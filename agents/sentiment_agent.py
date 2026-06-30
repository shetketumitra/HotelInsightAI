from textblob import TextBlob


class SentimentAgent:

    def analyze_sentiment(self, reviews):

        positive = 0
        neutral = 0
        negative = 0

        for review in reviews:

            polarity = TextBlob(str(review)).sentiment.polarity

            if polarity > 0:
                positive += 1

            elif polarity < 0:
                negative += 1

            else:
                neutral += 1

        return {
            "Positive": positive,
            "Neutral": neutral,
            "Negative": negative
        }