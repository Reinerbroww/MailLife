import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Prioritas model
MODELS = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
]

MAX_RETRY = 3
RETRY_DELAY = 2  # detik


def generate(prompt: str) -> str:
    """
    Mengirim prompt ke Gemini.

    Fitur:
    - Retry otomatis
    - Fallback model
    - Logging
    """

    last_exception = None

    for model in MODELS:

        print(f"\n🤖 Trying model: {model}")

        for attempt in range(1, MAX_RETRY + 1):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                print(f"✅ Success using {model}")

                return response.text

            except Exception as e:

                last_exception = e

                print(
                    f"⚠ Attempt {attempt}/{MAX_RETRY} failed on {model}"
                )

                if attempt < MAX_RETRY:
                    print(f"⏳ Waiting {RETRY_DELAY} seconds...")
                    time.sleep(RETRY_DELAY)

        print(f"❌ Switching to next model...\n")

    raise RuntimeError(
        f"All Gemini models failed.\n\nLast Error:\n{last_exception}"
    )