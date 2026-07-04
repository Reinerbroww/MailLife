from copy import deepcopy

# Template hasil analisis MailBrain
ANALYSIS_SCHEMA = {
    "intent": None,
    "email_type": None,
    "purpose": None,
    "recipient": {
        "role": None,
        "name": None
    },
    "tone": None,
    "language": None,
    "reason": None,
    "subject_hint": None,
    "confidence": 0.0
}


def validate_analysis(data: dict) -> dict:
    """
    Memastikan output MailBrain selalu memiliki struktur yang benar.

    Jika ada field yang hilang,
    validator akan mengisinya dengan default value.
    """

    result = deepcopy(ANALYSIS_SCHEMA)

    if not isinstance(data, dict):
        return result

    for key in result:

        if key not in data:
            continue

        # Recipient membutuhkan pengecekan khusus
        if key == "recipient":

            if isinstance(data["recipient"], dict):

                result["recipient"]["role"] = data["recipient"].get("role")

                result["recipient"]["name"] = data["recipient"].get("name")

        else:

            result[key] = data[key]

    # Confidence harus berupa angka
    try:
        result["confidence"] = float(result["confidence"])
    except Exception:
        result["confidence"] = 0.0

    # Batasi confidence 0 - 1
    result["confidence"] = max(
        0.0,
        min(1.0, result["confidence"])
    )

    return result