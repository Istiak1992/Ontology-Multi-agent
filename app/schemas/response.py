from pydantic import BaseModel

class TranslationResponse(BaseModel):
    input_text: str
    source_language: str
    target_language: str
    translated_text: str
    sentiment: str
    safety: str