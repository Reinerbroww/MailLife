import json

from core.gemini_client import generate
from prompts.writer_prompt import WRITER_PROMPT
from utils.json_parser import extract_json


class MailWriter:
    """
    MailWriter bertugas membuat draft email
    berdasarkan hasil analisis MailBrain.
    """

    def write(self, analysis: dict) -> dict:

        prompt = f"""
{WRITER_PROMPT}

MailBrain Analysis:

{json.dumps(analysis, indent=4)}
"""

        result = generate(prompt)

        print("\n===== MAIL WRITER =====")

        print(result)

        print("=======================\n")

        draft = extract_json(result)

        return draft