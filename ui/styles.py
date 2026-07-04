import streamlit as st
from textwrap import dedent


def load_css():

    st.markdown(
        dedent("""
<style>

/* =======================================================
GENERAL
======================================================= */

html, body, [class*="css"]{
    font-family:"Segoe UI",sans-serif;
}

/* Background */

.stApp{

    background:
    linear-gradient(
        135deg,
        #f4f7ff,
        #eef3ff
    );

}

/* =======================================================
HERO CARD
======================================================= */

.hero-card{

    padding:38px;

    border-radius:22px;

    background:
    linear-gradient(
        135deg,
        #3b82f6,
        #2563eb
    );

    color:white;

    text-align:center;

    box-shadow:
    0 12px 35px rgba(0,0,0,.15);

    margin-bottom:30px;

}

.hero-title{

    font-size:42px;

    font-weight:700;

}

.hero-subtitle{

    font-size:18px;

    opacity:.95;

    margin-top:12px;

}

/* =======================================================
BUTTON
======================================================= */

.stButton>button{

    width:100%;

    border:none;

    border-radius:12px;

    padding:14px;

    font-size:17px;

    font-weight:bold;

    background:
    linear-gradient(
        135deg,
        #2563eb,
        #1d4ed8
    );

    color:white;

    transition:.25s;

}

.stButton>button:hover{

    transform:translateY(-2px);

    box-shadow:
    0 10px 25px rgba(37,99,235,.35);

}

/* =======================================================
TEXT AREA
======================================================= */

textarea{

    border-radius:14px !important;

}

/* =======================================================
INPUT
======================================================= */

input{

    border-radius:10px !important;

}

/* =======================================================
METRIC
======================================================= */

[data-testid="metric-container"]{

    background:white;

    border-radius:18px;

    padding:18px;

    border:1px solid #e5e7eb;

    box-shadow:
    0 8px 20px rgba(0,0,0,.05);

}

/* =======================================================
TABS
======================================================= */

.stTabs [role="tab"]{

    border-radius:10px;

    padding:10px 18px;

}

.stTabs [aria-selected="true"]{

    background:#2563eb;

    color:white;

}

/* =======================================================
DOWNLOAD BUTTON
======================================================= */

.stDownloadButton>button{

    width:100%;

    border-radius:12px;

    font-weight:bold;

}

/* =======================================================
SUCCESS
======================================================= */

.stSuccess{

    border-radius:12px;

}

/* =======================================================
INFO
======================================================= */

.stInfo{

    border-radius:12px;

}

/* =======================================================
WARNING
======================================================= */

.stWarning{

    border-radius:12px;

}

/* =======================================================
ERROR
======================================================= */

.stError{

    border-radius:12px;

}

/* =======================================================
SIDEBAR
======================================================= */

[data-testid="stSidebar"]{

    background:#0f172a;

}

[data-testid="stSidebar"] *{

    color:white;

}

/* =======================================================
SCROLLBAR
======================================================= */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#2563eb;

    border-radius:20px;

}

::-webkit-scrollbar-track{

    background:#edf2ff;

}

/* =======================================================
FOOTER
======================================================= */

footer{

    visibility:hidden;

}

</style>
        """),
        unsafe_allow_html=True
    )