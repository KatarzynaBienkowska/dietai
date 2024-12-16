import streamlit as st
import base64
from ai import vision

def process_image(image):
    image_data = base64.b64encode(image.getvalue()).decode("utf-8")
    st.markdown(vision.generate_response(image_data))

st.title("Identify your food")
st.write("Take a picture of your food and get nutritional info about it.")

col1, col2 = st.columns([1, 2])

with col1:
    enable_camera = st.checkbox("Enable camera")
    picture = st.camera_input("Take a picture", disabled=not enable_camera)

    hr_css = "flex-grow: 1; border: 1px solid #ccc; margin: 0 10px;"
    st.markdown(f"""
        <div style="display: flex; align-items: center; margin: 20px 0;">
            <hr style="{hr_css}">
            <span style="white-space: nowrap; font-weight: bold;">or</span>
            <hr style="{hr_css}">
        </div>
    """, unsafe_allow_html=True)

    uploaded_picture = st.file_uploader(label="Upload picture", type=["png", "jpg"])

with col2:
    image = picture or uploaded_picture
    if image:
        with st.spinner("Identifying food..."):
            process_image(image)