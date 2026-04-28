# 🏦 Early Warning System (EWS)

## 📌 Описание проекта
Данный проект представляет собой систему раннего предупреждения проблемных кредитов.

Цель: выявить клиентов с ухудшающимся кредитным поведением до дефолта.

---

## 📊 Данные
Использован открытый датасет Credit Risk Dataset (Kaggle).

Размер:
- 32 000+ записей
- 12 исходных признаков

---

## ⚙️ Feature Engineering
Добавлены новые признаки:
- debt_to_income
- interest_pressure
- credit_history_risk

---

## 🧠 Target (EWS логика)

Клиенты делятся на:
- stable — стабильный
- risk_increasing — риск растет
- high_risk — высокий риск

---

## 🤖 Модель
Random Forest Classifier

---

## 📈 Метрики
- Accuracy: ~0.90
- F1-score: ~0.90

---

## ⚠️ Важный момент
На этапе разработки была обнаружена проблема data leakage (использование loan_status в признаках), которая была исправлена.

---

## 🖥 Streamlit приложение

Функционал:
- ввод данных клиента
- расчет риска
- вывод результата (Stable / Risk Increasing / High Risk)

---

## 🚀 Запуск проекта

```bash
pip install -r requirements.txt
streamlit run app.py