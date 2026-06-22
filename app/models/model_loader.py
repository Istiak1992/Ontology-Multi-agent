import os
import torch
from dotenv import load_dotenv
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    pipeline
)
from detoxify import Detoxify

# Load .env
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_NAME = "facebook/nllb-200-distilled-600M"

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    use_fast=False,
    token=HF_TOKEN
)

print("Loading translation model...")

translation_model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    token=HF_TOKEN
)

device = "cuda" if torch.cuda.is_available() else "cpu"
translation_model.to(device)

print("Loading sentiment model...")

sentiment_model = pipeline("sentiment-analysis")

print("Loading toxicity model...")

toxicity_model = Detoxify("original")

print("All models loaded.")