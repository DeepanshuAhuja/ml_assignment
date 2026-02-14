import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

st.title("Income Classification App for BITS")
st.write("Machine Learning Classification Models Deployment")

# Upload CSV
uploaded_file = st.file_uploader("Upload the csv file", type=["csv"])

model_option = st.selectbox(
    "Select the Model",
    ["Logistic Regression", "Decision Tree", "KNN",
     "Naive Bayes", "Random Forest", "XGBoost"]
)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)


    name = model_option.replace(" ", "_")
    model = joblib.load(f"model/{name}.pkl")

    X = data.drop("income", axis=1)
    y = data["income"]

    predictions = model.predict(X)

    st.subheader("Evaluation Metrics")
    report = classification_report(y, predictions, output_dict=True)
    st.write(pd.DataFrame(report).transpose())

    st.subheader("Confusion Matrix")
    cm = confusion_matrix(y, predictions)
    st.write(cm)