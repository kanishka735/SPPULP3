
# Experiment 2: Email Spam Detection using Machine Learning
#
# Problem Statement:
# Classify emails into two categories using Binary Classification:
# 1. Normal State - Not Spam (Ham)
# 2. Abnormal State - Spam
#
# Implement the following algorithms:
# 1. Naive Bayes
# 2. K-Nearest Neighbors (KNN)
# 3. Support Vector Machine (SVM)
#
# Evaluate the models using Accuracy, Precision, Recall and F1-score.


# --------------------------------------------------
# Step 1: Import Required Libraries
# --------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# Converts text into numerical values using TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
# Combines preprocessing and machine learning steps
from sklearn.pipeline import make_pipeline
# Import classification algorithms
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC

# Import evaluation metrics
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    confusion_matrix
)

# --------------------------------------------------
# Step 2: Load or Generate Dataset
# --------------------------------------------------

# Theory:
# A dataset contains email messages and their labels.
# Each email is classified as:
# Ham  = Normal email
# Spam = Unwanted or promotional email
#
# CSV file should contain two columns:
# text  = Email message
# label = ham or spam

try:

    # Load email dataset from CSV file
    df = pd.read_csv("emails.csv")

    # Extract email messages and labels
    X = df["text"].astype(str)
    y = df["label"].astype(str).str.strip().str.lower()

    print("Dataset loaded successfully!")

except FileNotFoundError:

    # Generate sample dataset if CSV is unavailable

    X = pd.Series([
        "Congratulations you won a free prize click now",
        "Meeting moved to 3 pm tomorrow",
        "Claim your cash reward now",
        "Please review the attached project report",
        "You have won lottery send bank details",
        "Can we discuss the assignment today",
        "Urgent claim your free gift",
        "The lecture starts at ten"
    ] * 20)

    y = pd.Series([
        "spam", "ham", "spam", "ham",
        "spam", "ham", "spam", "ham"
    ] * 20)

    print("Sample dataset generated!")


# --------------------------------------------------
# Step 3: Data Preprocessing
# --------------------------------------------------

# Theory:
# Data preprocessing is the process of cleaning
# and preparing raw data before applying ML algorithms.
#
# Steps:
# 1. Remove missing values.
# 2. Convert text into string format.
# 3. Remove unnecessary spaces.
# 4. Convert labels into lowercase.
# 5. Keep only valid categories.

# Create a clean DataFrame
data = pd.DataFrame({
    "text": X,
    "label": y
})

# Remove rows containing missing values
data = data.dropna()

# Convert email messages into lowercase
data["text"] = data["text"].str.lower()

# Remove extra spaces
data["text"] = data["text"].str.strip()

# Convert labels into lowercase
data["label"] = data["label"].str.strip().str.lower()

# Keep only ham and spam categories
data = data[data["label"].isin(["ham", "spam"])]

# Remove empty email messages
data = data[data["text"] != ""]

# Remove duplicate messages only for real datasets
# Repeated sample messages are retained for demonstration.

print("\nPreprocessed Dataset:")
print(data.head())

print("\nTotal Emails:", len(data))

# Separate input and output
X = data["text"]
y = data["label"]


# --------------------------------------------------
# Step 4: Text Vectorization using TF-IDF
# --------------------------------------------------

# Theory:
# Machine learning algorithms cannot directly understand
# text messages. Therefore, text is converted into numbers.
#
# TF-IDF stands for Term Frequency - Inverse Document Frequency.
#
# Formula:
#
# TF-IDF(t,d) = TF(t,d) * IDF(t)
#
# IDF(t) = log(N / DF(t))
#
# Where:
# TF = Frequency of a word in a document
# N  = Total number of documents
# DF = Number of documents containing the word
#
# TF-IDF gives higher importance to meaningful words
# and lower importance to very common words.

# TfidfVectorizer converts text into numerical features.
# It will be fitted separately on training data in each pipeline.


# --------------------------------------------------
# Step 5: Split Dataset into Training and Testing
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))


# --------------------------------------------------
# Step 6: Naive Bayes Classification
# --------------------------------------------------

# THEORY: NAIVE BAYES
#
# Naive Bayes is a supervised classification algorithm.
# It is based on Bayes' Theorem.
#
# It predicts the category of an email using
# the probability of words appearing in that email.
#
# Bayes Theorem Formula:
#
# P(A|B) = P(B|A) * P(A) / P(B)
#
# Where:
# P(A|B) = Posterior Probability
# P(B|A) = Likelihood
# P(A)   = Prior Probability
# P(B)   = Evidence
#
# Multinomial Naive Bayes is suitable for text
# classification problems.
#
# It assumes that features are conditionally independent
# given the class.

# Create Naive Bayes model
naive_bayes = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)


# --------------------------------------------------
# Step 7: K-Nearest Neighbors (KNN) Classification
# --------------------------------------------------

# THEORY: KNN
#
# KNN is a supervised machine learning algorithm.
# It classifies a new email based on its K nearest
# neighboring training examples.
#
# Euclidean Distance Formula:
#
# d = sqrt((x1-y1)^2 + (x2-y2)^2 + ... )
#
# Where:
# x and y are feature vectors of two data points.
#
# The majority class among the K nearest neighbors
# determines the final predicted class.
#
# Here, K = 3.
#
# KNN is a distance-based classification algorithm.

# Create KNN model
knn = make_pipeline(
    TfidfVectorizer(),
    KNeighborsClassifier(n_neighbors=3)
)


# --------------------------------------------------
# Step 8: Support Vector Machine (SVM) Classification
# --------------------------------------------------

# THEORY: SVM
#
# Support Vector Machine is a supervised learning algorithm.
# It separates data into different classes using
# an optimal hyperplane.
#
# Hyperplane Formula:
#
# w.x + b = 0
#
# Where:
# w = Weight vector
# x = Input features
# b = Bias
#
# SVM tries to find the maximum margin between classes.
#
# Support Vectors are the data points closest to
# the separating hyperplane.
#
# LinearSVC is used for text classification because
# it works efficiently with high-dimensional text features.

# Create SVM model
svm = make_pipeline(
    TfidfVectorizer(),
    LinearSVC()
)


# --------------------------------------------------
# Step 9: Train and Evaluate All Models
# --------------------------------------------------

# Create dictionary containing all three models

models = {
    "Naive Bayes": naive_bayes,
    "K-Nearest Neighbors": knn,
    "Support Vector Machine": svm
}

# Train and test each model one by one

for name, model in models.items():

    # Train the model using training data
    model.fit(X_train, y_train)

    # Predict email categories using test data
    pred = model.predict(X_test)


    # --------------------------------------------------
    # Step 10: Model Evaluation
    # --------------------------------------------------

    # THEORY 1: ACCURACY
    #
    # Accuracy = (TP + TN) / (TP + TN + FP + FN)
    #
    # It measures the percentage of correctly
    # classified emails.

    accuracy = accuracy_score(y_test, pred)


    # THEORY 2: CONFUSION MATRIX
    #
    # It shows correct and incorrect predictions.
    #
    # TP = True Positive
    # TN = True Negative
    # FP = False Positive
    # FN = False Negative
    #
    # Here, Spam is treated as the positive class.

    cm = confusion_matrix(
        y_test,
        pred,
        labels=["spam", "ham"]
    )


    # THEORY 3: PRECISION
    #
    # Precision = TP / (TP + FP)
    #
    # It measures how many emails predicted as spam
    # are actually spam.

    # THEORY 4: RECALL
    #
    # Recall = TP / (TP + FN)
    #
    # It measures how many actual spam emails
    # are correctly identified.

    # THEORY 5: F1-SCORE
    #
    # F1 = 2 * (Precision * Recall) /
    #      (Precision + Recall)
    #
    # It is the harmonic mean of Precision and Recall.

    # Display results
    print("\n--------------------------------")
    print("Model:", name)
    print("--------------------------------")

    print("Accuracy:", round(accuracy * 100, 2), "%")

    print("\nConfusion Matrix:")
    print(cm)

    print("\nClassification Report:")

    print(classification_report(
        y_test,
        pred,
        zero_division=0
    ))


# --------------------------------------------------
# Step 11: Final Result
# --------------------------------------------------

print("\nEmail Spam Detection Completed Successfully!")

print("Naive Bayes, KNN and SVM models")
print("have been trained and evaluated.")
