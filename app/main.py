from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.schemas.request import (
    TranslationRequest
)

from app.services.orchestrator import (
    MultiAgentTranslator
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


translator = MultiAgentTranslator()


@app.get("/")
def home():

    return {
        "message":
        "Multi-Agent Translator Running"
    }


@app.post("/translate")
def translate(
    request: TranslationRequest
):

    return translator.execute(
        request.text,
        request.source_lang,
        request.target_lang
    )