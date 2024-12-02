# Credit Card Fraud Detection

## Overview

This project focuses on detecting fraudulent credit card transactions using machine learning techniques. Fraud detection is a critical problem faced by financial institutions, as fraudulent transactions can result in significant financial losses. The project utilizes a dataset of anonymized credit card transactions and applies various machine learning models to classify transactions as fraudulent or legitimate.

## Features

- **Data Preprocessing**: 
  - Handled class imbalance using techniques like SMOTE.
  - Scaled features using StandardScaler for optimal model performance.
- **Exploratory Data Analysis (EDA)**: 
  - Visualized class distribution and analyzed correlations among features.
  - Investigated patterns in fraudulent vs. legitimate transactions.
- **Model Building**: 
  - Implemented Logistic Regression, Random Forest, Gradient Boosting, and other models.
  - Tuned hyperparameters for optimal performance.
- **Evaluation Metrics**: 
  - Used metrics like Accuracy, Precision, Recall, F1-Score, and ROC-AUC to evaluate models.
  - Focused on minimizing false negatives to reduce undetected fraud.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook Credit_Card_Fraud_Detection.ipynb
   ```

## Dataset

The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). It consists of:
- 284,807 transactions
- 31 features, including anonymized PCA components and labels (1 for fraud, 0 for legitimate)

## Key Insights

1. Fraudulent transactions make up only **0.17%** of the dataset, highlighting the extreme class imbalance.
2. PCA components (V1 to V28) are used to protect sensitive information while preserving patterns.
3. Feature scaling and class balancing techniques significantly improved model performance.

## Future Work

- Implement deep learning models like RNNs and Autoencoders for better anomaly detection.
- Develop a real-time fraud detection system.
- Integrate explainability tools like SHAP or LIME to interpret model predictions.
