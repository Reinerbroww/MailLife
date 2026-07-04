import streamlit as st
import time
from textwrap import dedent


class AgentTimeline:

    def __init__(self):
        self.placeholder = st.empty()

    # =====================================================
    # UPDATE TIMELINE
    # =====================================================

    def update(
        self,
        brain=False,
        writer=False,
        reviewer=False
    ):

        def icon(done):
            return "✅" if done else "⏳"

        html = dedent(f"""
<div style="
background:white;
padding:20px;
border-radius:18px;
box-shadow:0 6px 18px rgba(0,0,0,.08);
margin-top:15px;
margin-bottom:25px;
border:1px solid #e5e7eb;
">

<h3 style="margin-top:0;">
🤖 Multi-Agent Workflow
</h3>

<hr style="margin:12px 0;">

<p style="font-size:16px;">
{icon(brain)} <b>MailBrain</b><br>
<span style="color:#6b7280;">
Analyze user request
</span>
</p>

<p style="font-size:16px;">
{icon(writer)} <b>MailWriter</b><br>
<span style="color:#6b7280;">
Generate professional email
</span>
</p>

<p style="font-size:16px;">
{icon(reviewer)} <b>MailReviewer</b><br>
<span style="color:#6b7280;">
Review and improve draft
</span>
</p>

</div>
""")

        self.placeholder.markdown(
            html,
            unsafe_allow_html=True
        )

    # =====================================================
    # MAILBRAIN
    # =====================================================

    def brain(self):

        self.update(
            brain=False,
            writer=False,
            reviewer=False
        )

        time.sleep(0.4)

        self.update(
            brain=True,
            writer=False,
            reviewer=False
        )

    # =====================================================
    # MAILWRITER
    # =====================================================

    def writer(self):

        self.update(
            brain=True,
            writer=False,
            reviewer=False
        )

        time.sleep(0.4)

        self.update(
            brain=True,
            writer=True,
            reviewer=False
        )

    # =====================================================
    # REVIEWER
    # =====================================================

    def reviewer(self):

        self.update(
            brain=True,
            writer=True,
            reviewer=False
        )

        time.sleep(0.4)

        self.update(
            brain=True,
            writer=True,
            reviewer=True
        )

    # =====================================================
    # FINISH
    # =====================================================

    def finish(self):

        self.update(
            brain=True,
            writer=True,
            reviewer=True
        )