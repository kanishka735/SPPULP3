# Practical 1: Uber Fare Prediction

## Objective
Predict the price of an Uber ride given pickup/drop-off coordinates and timestamps using regression models. Perform end-to-end data pre-processing, outlier detection, correlation analysis, and regression model evaluation.

---

## Tasks & Workflow
1. **Pre-processing**: Handle missing values, parse pickup datetime into features (hour, day, month, year, day-of-week), compute Haversine travel distance.
2. **Outlier Detection**: Filter invalid coordinates, extreme passenger counts, negative or unreasonable fares.
3. **Correlation Analysis**: Check feature correlation matrix with fare amount.
4. **Model Implementation**:
   - Linear Regression (Baseline)
   - Random Forest Regressor
5. **Evaluation Metrics**: Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Coefficient of Determination ($R^2$ Score).

---

## Files in this Directory
- `uber.py` / `01_uber.py`: Complete Python implementation script.
- `Uber.ipynb` / `ML_1_Uber.ipynb`: Interactive Jupyter Notebook with cell-by-cell execution and outputs.
- `uber.csv`: Real-world Uber ride dataset containing coordinates, timestamps, passenger count, and fare amounts.

> [!NOTE]
> The Python script includes a synthetic-data fallback in case `uber.csv` is not found, but the real `uber.csv` is included in this directory.

---

## How to Run

### Command Line
```bash
cd Group-B-Machine-Learning/01-Uber-Fare-Prediction
python uber.py
```

### Jupyter Notebook
```bash
jupyter notebook Uber.ipynb
```
