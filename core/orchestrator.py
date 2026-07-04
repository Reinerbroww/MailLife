import time

from agents.planner import MailBrain
from agents.writer import MailWriter
from agents.reviewer import MailReviewer
from utils.observer import Observer

class MailLifeOrchestrator:
    """
    MailLife Orchestrator

    Bertugas mengatur workflow seluruh AI Agent.

    Workflow:
        User
          ↓
      MailBrain
          ↓
      MailWriter
          ↓
      MailReviewer
          ↓
      Final Email
    """

    def __init__(self):
        self.brain = MailBrain()
        self.writer = MailWriter()
        self.reviewer = MailReviewer()
        self.observer = Observer()

    def generate_email(self, user_request: str) -> dict:

        self.observer.start_session()
        print("🧠 MailBrain is analyzing...")

        analysis = self.brain.analyze(user_request)

        print("✅ Analysis completed.")

        # Jika confidence terlalu rendah, hentikan proses
        confidence = analysis.get("confidence", 0)

        if confidence < 0.50:
            return {
                "status": "failed",
                "message": "The request is too unclear. Please provide more details.",
                "analysis": analysis
            }

        print("✍️ MailWriter is drafting...")

        draft = self.writer.write(analysis)

        print("✅ Draft completed.")

        print("🔍 MailReviewer is reviewing...")

        final = self.reviewer.review(draft)

        print("✅ Review completed.")

        self.observer.end_session()

        return {
            "status": "success",
            "analysis": analysis,
            "draft": draft,
            "final": final,
            "observer": self.observer
        }