import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("💵 Калькулятор себестоимости USDT (HTX)")

components.iframe(
    "https://sebek111.github.io/btc-usdt-calc/",  # ← встроенный HTML-калькулятор
    height=1200,
    width=1000,
    scrolling=True
)
