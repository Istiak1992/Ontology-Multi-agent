# 🌍 Multi-Agent Translation API with Ontology-Aware AI

An AI-powered translation system built with **FastAPI** and a **multi-agent architecture**, enhanced with **ontology-based semantic modeling** for structured language understanding.

---

## 🚀 Overview

This project implements a modular AI translation API that enriches translation output with:

* 🌐 Multilingual Translation
* 😊 Sentiment Analysis
* 🛡️ Safety & Toxicity Detection
* 🧠 Ontology-based semantic structuring
* ⚡ RESTful API (FastAPI)
* 📊 Machine-readable JSON responses

---

## ▶️ Run the Project

Start the server:

```bash
python run.py
```

The API will run at:

```
http://127.0.0.1:8080
```

Swagger documentation:

```
http://127.0.0.1:8080/docs
```

---

## 📡 API Usage

### Endpoint

`POST /translate`

---

## 📥 Request Example

```json
{
  "text": "Jag älskar ML.Var du komma från?",
  "source_lang": "swe_Latn",
  "target_lang": "eng_Latn"
}
```

---

## 🔗 cURL Example

```bash
curl -X POST \
  "http://127.0.0.1:8080/translate" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Jag älskar ML.Var du komma från?",
    "source_lang": "swe_Latn",
    "target_lang": "eng_Latn"
  }'
```

---

## 📤 Response Example

```json
{
  "input_text": "Jag älskar ML.Var du komma från?",
  "source_language": {
    "code": "swe_Latn",
    "name": "Swedish"
  },
  "target_language": {
    "code": "eng_Latn",
    "name": "English"
  },
  "translated_text": "I love ML. Where did you come from?",
  "sentiment": {
    "label": "NEGATIVE",
    "score": 0.996677041053772,
    "description": "User expresses negative emotion"
  },
  "safety": {
    "toxicity": 0.00919726025313139,
    "insult": 0.0004238340479787439,
    "threat": 0.000129782099975273,
    "identity_attack": 0.0002205293858423829,
    "risk_level": "LOW"
  }
}
```

---

## 🧠 Ontology-Based AI Design

This system uses **ontology concepts** to structure meaning across AI components.

### Key Ideas:

* **Entity Representation**

  * Language, sentiment, and safety are modeled as structured entities

* **Relationship Modeling**

  * Translation, sentiment, and safety are interconnected knowledge components

* **Semantic Interoperability**

  * All agents follow a unified schema

* **Knowledge Abstraction**

  * Separates raw NLP processing from structured meaning representation

---

## ⚙️ Features

### 🌐 Translation Agent

Supports language pairs using codes like:

* `swe_Latn` → Swedish
* `eng_Latn` → English

---

### 😊 Sentiment Analysis Agent

Detects emotional tone:

* Positive
* Neutral
* Negative

---

### 🛡️ Safety Agent

Detects harmful or unsafe content:

* Toxicity
* Insults
* Threats
* Identity attacks

---

## 🏗️ Architecture

```
User Input
    │
    ▼
Translation Agent
    │
    ├──► Sentiment Agent
    │
    ├──► Safety Agent
    │
    └──► Ontology Mapping Layer
            │
            ▼
     Structured JSON Response
```

---

## 🛠️ Tech Stack

* FastAPI
* Python
* Hugging Face Transformers
* NLLB Models
* Pydantic
* Ontology-driven AI design

---

## 🔮 Future Improvements

* RDF/OWL-based formal ontology integration
* Knowledge graph backend (Neo4j)
* Streaming translation API
* Docker deployment
* Multi-agent LLM orchestration

---

## 👨‍💻 Author

**Istiak Ahmed**

AI Consultant | ML Engineer | DevOps Enthusiast
