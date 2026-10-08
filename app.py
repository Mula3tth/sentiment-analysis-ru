import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="blanchefort/rubert-base-cased-sentiment"
    )

st.set_page_config(page_title="Анализ тональности", page_icon="🎭")
st.title("🎭 Анализ тональности отзывов")
st.write("Введите отзыв — модель скажет, позитивный он или негативный.")

text = st.text_area(
    "Текст отзыва:",
    "Доставка быстрая, товар отличный, всем рекомендую!"
)

if st.button("Анализировать"):
    if not text.strip():
        st.warning("Введите текст отзыва.")
    else:
        with st.spinner("Модель думает..."):
            model = load_model()
            result = model(text)[0]
        
        label = "😊 Позитивный" if result["label"] == "POSITIVE" else "😞 Негативный"
        st.success(f"**{label}** — уверенность: {result['score']:.2%}")