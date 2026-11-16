
# Experiment 1: Uber Fare Prediction using Machine Learning

# Problem Statement:
# Predict the price of the Uber ride from a given pickup point
# to the agreed drop-off location.
#
# Tasks:
# 1. Pre-process the dataset.
# 2. Identify outliers.
# 3. Check the correlation.
# 4. Implement Linear Regression and Random Forest Regression.
# 5. Evaluate models using R2, RMSE, MSE, etc.


# --------------------------------------------------
# Step 1: Import Required Libraries
# --------------------------------------------------

import os
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


# --------------------------------------------------
# Step 2: Load Dataset
# --------------------------------------------------

# Load uber.csv if available.
# Otherwise, generate a synthetic dataset.

path = "uber.csv"

if os.path.exists(path):
    df = pd.read_csv(path)
    print("Dataset loaded successfully!")

else:
    # Generate synthetic data
    rng = np.random.default_rng(7)
    n = 1000

    # Generate random pickup coordinates
    plon = rng.uniform(-74.05, -73.75, n)
    plat = rng.uniform(40.60, 40.90, n)

    # Generate random drop-off coordinates
    dlon = rng.uniform(-74.05, -73.75, n)
    dlat = rng.uniform(40.60, 40.90, n)

    # Calculate approximate distance
    # Formula:
    # Distance = sqrt((x1-x2)^2 + (y1-y2)^2) * 70

    dist = np.sqrt((plon-dlon)**2 + (plat-dlat)**2) * 70

    # Create DataFrame
    df = pd.DataFrame({
        "pickup_longitude": plon,
        "pickup_latitude": plat,
        "dropoff_longitude": dlon,
        "dropoff_latitude": dlat,
        "passenger_count": rng.integers(1, 6, n),

        # Synthetic fare formula:
        # Fare = Base Fare + (Rate * Distance) + Random Noise

        "fare_amount": 3 + 2.2*dist + rng.normal(0, 2, n)
    })

    print("Synthetic dataset generated!")


# --------------------------------------------------
# Step 3: Data Pre-processing
# --------------------------------------------------

# Select input features
features = [
    "pickup_longitude",
    "pickup_latitude",
    "dropoff_longitude",
    "dropoff_latitude",
    "passenger_count"
]

# Select required columns
df = df[features + ["fare_amount"]].copy()

# Convert values into numeric format
for col in features + ["fare_amount"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Replace infinite values with NaN
df = df.replace([np.inf, -np.inf], np.nan)

# Remove rows with missing fare values
df = df.dropna(subset=["fare_amount"])

# Remove invalid fare and passenger values
df = df[df["fare_amount"] > 0]
df = df[df["passenger_count"] > 0]

# SimpleImputer will handle missing input feature values later.

print("\nPreprocessed Dataset:")
print(df.head())
print("Dataset Shape:", df.shape)


# --------------------------------------------------
# Step 4: Outlier Detection using IQR Method
# --------------------------------------------------

# Theory:
# Outliers are unusually high or low values in a dataset.
# IQR stands for Interquartile Range.

# Formula:
# IQR = Q3 - Q1
#
# Lower Limit = Q1 - 1.5 * IQR
# Upper Limit = Q3 + 1.5 * IQR
#
# Q1 = First Quartile (25%)
# Q3 = Third Quartile (75%)
#
# Values below Lower Limit or above Upper Limit
# are considered outliers.

# Calculate Q1 and Q3
Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate lower and upper limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[
    (df["fare_amount"] < lower_limit) |
    (df["fare_amount"] > upper_limit)
]

print("\nNumber of Outliers:", len(outliers))

# Remove outliers
df = df[
    (df["fare_amount"] >= lower_limit) &
    (df["fare_amount"] <= upper_limit)
]

print("Dataset after removing outliers:", df.shape)


# --------------------------------------------------
# Step 5: Correlation Analysis
# --------------------------------------------------

# Theory:
# Correlation measures the relationship between two variables.
#
# Pearson Correlation Formula:
#
# r = Cov(X,Y) / (SD(X) * SD(Y))
#
# Where:
# r = Correlation coefficient
# Cov(X,Y) = Covariance between X and Y
# SD(X), SD(Y) = Standard deviations
#
# Range:
# +1 = Perfect positive correlation
#  0 = No linear correlation
# -1 = Perfect negative correlation

# Calculate correlation matrix
correlation = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(correlation.round(3))

# Check correlation with fare amount
print("\nCorrelation with Fare Amount:")
print(correlation["fare_amount"].sort_values(ascending=False))


# --------------------------------------------------
# Step 6: Split Dataset into Training and Testing
# --------------------------------------------------

# Theory:
# Training data is used to train the model.
# Testing data is used to evaluate model performance.
#
# Here, 80% data is used for training
# and 20% data is used for testing.

# X = Independent variables (input features)
# Y = Dependent variable (target fare)

X = df[features]
y = df["fare_amount"]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))


# --------------------------------------------------
# Step 7: Implement Linear Regression and Random Forest
# --------------------------------------------------

# THEORY 1: LINEAR REGRESSION
#
# Linear Regression is a supervised machine learning algorithm.
# It predicts a continuous numerical value.
#
# Formula:
# Y = b0 + b1X1 + b2X2 + ... + bnXn
#
# Where:
# Y  = Predicted fare
# b0 = Intercept
# b1, b2 = Coefficients
# X1, X2 = Input features
#
# It finds the best-fit line by minimizing
# the sum of squared errors.


# THEORY 2: RANDOM FOREST REGRESSION
#
# Random Forest is an ensemble learning algorithm.
# It creates multiple decision trees and combines
# their predictions to get the final output.
#
# Formula:
# Final Prediction = (T1 + T2 + ... + Tn) / n
#
# Where:
# T1, T2, ... Tn = Predictions of individual trees
# n = Total number of decision trees
#
# It generally provides better results for
# complex and non-linear relationships.


# Create both machine learning models
models = {

    # Linear Regression Pipeline
    "Linear Regression": make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler(),
        LinearRegression()
    ),

    # Random Forest Pipeline
    "Random Forest": make_pipeline(
        SimpleImputer(strategy="median"),
        RandomForestRegressor(
            n_estimators=150,
            random_state=42
        )
    )
}


# --------------------------------------------------
# Step 8: Model Training and Prediction
# --------------------------------------------------

# Train both models and predict fare amount

for name, model in models.items():

    # Train the model using training data
    model.fit(X_train, y_train)

    # Predict fare using testing data
    pred = model.predict(X_test)


    # --------------------------------------------------
    # Step 9: Model Evaluation
    # --------------------------------------------------

    # THEORY: MEAN SQUARED ERROR (MSE)
    #
    # MSE = (1/n) * Sum(actual - predicted)^2
    #
    # It calculates the average squared prediction error.
    # Lower MSE indicates better performance.

    mse = mean_squared_error(y_test, pred)


    # THEORY: ROOT MEAN SQUARED ERROR (RMSE)
    #
    # RMSE = sqrt(MSE)
    #
    # It measures the average prediction error
    # in the same unit as the fare amount.
    # Lower RMSE indicates better performance.

    rmse = np.sqrt(mse)


    # THEORY: R2 SCORE
    #
    # R2 = 1 - (SSres / SStot)
    #
    # SSres = Sum of squared residuals
    # SStot = Total sum of squares
    #
    # R2 = 1 means perfect prediction.
    # R2 = 0 means model explains no improvement
    # over predicting the mean.
    # Higher R2 generally indicates better performance.

    r2 = r2_score(y_test, pred)


    # Display evaluation results
    print("\nModel:", name)
    print("R2 Score:", round(r2, 3))
    print("RMSE:", round(rmse, 3))
    print("MSE:", round(mse, 3))


# --------------------------------------------------
# Step 10: Final Result
# --------------------------------------------------

print("\nUber Fare Prediction Completed Successfully!")
print("Both models trained and evaluated successfully.")
