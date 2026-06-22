from app.ontology.core import (
    LanguageOntology,
    SentimentOntology,
    SafetyOntology
)


class FormatterAgent:

    def __init__(self):
        self.lang_onto = LanguageOntology()
        self.sentiment_onto = SentimentOntology()
        self.safety_onto = SafetyOntology()

    def execute(
        self,
        text,
        source_lang,
        target_lang,
        translation,
        sentiment,
        safety
    ):

        return {
            "input_text": text,

            "source_language": {
                "code": source_lang,
                "name": self.lang_onto.LANGUAGES
                    .get(source_lang, {})
                    .get("name", "Unknown")
            },

            "target_language": {
                "code": target_lang,
                "name": self.lang_onto.LANGUAGES
                    .get(target_lang, {})
                    .get("name", "Unknown")
            },

            "translated_text": translation,

            "sentiment": {
                "label": sentiment.get("label"),
                "score": sentiment.get("score"),
                "description": self.sentiment_onto.DESCRIPTIONS.get(
                    sentiment.get("label"),
                    "Unknown sentiment"
                )
            },

            "safety": {
                **safety,
                "risk_level": self.safety_onto.risk_level(safety)
            }
        }