
# Experiment 3: Bank Customer Churn Prediction
# Using MLP Neural Network Classifier
#
# Problem Statement:
# Predict whether a bank customer will leave the bank
# or continue using its services.
#
# 0 = Customer will stay (Not Churn)
# 1 = Customer will leave (Churn)


# --------------------------------------------------
# Step 1: Import Required Libraries
# --------------------------------------------------

import os
import numpy as np
import pandas as pd

# Used to split dataset into training and testing
from sklearn.model_selection import train_test_split

# Used to apply preprocessing to different columns
from sklearn.compose import ColumnTransformer

# Used to convert categorical data into numerical values
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Used to combine multiple preprocessing steps
from sklearn.pipeline import make_pipeline

# Used to handle missing values
from sklearn.impute import SimpleImputer

# Import MLP Neural Network classifier
from sklearn.neural_network import MLPClassifier

# Import model evaluation metrics
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# --------------------------------------------------
# Step 2: Load or Generate Dataset
# --------------------------------------------------

# Theory:
# Dataset contains information about bank customers.
# Features include Age, Balance, Tenure, Products,
# Geography and Gender.
#
# Target variable:
# Exited = 1 means customer left the bank.
# Exited = 0 means customer stayed.

if os.path.exists("bank.csv"):

    # Load actual bank dataset
    df = pd.read_csv("bank.csv")

    # Identify target column
    target = "Exited" if "Exited" in df.columns else "churn"

    # Separate input and output
    y = df[target]
    X = df.drop(columns=[target])

    print("Bank dataset loaded successfully!")

else:

    # Generate synthetic bank customer dataset
    rng = np.random.default_rng(3)
    n = 800

    # Generate numerical features
    age = rng.integers(18, 80, n)
    balance = rng.uniform(0, 200000, n)
    tenure = rng.integers(0, 11, n)
    products = rng.integers(1, 5, n)

    # Generate categorical features
    geography = rng.choice(
        ["France", "Spain", "Germany"], n
    )

    gender = rng.choice(
        ["Female", "Male"], n
    )

    # THEORY: LOGISTIC FUNCTION
    #
    # First calculate logit value.
    #
    # logit = -3 + 0.035*(age-40)
    #         + 0.000012*balance
    #         + 0.45*(products==1)
    #         + 0.7*(geography=="Germany")
    #
    # Convert logit into probability using sigmoid.
    #
    # Sigmoid Formula:
    #
    # P = 1 / (1 + e^(-logit))
    #
    # The probability determines the likelihood
    # of a customer leaving the bank.

    logit = (
        -3
        + 0.035 * (age - 40)
        + 0.000012 * balance
        + 0.45 * (products == 1)
        + 0.7 * (geography == "Germany")
    )

    # Calculate churn probability
    prob = 1 / (1 + np.exp(-logit))

    # Generate binary target variable
    y = (rng.random(n) < prob).astype(int)

    # Create customer DataFrame
    X = pd.DataFrame({
        "Age": age,
        "Balance": balance,
        "Tenure": tenure,
        "NumOfProducts": products,
        "Geography": geography,
        "Gender": gender
    })

    print("Synthetic bank dataset generated!")


# --------------------------------------------------
# Step 3: Data Preprocessing
# --------------------------------------------------

# Theory:
# Data preprocessing prepares raw data for machine learning.
#
# Numerical features:
# Age, Balance, Tenure, NumOfProducts
#
# Categorical features:
# Geography, Gender
#
# Numerical missing values are filled using median.
# Categorical missing values are filled using mode.
#
# StandardScaler Formula:
#
# Z = (X - Mean) / Standard Deviation
#
# It brings numerical features to a comparable scale.
#
# One-Hot Encoding:
# Converts categorical values into binary numerical columns.

# Identify numerical columns
numeric = X.select_dtypes(
    include=np.number
).columns.tolist()

# Identify categorical columns
categorical = [
    c for c in X.columns if c not in numeric
]

print("\nNumerical Columns:", numeric)
print("Categorical Columns:", categorical)


# --------------------------------------------------
# Step 4: Create Preprocessing Pipeline
# --------------------------------------------------

# Numerical preprocessing:
# 1. Fill missing values using median.
# 2. Standardize numerical features.

# Categorical preprocessing:
# 1. Fill missing values using most frequent value.
# 2. Convert categories into numerical values.

prep = ColumnTransformer([
    (
        "num",
        make_pipeline(
            SimpleImputer(strategy="median"),
            StandardScaler()
        ),
        numeric
    ),

    (
        "cat",
        make_pipeline(
            SimpleImputer(strategy="most_frequent"),
            OneHotEncoder(handle_unknown="ignore")
        ),
        categorical
    )
])


# --------------------------------------------------
# Step 5: Split Dataset into Training and Testing
# --------------------------------------------------

# Theory:
# Training data is used to train the neural network.
# Testing data is used to evaluate model performance.
#
# 80% = Training data
# 20% = Testing data
#
# stratify=y maintains the class distribution
# in both training and testing datasets.

Xtr, Xte, ytr, yte = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(Xtr))
print("Testing Samples:", len(Xte))


# --------------------------------------------------
# Step 6: Implement MLP Neural Network Classifier
# --------------------------------------------------

# THEORY: MULTI-LAYER PERCEPTRON (MLP)
#
# MLP is a supervised Artificial Neural Network.
# It consists of three main types of layers:
#
# 1. Input Layer
# 2. Hidden Layer
# 3. Output Layer
#
# Each neuron receives input, applies weights and bias,
# and passes the result through an activation function.
#
# Neuron Formula:
#
# Z = W.X + b
#
# A = f(Z)
#
# Where:
# W = Weights
# X = Input values
# b = Bias
# f = Activation function
#
# ReLU Activation Function:
#
# f(x) = max(0, x)
#
# It converts negative values into zero
# and keeps positive values unchanged.
#
# Sigmoid Activation Function:
#
# f(x) = 1 / (1 + e^(-x))
#
# It converts output into a probability between 0 and 1.
#
# Backpropagation:
# It calculates errors and updates weights
# to improve prediction accuracy.
#
# Learning process:
# 1. Forward Propagation
# 2. Calculate Error
# 3. Backpropagation
# 4. Update Weights
#
# Here:
# hidden_layer_sizes=(32,16) means two hidden layers.
# First hidden layer contains 32 neurons.
# Second hidden layer contains 16 neurons.
# max_iter=600 means maximum 600 training iterations.
# early_stopping=True stops training if validation
# performance does not improve sufficiently.


# --------------------------------------------------
# Step 7: Create MLP Model
# --------------------------------------------------

model = make_pipeline(
    prep,
    MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        max_iter=600,
        random_state=42,
        early_stopping=True
    )
)


# --------------------------------------------------
# Step 8: Train the Neural Network
# --------------------------------------------------

# fit() trains the MLP model using training data.
# It learns weights and biases from customer information.

model.fit(Xtr, ytr)


# --------------------------------------------------
# Step 9: Make Predictions
# --------------------------------------------------

# predict() predicts whether customers will
# stay or leave the bank.

pred = model.predict(Xte)


# --------------------------------------------------
# Step 10: Model Evaluation
# --------------------------------------------------

# THEORY 1: ACCURACY
#
# Accuracy = (TP + TN) / (TP + TN + FP + FN)
#
# It measures the percentage of correct predictions.

accuracy = accuracy_score(yte, pred)


# THEORY 2: CONFUSION MATRIX
#
# TP = True Positive
# TN = True Negative
# FP = False Positive
# FN = False Negative
#
# It compares actual and predicted customer classes.

cm = confusion_matrix(yte, pred)


# THEORY 3: PRECISION
#
# Precision = TP / (TP + FP)
#
# It measures how many predicted churn customers
# actually left the bank.


# THEORY 4: RECALL
#
# Recall = TP / (TP + FN)
#
# It measures how many actual churn customers
# were correctly identified.


# THEORY 5: F1-SCORE
#
# F1 = 2 * (Precision * Recall) /
#      (Precision + Recall)
#
# It balances Precision and Recall.


# Display evaluation results
print("\n----- MLP MODEL RESULTS -----")

print("Accuracy:", round(accuracy, 3))

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(
    yte,
    pred,
    zero_division=0
))


# --------------------------------------------------
# Step 11: Final Result
# --------------------------------------------------

print("\nBank Customer Churn Prediction Completed Successfully!")

print("MLP Neural Network Model trained and evaluated.")
