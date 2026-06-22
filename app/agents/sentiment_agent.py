from dataclasses import dataclass
from typing import Dict


@dataclass
class SentimentResult:
    label: str
    score: float


class SentimentAgent:
   
    def __init__(self):
        # basic lexicon (expand later or replace with model)
        self.positive_words = {
            "good", "great", "excellent", "awesome", "happy",
            "love", "like", "amazing", "positive", "nice"
        }

        self.negative_words = {
            "bad", "terrible", "awful", "hate", "poor",
            "sad", "angry", "worst", "negative", "dislike"
        }

    def execute(self, text: str) -> Dict:
        """
        Main entry point used by orchestrator.
        """
        sentiment = self.analyze(text)
        return {
            "agent": "sentiment",
            "label": sentiment.label,
            "score": sentiment.score
        }

    def analyze(self, text: str) -> SentimentResult:
        """
        Core sentiment logic.
        """
        if not text:
            return SentimentResult(label="neutral", score=0.0)

        words = text.lower().split()

        pos_count = sum(1 for w in words if w in self.positive_words)
        neg_count = sum(1 for w in words if w in self.negative_words)

        total = pos_count + neg_count

        if total == 0:
            return SentimentResult(label="neutral", score=0.5)

        score = pos_count / total

        if pos_count > neg_count:
            label = "positive"
        elif neg_count > pos_count:
            label = "negative"
        else:
            label = "neutral"

        return SentimentResult(label=label, score=round(score, 3))