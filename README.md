AI Internship Challenge – SMS Spam Classification
This project is a simple ** text classification model ** to detect SPAM messages.  
It uses ** SMS Spam Collection Dataset ** (UCI Depot) and uses machine learning techniques to classify messages like ** him (legal) ** or ** spam **.

,,

## 📂 dataset
- Source: [UCI Machine Learning Repository - SMS Spam Collection] (https://archive.ici.edu/ml/datasets/smspamspam+++++++++  
- The dataset has 5 574 SMS messages marked as ** him ** (legal) or ** spam **.  
- Store the data set file 'SMSSSPAMCOLLACTION' in the data/`` folder for this project.

,,

## ⚙ Features
-Pre-treatment: Remove lowercase letters, stop words (through TF-IDF vector).
- Model: ** Bole Bayes ** (Baseline) and option for testing the logistics region.
- Evaluation: accuracy, accurate, recall, F1 score.
- Visualization: Confusion matrix for classification results.
- predicting scripts to test custom messages ('prediction. PY`).

,,

## 🚀 How to Run


### 1. Install dependencies
```bash
pip install -r requirements.txt
