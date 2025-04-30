import streamlit as st
import streamlit.components.v1 as components

# Настройка страницы
st.set_page_config(
    page_title="Калькулятор USDT",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Скрытие заголовков и отступов через CSS
hide_streamlit_style = """
    <style>
        header, footer {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            background-color: #0e0e0e;
        }
        iframe {
            display: block;
            margin: 0 auto;
            border: none;
            width: 100%;
            max-width: 600px;
            height: 100vh;
            max-height: 100vh;
        }
        html, body {
            background-color: #0e0e0e !important;
            overflow: hidden;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Встраивание калькулятора
components.iframe(
    "https://sebek111.github.io/btc-usdt-calc/",
    height=800,
    scrolling=False
)
