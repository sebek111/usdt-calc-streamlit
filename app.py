import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Калькулятор USDT",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS: фоновый цвет, скролл, скрытие заголовков Streamlit
custom_css = """
<style>
    header, footer {visibility: hidden;}
    .block-container {
        padding: 0;
        margin: 0;
        background-color: #0e0e0e;
    }
    html, body {
        height: 100%;
        margin: 0;
        padding: 0;
        overflow: auto;
        background-color: #0e0e0e;
    }
    iframe {
        border: none;
        height: 100vh;
        width: 100%;
        display: block;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Встраивание калькулятора
components.iframe(
    src="https://sebek111.github.io/btc-usdt-calc/",
    height=1400,  # больше, чем экран, чтобы сработал скролл
    scrolling=True
)
