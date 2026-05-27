import streamlit as st
import requests

API_URL = "https://image-classification-project-nl0r.onrender.com/predict"

st.title("Классификация изображений")

uploaded_file = st.file_uploader(
    "Загрузите изображение",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    st.image(uploaded_file)

    if st.button("Предсказать"):
        files = {
            "file": uploaded_file.getvalue()
        }

        response = requests.post(API_URL, files=files)

        result = response.json()

        st.success(
            f"Класс: {result['class']} "
            f"(confidence={result['confidence']:.4f})"
        )