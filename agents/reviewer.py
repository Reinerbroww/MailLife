import json

from core.gemini_client import generate
from prompts.reviewer_prompt import REVIEWER_PROMPT
from utils.json_parser import extract_json


class MailReviewer:
    """
    MailReviewer bertugas mengevaluasi draft email.

    Reviewer akan:

    - Memperbaiki grammar
    - Memperbaiki profesionalisme
    - Memberikan Quality Score
    - Memberikan Suggestions
    """

    def review(self, draft: dict) -> dict:

        prompt = f"""
{REVIEWER_PROMPT}

MailWriter Draft:

{json.dumps(draft, indent=4)}
"""

        result = generate(prompt)

        print("\n===== MAIL REVIEWER =====")

        print(result)

        print("=========================\n")

        review = extract_json(result)

        return review