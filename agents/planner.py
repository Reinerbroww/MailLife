from core.gemini_client import generate
from prompts.planner_prompt import PLANNER_PROMPT
from utils.json_parser import extract_json
from utils.validator import validate_analysis


class MailBrain:
    """
    MailBrain bertugas menganalisis kebutuhan user.

    Tugas:
    - Memahami intent user
    - Mengidentifikasi penerima email
    - Menentukan tone
    - Menentukan bahasa
    - Memberikan subject hint

    MailBrain TIDAK menulis email.
    """

    def analyze(self, user_request: str) -> dict:

        prompt = f"""
{PLANNER_PROMPT}

User Request:

{user_request}
"""

        result = generate(prompt)

        print("\n===== RAW GEMINI RESPONSE =====")
        print(result)
        print("===============================\n")

        analysis = extract_json(result)

        analysis = validate_analysis(analysis)

        print("===== VALIDATION =====")

        missing = []

        for key, value in analysis.items():

            if value is None:
                missing.append(key)

        if missing:
            print("⚠ Missing:", ", ".join(missing))
        else:
            print("✅ All required fields are present.")

        print("======================")

        print("===== PARSED JSON =====")

        print(analysis)

        print("=======================\n")

        return analysis