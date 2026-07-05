import streamlit as st

from core.orchestrator import MailLifeOrchestrator

from ui.styles import load_css
from ui.sidebar import render_sidebar
from ui.timeline import AgentTimeline

from ui.components import (
    render_hero,
    render_input,
    render_summary,
    render_analysis,
    render_draft,
    render_review,
    render_observer,
    render_download
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="MailLife",
    page_icon="📧",
    layout="wide"
)

load_css()

settings = render_sidebar()

render_hero()

st.divider()

# =====================================================
# ORCHESTRATOR
# =====================================================

orchestrator = MailLifeOrchestrator()

# =====================================================
# INPUT
# =====================================================

user_request = render_input()

generate = st.button(
    "🚀 Generate Email",
    use_container_width=True
)
if generate:

    if not user_request.strip():

        st.warning(
            "Please describe your email first."
        )

        st.stop()

    timeline = AgentTimeline()

    progress = st.progress(0)

    timeline.update()

    progress.progress(15)

    with st.spinner("🧠 MailBrain is thinking..."):

        try:

            result = orchestrator.generate_email(
                user_request
            )

        except RuntimeError as e:

            st.error(
                "🚦 Gemini API is currently busy.\n\n"
                "Please wait a moment and try again."
            )

            with st.expander("Technical Details"):

                st.code(str(e))

            st.stop()

    progress.progress(100)

    timeline.finish()

    if result["status"] == "failed":

        st.error(result["message"])

        st.stop()

    observer = result["observer"]

    analysis = result["analysis"]

    draft = result["draft"]

    review = result["final"]

    st.success("✅ Email generated successfully!")

    render_summary(
        observer,
        review
    )
    tab1, tab2, tab3, tab4 = st.tabs(

        [

            "🧠 Analysis",

            "✍ Draft",

            "🔍 Review",

            "📊 Observability"

        ]

    )

    with tab1:

        render_analysis(
            analysis
        )

    with tab2:

        render_draft(
            draft
        )

    with tab3:

        render_review(
            review
        )

    with tab4:

        render_observer(
            observer
        )

    st.divider()

    render_download(

        review,

        analysis

    )