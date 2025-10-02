AI Internship Challenge – SMS Spam Classification
This project is a simple ** text classification model ** to detect SPAM messages.  
It uses ** SMS Spam Collection Dataset ** (UCI Depot) and uses machine learning techniques to classify messages like ** him (legal) ** or ** spam **.

,,

## 📂 dataset
- Source: [UCI Machine Learning Repository - SMS Spam Collection] (https://archive.ics.uci.edu/dataset/228/sms+spam+collection)  
- The dataset has 5 574 SMS messages marked as ** him ** (legal) or ** spam **.  
,,

## ⚙ Features
-Pre-treatment: Remove lowercase letters, stop words (through TF-IDF vector).
- Model: ** Bole Bayes ** (Baseline) and option for testing the logistics region.
- Evaluation: accuracy, accurate, recall, F1 score.
- Visualization: Confusion matrix for classification results.
- predicting scripts to test custom messages ('prediction. PY`).

,,

## 🚀 How to Run
### 1. Clone the Repository  
Download the project from GitHub:  
```bash
git clone https://github.com/yourusername/ai-text-classification.git
cd ai-text-classification

Install depencies
pip install -r requirements.txt

Train and Evaluate the Model
python main.ipynb

Make predictions
python predict.py
```bash
pip install -r requirements.txt
