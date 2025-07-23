import streamlit as st
import numpy as np
import joblib
st.title("Employee Salary Prediction")
st.divider()
st.write("With this app, you can predict salery of an employee")

years =st.number_input("Years of Experience", min_value=0, max_value=50, value=1,)


jobrate = st.number_input("Job Rating", min_value=0.0, max_value=5.0, value=0.0, step=1.0)
x=[years, jobrate]
st.divider()

predict= st.button("Predict Salary")
st.divider()
if predict:
        model = joblib.load("linearmodel.pkl")
        st.balloons()  # fixed typo
        x1 = np.array([x])
        predction = model.predict(x1)
        st.write(f"Salary Prediction is {predction}")

else:
        st.write("Press the button to predict salary")
