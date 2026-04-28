import streamlit as st
import pandas as pd
import joblib

# загрузка модели
model = joblib.load("ews_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("🏦 Early Warning System")
st.write("Система раннего предупреждения проблемных кредитов")

# ввод данных
person_age = st.number_input("Возраст клиента", 18, 100, 30)
person_income = st.number_input("Доход клиента", 1000, 10000000, 60000)
person_emp_length = st.number_input("Стаж работы", 0.0, 50.0, 5.0)
loan_amnt = st.number_input("Сумма кредита", 500, 1000000, 10000)
loan_int_rate = st.number_input("Процентная ставка", 1.0, 40.0, 12.0)
loan_percent_income = st.number_input("Доля кредита от дохода", 0.0, 1.0, 0.2)
cb_person_cred_hist_length = st.number_input("Длина кредитной истории", 1, 50, 5)

person_home_ownership = st.selectbox("Тип жилья", ["RENT", "OWN", "MORTGAGE", "OTHER"])
loan_intent = st.selectbox("Цель кредита", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"])
loan_grade = st.selectbox("Кредитный grade", ["A", "B", "C", "D", "E", "F", "G"])
cb_person_default_on_file = st.selectbox("Был ли дефолт?", ["N", "Y"])

# расчеты
debt_to_income = loan_amnt / person_income
interest_pressure = loan_int_rate / 100
credit_history_risk = 1 / (cb_person_cred_hist_length + 1)

# собираем данные
input_data = pd.DataFrame([{
    "person_age": person_age,
    "person_income": person_income,
    "person_emp_length": person_emp_length,
    "loan_amnt": loan_amnt,
    "loan_int_rate": loan_int_rate,
    "loan_percent_income": loan_percent_income,
    "cb_person_cred_hist_length": cb_person_cred_hist_length,
    "debt_to_income": debt_to_income,
    "interest_pressure": interest_pressure,
    "credit_history_risk": credit_history_risk,
    "person_home_ownership": person_home_ownership,
    "loan_intent": loan_intent,
    "loan_grade": loan_grade,
    "cb_person_default_on_file": cb_person_default_on_file
}])

# кодирование
input_encoded = pd.get_dummies(input_data, drop_first=True)
input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

# кнопка
if st.button("Оценить риск"):
    prediction = model.predict(input_encoded)[0]

    if prediction == "high_risk":
        st.error("🔴 HIGH RISK — высокий риск")
    elif prediction == "risk_increasing":
        st.warning("🟡 RISK INCREASING — риск растет")
    else:
        st.success("🟢 STABLE — стабильный клиент")

    st.write("Расчетные признаки:")
    st.write(input_data[["debt_to_income", "interest_pressure", "credit_history_risk"]])



