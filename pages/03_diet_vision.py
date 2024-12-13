import streamlit as st

st.title("Identify your food")
st.write("Take a picture of your food and get nutritional info about it.")

enable_camera = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable_camera)

if picture:
    st.image(picture)