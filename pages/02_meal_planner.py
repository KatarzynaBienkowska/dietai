import streamlit as st

st.title("Plan your meals")

with st.form("meal_planner"):
    st.write("For how many days would you like to plan your meals?")
    days = st.number_input("Days", min_value=1, max_value=7, value=1)

    st.write("Dietary restrictions")
    restrictions = st.multiselect(
        "Select all that apply",
        ["Vegetarian", "Vegan", "Gluten-free", "Dairy-free"]
    )

    st.write("Additional preferences")
    additional_info = st.text_area("Add your preferences here")

    st.form_submit_button("Generate meal plan", type="primary")
