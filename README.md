<div align="center">

# 📧 MailLife

### AI-Powered Multi-Agent Email Assistant

Generate professional emails using an intelligent Multi-Agent AI workflow powered by Google Gemini.

<br>

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

---

*"Don't just generate emails. Let AI think before it writes."*

</div>

---

# 🚀 Overview

MailLife is an AI-powered email assistant built with a **Multi-Agent Architecture**.

Instead of asking one AI to generate an email directly, MailLife divides the task into multiple intelligent agents that collaborate to produce higher-quality results.

Each agent has a specific responsibility, making the generated email more accurate, professional, and reliable.

---

# ✨ Features

## 🧠 MailBrain

Analyze the user's request before writing.

✔ Detect user intent

✔ Identify recipient

✔ Understand email purpose

✔ Extract important information

✔ Determine language

✔ Determine writing tone

---

## ✍ MailWriter

Generate a complete professional email.

✔ Subject Generation

✔ Professional Formatting

✔ Natural Writing Style

✔ Context-aware Response

---

## 🔍 MailReviewer

Review and improve the generated email.

✔ Grammar Checking

✔ Professional Tone Enhancement

✔ Quality Score

✔ Suggested Improvements

---

## 📊 Observability

Monitor the AI workflow.

✔ Total AI Calls

✔ Execution Time

✔ Average Response Time

✔ Agent Timeline

---

## 🎨 Modern User Interface

Built with Streamlit.

✔ Responsive Layout

✔ Interactive Tabs

✔ Download TXT

✔ Download JSON

✔ Beautiful Dashboard

---

# 🏗 Multi-Agent Architecture

```text
                    User Request
                          │
                          ▼
                 🧠 MailBrain Agent
               Analyze & Understand
                          │
                          ▼
                ✍ MailWriter Agent
              Generate Email Draft
                          │
                          ▼
               🔍 MailReviewer Agent
            Improve & Score Quality
                          │
                          ▼
                 📊 Observability
                          │
                          ▼
                    Final Email
```

---

# 📂 Project Structure

```text
MailLife
│
├── agents/
│   ├── planner.py
│   ├── writer.py
│   └── reviewer.py
│
├── core/
│   ├── gemini_client.py
│   └── orchestrator.py
│
├── ui/
│   ├── components.py
│   ├── sidebar.py
│   ├── styles.py
│   └── timeline.py
│
├── utils/
│   ├── observer.py
│   └── validator.py
│
├── streamlit_app.py
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙ How It Works

```text
1. User describes the email.

        ↓

2. MailBrain analyzes the request.

        ↓

3. MailWriter creates the draft.

        ↓

4. MailReviewer improves the draft.

        ↓

5. Observability records every step.

        ↓

6. User downloads the final email.
```

---


# 🛠 Installation

Clone the repository

```bash
git clone https://github.com/Reinerbroww/MailLife.git
```

Go to the project folder

```bash
cd MailLife
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run streamlit_app.py
```

---

# 💡 Technologies

- Python
- Streamlit
- Google Gemini API
- python-dotenv

---

# 🎯 Future Improvements

- 📧 Gmail Integration
- 📄 PDF Export
- 🌍 Multi-language Translation
- 📚 Email History
- 🤖 More AI Agents
- ☁ Cloud Deployment

---

# 👨‍💻 Author

**Reiner Sakunab**

AI & Software Developer

---

<div align="center">

### ⭐ If you like this project, consider giving it a Star!

Made with ❤️ using Python & Google Gemini

</div>