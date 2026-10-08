\# 🎭 Анализ тональности отзывов



NLP-приложение для определения тональности русскоязычных отзывов.

Использует предобученную модель RuBERT от Hugging Face.



\## Что делает

Пользователь вводит отзыв → модель определяет, позитивный он или негативный,

и показывает уверенность в процентах.



\## Стек

\- Python 3

\- Transformers (Hugging Face)

\- Streamlit



\## Как запустить локально

\\`\\`\\`bash

pip install -r requirements.txt

streamlit run app.py

\\`\\`\\`



\## Модель

\[blanchefort/rubert-base-cased-sentiment](https://huggingface.co/blanchefort/rubert-base-cased-sentiment)



\## Что я узнал

\- Работа с предобученными NLP-моделями через Hugging Face

\- Построение веб-интерфейса на Streamlit

\- Обработка edge-cases (пустой ввод, длинные тексты)

