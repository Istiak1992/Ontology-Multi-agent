from app.models.model_loader import toxicity_model


class SafetyAgent:

    def execute(self, text):

        result = toxicity_model.predict(text)

        return {
            "toxicity": float(
                result["toxicity"]
            ),
            "insult": float(
                result["insult"]
            ),
            "threat": float(
                result["threat"]
            ),
            "identity_attack": float(
                result["identity_attack"]
            )
        }