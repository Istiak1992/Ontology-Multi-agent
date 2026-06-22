from app.agents.translation_agent import (
    TranslationAgent
)

from app.agents.sentiment_agent import (
    SentimentAgent
)

from app.agents.safety_agent import (
    SafetyAgent
)

from app.agents.formatter_agent import (
    FormatterAgent
)


class MultiAgentTranslator:

    def __init__(self):

        self.translation_agent = (
            TranslationAgent()
        )

        self.sentiment_agent = (
            SentimentAgent()
        )

        self.safety_agent = (
            SafetyAgent()
        )

        self.formatter_agent = (
            FormatterAgent()
        )

    def execute(
        self,
        text,
        source_lang,
        target_lang
    ):

        sentiment = (
            self.sentiment_agent.execute(text)
        )

        safety = (
            self.safety_agent.execute(text)
        )

        translation = (
            self.translation_agent.execute(
                text,
                source_lang,
                target_lang
            )
        )

        return self.formatter_agent.execute(
            text,
            source_lang,
            target_lang,
            translation,
            sentiment,
            safety
        )