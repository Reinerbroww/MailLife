import streamlit as st
from textwrap import dedent
import json


def render_hero():

    st.markdown(
        dedent("""
<div class="hero-card">

<div class="hero-title">
📧 MailLife
</div>

<div class="hero-subtitle">
AI-Powered Multi-Agent Email Assistant
</div>

<br>

Generate professional emails using a
Multi-Agent AI Architecture powered by
Google Gemini.

</div>
        """),
        unsafe_allow_html=True
    )

# ==========================================================
# INPUT
# ==========================================================

def render_input():
    return st.text_area(
        "Describe your email",
        placeholder="""
Example:

I want to send an email to my lecturer Mr. Marcellus because I have a fever tomorrow.
""",
        height=180,
        key="user_prompt"
    )


# ==========================================================
# SUMMARY CARDS
# ==========================================================

def render_summary(observer, review):
    quality = review.get("quality_score", 0)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🤖 Agents",
            "3"
        )

    with col2:
        st.metric(
            "⚡ AI Calls",
            observer.ai_calls
        )

    with col3:
        st.metric(
            "⭐ Quality",
            f"{quality}/100"
        )

    with col4:
        st.metric(
            "⏱ Total",
            f"{observer.total_time:.2f}s"
        )


# ==========================================================
# ANALYSIS
# ==========================================================

def render_analysis(analysis):
    st.subheader("🧠 MailBrain Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Intent",
            analysis.get("intent", "-")
        )

        st.metric(
            "Email Type",
            analysis.get("email_type", "-")
        )

        st.metric(
            "Tone",
            analysis.get("tone", "-")
        )

        st.metric(
            "Language",
            analysis.get("language", "-")
        )

    with col2:
        recipient = analysis.get("recipient", {})

        if isinstance(recipient, dict):
            recipient = recipient.get("role", "-")

        st.metric(
            "Recipient",
            recipient
        )

        st.metric(
            "Reason",
            analysis.get("reason", "-")
        )

        confidence = analysis.get("confidence", 0)

        st.metric(
            "Confidence",
            f"{confidence * 100:.0f}%"
        )


# ==========================================================
# DRAFT
# ==========================================================

def render_draft(draft):
    st.subheader("✍ Generated Draft")

    st.text_input(
        "Draft Subject",
        value=draft.get("subject", ""),
        disabled=True,
        key="draft_subject"
    )

    st.text_area(
        "Draft Body",
        value=draft.get("body", ""),
        height=350,
        disabled=True,
        key="draft_body"
    )


# ==========================================================
# REVIEW
# ==========================================================

def render_review(review):
    st.subheader("🔍 Final Email")

    st.text_input(
        "Final Subject",
        value=review.get("subject", ""),
        disabled=True,
        key="review_subject"
    )

    st.text_area(
        "Final Body",
        value=review.get("body", ""),
        height=320,
        disabled=True,
        key="review_body"
    )

    st.metric(
        "Quality Score",
        f"{review.get('quality_score', 0)}/100"
    )

    st.subheader("Changes")

    changes = review.get("changes", [])

    if changes:

        for item in changes:
            st.success(item)

    st.subheader("Suggestions")

    suggestions = review.get("suggestions", [])

    if suggestions:

        for item in suggestions:
            st.info(item)

    else:

        st.write("No suggestions.")


# ==========================================================
# OBSERVER
# ==========================================================

def render_observer(observer):
    st.subheader("📊 Observability")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "AI Calls",
            observer.ai_calls
        )

    with col2:
        st.metric(
            "Total Time",
            f"{observer.total_time:.2f}s"
        )

    with col3:
        st.metric(
            "Average",
            f"{observer.average_time:.2f}s"
        )

    st.divider()

    st.subheader("Agent Timeline")

    for agent in observer.agents:
        st.write(
            f"🤖 **{agent['name']}** — {agent['time']:.2f} sec"
        )


# ==========================================================
# DOWNLOAD
# ==========================================================

def render_download(review, analysis):
    st.subheader("📥 Export")

    email = f"""
Subject:
{review.get("subject", "")}

{review.get("body", "")}
"""

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "📄 Download TXT",
            data=email,
            file_name="MailLife_Email.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_txt"
        )

    with col2:
        st.download_button(
            "📦 Download JSON",
            data=json.dumps(
                analysis,
                indent=4
            ),
            file_name="analysis.json",
            mime="application/json",
            use_container_width=True,
            key="download_json"
        )