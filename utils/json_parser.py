import json
import re


def extract_json(text: str) -> dict:
    """
    Membersihkan output Gemini dan mengubahnya menjadi dictionary.
    """

    cleaned = re.sub(r"```json|```", "", text).strip()

    return json.loads(cleaned)