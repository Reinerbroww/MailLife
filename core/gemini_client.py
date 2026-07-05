import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ==========================================================
# MODEL PRIORITY
# ==========================================================

MODELS = [

    "gemini-2.5-flash",

    "gemini-2.5-flash-lite",

]

# ==========================================================
# CONFIG
# ==========================================================

MAX_RETRY = 3

INITIAL_DELAY = 1

MAX_DELAY = 4

# ==========================================================
# GENERATE
# ==========================================================


def generate(prompt: str) -> str:
    """
    Send prompt to Gemini.

    Features
    --------
    ✅ Retry
    ✅ Exponential Backoff
    ✅ Model Fallback
    ✅ 429 Handling
    ✅ 503 Handling
    ✅ Logging
    """

    last_exception = None

    for model in MODELS:

        print("=" * 60)
        print(f"🤖 Using Model : {model}")
        print("=" * 60)

        delay = INITIAL_DELAY

        for attempt in range(1, MAX_RETRY + 1):

            try:

                print(
                    f"🚀 Attempt {attempt}/{MAX_RETRY}"
                )

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                print(
                    f"✅ Success ({model})"
                )

                return response.text

            except Exception as e:

                last_exception = e

                error = str(e)

                print(
                    f"❌ Attempt {attempt} failed"
                )

                print(error)

                # ------------------------------------------
                # Quota Exceeded (429)
                # ------------------------------------------

                if "429" in error or "RESOURCE_EXHAUSTED" in error:

                    print(
                        "⚠ API quota exceeded."
                    )

                # ------------------------------------------
                # Server Busy (503)
                # ------------------------------------------

                elif "503" in error or "UNAVAILABLE" in error:

                    print(
                        "⚠ Gemini server is busy."
                    )

                # ------------------------------------------
                # Other Errors
                # ------------------------------------------

                else:

                    print(
                        "⚠ Unknown error."
                    )

                if attempt < MAX_RETRY:

                    print(
                        f"⏳ Retry in {delay} sec..."
                    )

                    time.sleep(delay)

                    delay = min(
                        delay * 2,
                        MAX_DELAY
                    )

        print(
            f"\n➡ Switching model...\n"
        )

    raise RuntimeError(

        "All Gemini models failed.\n\n"

        "Possible causes:\n"

        "• API quota exceeded (429)\n"

        "• Gemini server busy (503)\n"

        "• Network connection problem\n\n"

        f"Last Error:\n{last_exception}"

    )