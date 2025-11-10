"""
main.py - Pipeline for the HealthCare Solutions Data Science project
Author: Daniel Sanjines Lozano
Description: Load simulated dataset, perform EDA, preprocess, train a RandomForest model to predict 30-day readmission,
and save outputs (figures and a simple model report).

Requirements:
  pip install pandas numpy scikit-learn matplotlib seaborn joblib
Usage:
  python main.py
Outputs:
  - figures in the "outputs" folder
  - model report printed and saved to model_report.txt
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score
import matplotlib.pyplot as plt
import joblib

DATA_PATH = "dataset_healthcare_simulated.csv"

def load_data(path=DATA_PATH):
    df = pd.read_csv(path, parse_dates=['admission_date','discharge_date'])
    return df

def preprocess(df):
    # simple preprocessing: fillna, create features
    df = df.copy()
    # duration (should match length_of_stay but compute from dates as example)
    df['computed_los'] = (df['discharge_date'] - df['admission_date']).dt.days.clip(lower=1)
    # encode categorical
    df = pd.get_dummies(df, columns=['sex','admission_type','hospital_unit'], drop_first=True)
    # drop identifiers and dates
    df = df.drop(['patient_id','admission_date','discharge_date'], axis=1)
    return df

def train_model(df):
    X = df.drop('readmission_30d', axis=1)
    y = df['readmission_30d']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    clf = RandomForestClassifier(n_estimators=200, random_state=42, class_weight='balanced')
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    probs = clf.predict_proba(X_test)[:,1]
    report = classification_report(y_test, preds)
    acc = accuracy_score(y_test, preds)
    try:
        auc = roc_auc_score(y_test, probs)
    except Exception:
        auc = None
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/model_report.txt", "w") as f:
        f.write("Accuracy: " + str(acc) + "\n")
        f.write("AUC: " + str(auc) + "\n\n")
        f.write(report)
    joblib.dump(clf, "outputs/random_forest_readmission.joblib")
    print("Model training finished. Accuracy:", acc, "AUC:", auc)
    return clf, X_test, y_test

def save_basic_plots(df):
    os.makedirs("outputs", exist_ok=True)
    # histogram of age
    plt.figure()
    df['age'].hist(bins=20)
    plt.title("Distribution of Age")
    plt.savefig("outputs/age_hist.png")
    plt.close()
    # LOS vs Satisfaction scatter
    plt.figure()
    plt.scatter(df['length_of_stay'], df['satisfaction_score'], alpha=0.4)
    plt.title("Length of Stay vs Satisfaction Score")
    plt.xlabel("Length of Stay (days)")
    plt.ylabel("Satisfaction Score")
    plt.savefig("outputs/los_vs_satisfaction.png")
    plt.close()

if __name__ == "__main__":
    df = load_data(DATA_PATH)
    save_basic_plots(df)
    df_proc = preprocess(df)
    clf, X_test, y_test = train_model(df_proc)

