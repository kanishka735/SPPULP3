# Practical 2: Email Spam Classification

## Objective
Classify incoming emails into two categories (Spam vs. Ham/Normal) using supervised classification algorithms. Evaluate and compare the performance of K-Nearest Neighbors (KNN), Naive Bayes (MultinomialNB), and Support Vector Machine (LinearSVC).

---

## Algorithms Implemented
1. **Multinomial Naive Bayes (`MultinomialNB`)**: Probabilistic classifier based on Bayes' theorem under feature independence assumptions.
2. **K-Nearest Neighbors (`KNeighborsClassifier`)**: Non-parametric instance-based classifier.
3. **Support Vector Machine (`LinearSVC`)**: Maximum-margin linear hyperplane classifier.

---

## Pre-processing & Feature Extraction
- **TF-IDF Vectorization** (`TfidfVectorizer`): Converts text email bodies into numerical word importance vectors while scaling down globally frequent words.
- **Pipeline Architecture**: Uses `make_pipeline` to cleanly encapsulate vectorization and model inference.

---

## Evaluation Metrics
- Confusion Matrix
- Accuracy Score
- Precision, Recall, and F1-Score (via `classification_report`)

---

## Files in this Directory
- `email.py` / `02_email.py`: Complete Python classification script.
- `email.ipynb` / `02_email_spam_classification.ipynb`: Jupyter Notebook with step-by-step visualization.
- `emails.csv`: Email dataset with word frequency / text tokens and spam labels.

---

## How to Run

### Command Line
```bash
cd Group-B-Machine-Learning/02-Email-Spam-Classification
python email.py
```

### Jupyter Notebook
```bash
jupyter notebook email.ipynb
```
