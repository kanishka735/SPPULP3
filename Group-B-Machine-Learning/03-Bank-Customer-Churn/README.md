# Practical 3: Bank Customer Churn Prediction (Neural Networks)

## Objective
Predict whether a bank customer will churn (leave the bank) or stay based on demographic and banking parameters using an Artificial Neural Network (Multilayer Perceptron - MLP).

---

## Theory & Architecture
Customer churn prediction is a binary classification task:
- `0`: Customer stays (No Churn)
- `1`: Customer exits (Churn)

### Neural Network Model: `MLPClassifier`
- **Input Layer**: Scaled numeric features (CreditScore, Age, Tenure, Balance, NumOfProducts, EstimatedSalary) and one-hot encoded categorical variables (Geography, Gender).
- **Hidden Layers**: Fully connected layers with non-linear activation (`relu`).
- **Optimization**: Adam optimizer with backpropagation for weight updates.
- **Preprocessing Pipeline**: `ColumnTransformer` combining `OneHotEncoder` and `StandardScaler`.

---

## Files in this Directory
- `bank.py` / `03_bank.py`: Python neural network script.
- `bank.ipynb` / `03_bank_customer_churn_neural_network.ipynb`: Interactive Jupyter Notebook.
- `bank.csv`: Churn modeling dataset containing customer profiles and churn status (`Exited`).

> [!NOTE]
> The script includes an automated synthetic-data generator if `bank.csv` is absent, ensuring zero-error execution. The authentic `bank.csv` dataset is provided in this directory.

---

## How to Run

### Command Line
```bash
cd Group-B-Machine-Learning/03-Bank-Customer-Churn
python bank.py
```

### Jupyter Notebook
```bash
jupyter notebook bank.ipynb
```
