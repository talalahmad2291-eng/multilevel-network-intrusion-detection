import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import accuracy_score, classification_report

st.title("AI-NIDS CSV Prediction App")

st.write("Upload a testing CSV file. The app will predict normal/attack and attack type.")

# Load saved files
binary_model = joblib.load("binary_intrusion_model.pkl")
attack_model = joblib.load("attack_type_model.pkl")

binary_scaler = joblib.load("binary_scaler.pkl")
binary_ohe = joblib.load("binary_ohe.pkl")

attack_scaler = joblib.load("attack_scaler.pkl")
attack_ohe = joblib.load("attack_ohe.pkl")
attack_label_encoder = joblib.load("attack_label_encoder.pkl")

binary_columns = joblib.load("original_binary_columns.pkl")
attack_columns = joblib.load("original_attack_columns.pkl")

uploaded_file = st.file_uploader("Upload testing CSV file", type=["csv"])

def preprocess_for_model(df, model_columns, scaler, ohe):
    X = df.copy()

    for col in model_columns:
        if col not in X.columns:
            X[col] = 0

    X = X[model_columns]

    categorical_cols = X.select_dtypes(include=["object", "string"]).columns.tolist()
    numeric_cols = X.select_dtypes(exclude=["object", "string"]).columns.tolist()

    X[numeric_cols] = X[numeric_cols].fillna(0)

    for col in categorical_cols:
        X[col] = X[col].fillna("-").astype(str)

    X_num_scaled = scaler.transform(X[numeric_cols])
    X_cat_encoded = ohe.transform(X[categorical_cols])

    X_processed = np.hstack((X_num_scaled, X_cat_encoded))

    return X_processed

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df.columns = df.columns.str.strip().str.lower()

    st.subheader("Uploaded Data Preview")
    st.dataframe(df.head())

    binary_input = preprocess_for_model(
        df,
        binary_columns,
        binary_scaler,
        binary_ohe
    )

    binary_predictions = binary_model.predict(binary_input)

    result_df = df.copy()
    result_df["predicted_label"] = binary_predictions
    result_df["predicted_status"] = result_df["predicted_label"].map({
        0: "Normal",
        1: "Attack"
    })

    attack_rows = result_df[result_df["predicted_label"] == 1].copy()

    if len(attack_rows) > 0:
        attack_input = preprocess_for_model(
            attack_rows,
            attack_columns,
            attack_scaler,
            attack_ohe
        )

        attack_predictions = attack_model.predict(attack_input)
        attack_names = attack_label_encoder.inverse_transform(attack_predictions)

        result_df["predicted_attack_cat"] = "Normal"
        result_df.loc[attack_rows.index, "predicted_attack_cat"] = attack_names
    else:
        result_df["predicted_attack_cat"] = "Normal"

    st.subheader("Prediction Results")
    st.dataframe(result_df)

    if "label" in df.columns:
        st.subheader("Binary Model Accuracy")

        true_labels = df["label"]
        pred_labels = result_df["predicted_label"]

        st.write("Accuracy:", accuracy_score(true_labels, pred_labels))

        report = classification_report(
            true_labels,
            pred_labels,
            zero_division=0,
            output_dict=True
        )

        st.dataframe(pd.DataFrame(report).transpose())

    if "attack_cat" in df.columns:
        st.subheader("Attack Type True vs Predicted")

        compare_df = result_df[["attack_cat", "predicted_attack_cat"]].copy()
        compare_df.columns = ["True Attack Type", "Predicted Attack Type"]

        st.dataframe(compare_df)

    csv_output = result_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Prediction Results",
        data=csv_output,
        file_name="nids_predictions.csv",
        mime="text/csv"
    )