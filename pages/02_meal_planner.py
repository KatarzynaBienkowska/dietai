import streamlit as st
from ai import planner

st.title("Plan your meals for the day")

col1, col2 = st.columns([1, 2])

with col1:
    with st.form("meal_planner"):
        st.write("What is your daily calorie goal?")
        calories = st.number_input("Calories", min_value=1200, max_value=5000, value=2000)

        st.write("Additional preferences")
        user_preferences = st.text_area("Add your preferences here")

        submit = st.form_submit_button("Generate meal plan", type="primary")

with col2:
    if submit:
        with st.spinner("Generating meal plan..."):
            meal_plan = planner.generate_response(calories, user_preferences)
            st.write(meal_plan)
