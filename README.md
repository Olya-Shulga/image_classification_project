# Image Classification Project

## Описание проекта

Проект разработан в рамках практической работы №10 по дисциплине:

**«Методы глубокого обучения для работы с большими пространственными данными»**

Цель проекта — сравнение различных моделей глубокого обучения для задачи классификации изображений и развертывание модели в виде API-сервиса с графическим пользовательским интерфейсом.

В рамках работы были:
- подготовлены данные для обучения;
- реализованы и обучены несколько моделей классификации изображений;
- проведено сравнение моделей по метрикам качества;
- выбрана лучшая модель;
- разработан backend API на FastAPI;
- разработан frontend интерфейс на Streamlit;
- подготовлена структура проекта для развертывания.

---

# Используемые технологии

## Основные библиотеки

- Python 3.10+
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Backend

- FastAPI
- Uvicorn

## Frontend

- Streamlit

---

# Структура проекта

```text
image_classification_project/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── models/
│   ├── best_model_final.keras
│   ├── class_names.json
│   └── model_meta.json
│
├── results/
│   ├── model_comparison.csv
│   ├── metrics_comparison.png
│   ├── inference_time.png
│   ├── confusion_matrices.png
│   └── best_model_metrics.json
│
├── requirements.txt
└── README.md
```

---

# Описание моделей

В проекте были реализованы и сравнены несколько архитектур:

1. Полносвязная нейронная сеть (Dense Neural Network)
2. Простая сверточная нейронная сеть (CNN)
3. MobileNetV2 (Transfer Learning)

Сравнение выполнялось по следующим метрикам:
- Accuracy
- Precision
- Recall
- F1-score
- Время инференса

---

# Лучшая модель

По результатам сравнения лучшей моделью была выбрана:

```text
best_model_final.keras
```

Модель сохранена в папке:

```text
models/
```

---

# Backend (FastAPI)

Backend реализован с использованием FastAPI.

## Возможности API

- загрузка изображения;
- предсказание класса изображения;
- возврат confidence score.

## Основной endpoint

### POST /predict

Принимает изображение и возвращает результат классификации.

Пример ответа:

```json
{
  "class": "cats",
  "confidence": 0.9875
}
```

---

# Frontend (Streamlit)

Frontend реализован с использованием Streamlit.

Возможности интерфейса:
- загрузка изображения;
- отображение изображения;
- отправка изображения в API;
- отображение результата классификации.

---

# Установка проекта

# Создание виртуального окружения

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Установка зависимостей

```bash
pip install -r requirements.txt
```

---

# Запуск backend

Перейдите в папку backend:

```bash
cd backend
```

Запустите сервер:

```bash
uvicorn main:app --reload
```

После запуска API будет доступен по адресу:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```
![Backend Screenshot](https://raw.githubusercontent.com/Olya-Shulga/image_classification_project/main/backend.jpg)
---

# Запуск frontend

Откройте новый терминал.

Перейдите в папку frontend:

```bash
cd frontend
```

Запустите Streamlit:

```bash
streamlit run app.py
```

После запуска интерфейс откроется в браузере автоматически.

![Frontend Screenshot](https://raw.githubusercontent.com/Olya-Shulga/image_classification_project/main/frontend.jpg)

---

# Пример работы

1. Пользователь загружает изображение.
2. Frontend отправляет изображение в FastAPI.
3. Backend обрабатывает изображение.
4. Модель выполняет классификацию.
5. Результат отображается в интерфейсе.

---

# Результаты экспериментов

Результаты сравнения моделей находятся в папке:

```text
results/
```

Содержимое:
- confusion matrices;
![confusion matrices Screenshot](https://github.com/Olya-Shulga/image_classification_project/blob/main/results/confusion_matrices.png)
- графики метрик;
![metrics_comparison Screenshot](https://github.com/Olya-Shulga/image_classification_project/blob/main/results/metrics_comparison.png)
- время инференса;
![inference_time Screenshot](https://github.com/Olya-Shulga/image_classification_project/blob/main/results/inference_time.png)
- CSV-таблица сравнения моделей.

---

# Возможные улучшения проекта

- использование более сложных архитектур;
- добавление Docker-контейнеризации;
- развертывание в облаке;
- поддержка пакетной обработки изображений;
- добавление базы данных;
- реализация аутентификации пользователей.

---

# Автор

Ольга Шульга

Магистратура:
«Анализ больших пространственных данных»

---

# Лицензия

Проект создан в учебных целях.
