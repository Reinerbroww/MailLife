from core.orchestrator import MailLifeOrchestrator


def section(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def show_analysis(analysis: dict):
    section("🧠 MAILBRAIN ANALYSIS")

    for key, value in analysis.items():
        print(f"{key}: {value}")


def show_draft(draft: dict):
    section("✍️ MAILWRITER DRAFT")

    print(f"Subject : {draft['subject']}\n")
    print(draft["body"])


def show_review(review: dict):
    section("🔍 MAILREVIEWER FINAL")

    print(f"Subject : {review['subject']}\n")
    print(review["body"])

    section("📊 REVIEW REPORT")

    print(f"Quality Score : {review['quality_score']}/100")

    print("\nChanges:")

    for change in review["changes"]:
        print(f" • {change}")

    print("\nSuggestions:")

    if review["suggestions"]:
        for suggestion in review["suggestions"]:
            print(f" • {suggestion}")
    else:
        print(" • No suggestions.")


def show_observability(observer):
    section("📊 SESSION OBSERVABILITY")

    print(f"AI Calls      : {observer.ai_calls}")
    print(f"Total Time    : {observer.total_time:.3f} sec")
    print(f"Average Time  : {observer.average_time:.3f} sec")

    print("\nAgent Timeline")

    for agent in observer.agents:
        print(f" • {agent['name']:15} {agent['time']:.3f} sec")


def main():
    section("📧 MailLife - Multi-Agent AI Email Assistant")

    orchestrator = MailLifeOrchestrator()

    user_request = input("\nDescribe your email:\n\n")

    result = orchestrator.generate_email(user_request)

    if result["status"] == "failed":
        print("\n❌ Failed")
        print(result["message"])

        print("\nAnalysis:")
        print(result["analysis"])
        return

    observer = result["observer"]

    show_analysis(result["analysis"])

    show_draft(result["draft"])

    show_review(result["final"])

    show_observability(observer)


if __name__ == "__main__":
    main()