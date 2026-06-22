class LanguageOntology:

    LANGUAGES = {
    "eng_Latn": {"name": "English"},
    "swe_Latn": {"name": "Swedish"},
    "hin_Deva": {"name": "Hindi"},
    "ben_Beng": {"name": "Bengali"},
    "spa_Latn": {"name": "Spanish"},
    "fra_Latn": {"name": "French"},
    "deu_Latn": {"name": "German"},
    "ita_Latn": {"name": "Italian"},
    "por_Latn": {"name": "Portuguese"},
    "rus_Cyrl": {"name": "Russian"},
    "ara_Arab": {"name": "Arabic"},
    "jpn_Jpan": {"name": "Japanese"},
    "kor_Hang": {"name": "Korean"},
    "zho_Hans": {"name": "Chinese (Simplified)"},
    "zho_Hant": {"name": "Chinese (Traditional)"},
    "tur_Latn": {"name": "Turkish"},
    "nld_Latn": {"name": "Dutch"},
    "pol_Latn": {"name": "Polish"},
    "ukr_Cyrl": {"name": "Ukrainian"},
    "vie_Latn": {"name": "Vietnamese"},
    "tha_Thai": {"name": "Thai"},
    "ind_Latn": {"name": "Indonesian"},
    "msa_Latn": {"name": "Malay"},
    "fas_Arab": {"name": "Persian"},
    "urd_Arab": {"name": "Urdu"},
    "tam_Taml": {"name": "Tamil"},
    "tel_Telu": {"name": "Telugu"},
    "mar_Deva": {"name": "Marathi"},
    "guj_Gujr": {"name": "Gujarati"},
    "kan_Knda": {"name": "Kannada"},
    "mal_Mlym": {"name": "Malayalam"},
    "pan_Guru": {"name": "Punjabi"},
}


class SentimentOntology:

    DESCRIPTIONS = {
        "POSITIVE": "User expresses positive emotion",
        "NEGATIVE": "User expresses negative emotion",
        "NEUTRAL": "Neutral emotional tone"
    }


class SafetyOntology:

    @staticmethod
    def risk_level(scores):
        toxicity = scores.get("toxicity", 0)

        if toxicity > 0.7:
            return "HIGH"
        elif toxicity > 0.3:
            return "MEDIUM"
        return "LOW"