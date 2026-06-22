from app.models.model_loader import sentiment_model


class SentimentAgent:

    def execute(self, text):

        result = sentiment_model(text)[0]

        return {
            "label": result["label"],
            "score": float(result["score"])
        }