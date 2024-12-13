import streamlit as st

st.set_page_config(
   page_title="DietAI",
   page_icon="🍉",
   layout="centered"
)

st.logo("images/logo.png", size="large")

pages = [
    st.Page("pages/01_chat.py", title="💬Chat"),
    st.Page("pages/02_meal_planner.py", title="🥗Meal Planner"),
    st.Page("pages/03_diet_vision.py", title="👁️Diet Vision")
]

pg = st.navigation(pages)
pg.run()