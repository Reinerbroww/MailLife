import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            # 📧 MailLife

            **AI-Powered Multi-Agent Email Assistant**

            ---
            """
        )

        st.markdown("## 🤖 AI Agents")

        st.success("🧠 MailBrain")
        st.success("✍️ MailWriter")
        st.success("🔍 MailReviewer")

        st.divider()

        st.markdown("## ⚙️ Settings")

        model = st.selectbox(
            "Gemini Model",
            [
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite"
            ],
            index=0,
            key="sidebar_model"
        )

        language = st.selectbox(
            "Output Language",
            [
                "Auto",
                "English",
                "Indonesia"
            ],
            index=0,
            key="sidebar_language"
        )

        tone = st.selectbox(
            "Preferred Tone",
            [
                "Auto",
                "Professional",
                "Formal",
                "Friendly",
                "Casual"
            ],
            index=0,
            key="sidebar_tone"
        )

        st.divider()

        developer = st.toggle(
            "🛠 Developer Mode",
            value=False,
            key="developer_mode"
        )

        st.divider()

        st.markdown("## 📈 Project Info")

        st.metric(
            "Agents",
            "3"
        )

        st.metric(
            "Version",
            "v2.0"
        )

        st.metric(
            "Backend",
            "Gemini"
        )

        st.divider()

        st.markdown(
            """
            ### Features

            Multi-Agent Workflow

            Email Planner

            AI Email Writer

            AI Reviewer

            Observability

            Download TXT

            Download JSON
            """
        )

        st.divider()

        st.caption("Made with ❤️ using Python, Streamlit & Gemini")

    return {
        "model": model,
        "language": language,
        "tone": tone,
        "developer_mode": developer
    }