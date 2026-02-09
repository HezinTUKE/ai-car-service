import json
import logging

from requests import post
from application.utils.globals import extract_question_data_prompt, translate_prompt


logger = logging.getLogger(" ")


def embedding(text: str):
    normalized_text = "".join(text.strip().strip())
    response = post(
        url="http://localhost:11434/api/embeddings", json={"model": "nomic-embed-text", "prompt": normalized_text}
    )
    return response.json()["embedding"]


def question_encoding(question: str) -> dict | None:
    try:
        request = post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3:8b",
                "prompt": f"{extract_question_data_prompt}\nQuestion: {question}",
                "stream": False,
            },
        )

        if request.status_code != 200:
            return None

        res = request.json()["response"]
        return json.loads(res)
    except Exception:
        logger.error(f"Failed to understand question {question}", exc_info=True)
        return None


def translate(text: str) -> str | None:
    try:
        request = post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3:8b",
                "prompt": f"{translate_prompt}:\n{text}",
                "stream": False,
            },
        )

        if request.status_code != 200:
            return None

        translated_text: str = request.json()["response"]
        return translated_text.strip().replace("\n", " ")
    except Exception:
        logger.error(f"Failed to translate {text}", exc_info=True)
        return None
