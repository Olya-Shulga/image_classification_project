import streamlit as st
import requests
from PIL import Image

API_URL = "https://image-classification-project-nl0r.onrender.com/predict"

st.set_page_config(
    page_title="Классификация изображений",
    layout="centered"
)

st.title("Классификация изображений")
st.markdown("---")

uploaded_file = st.file_uploader(
    "Выберите изображение...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.image(image, caption="Загруженное изображение", use_column_width=True)

    with col2:
        st.subheader("Прогноз нейросети:")

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        try:
            response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                result = response.json()

                # Если backend возвращает вероятности всех классов
                if "probabilities" in result:
                    probabilities = result["probabilities"]

                    for cls, val in probabilities.items():
                        val = float(val)

                        col_text, col_val = st.columns([2, 1])
                        col_text.markdown(f"**{cls.capitalize()}**")
                        col_val.markdown(f"*{val * 100:.1f}%*")
                        st.progress(val)

                st.markdown("---")
                st.success(
                    f"Это **{result['class'].upper()}** "
                    f"с уверенностью {result['confidence'] * 100:.1f}%"
                )

            else:
                st.error("Ошибка при обращении к backend API")

        except Exception as e:
            st.error(f"Ошибка соединения с backend: {e}")