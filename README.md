# Problem Statement
Predict whether a person earns more than 50K annually based on demographic features.

# Dataset Description

UCI Adult Income Dataset
Instances: 48,842
Features: 14
Target: Income(>50K / <=50K)

# Models Used 
1.) Accuracy \
2.) Precision \
3.) Recall \
4.) F1 Score \
5.) AUC\
6.) MCC 

# Comparison Table

| ML Model Name       | Accuracy | AUC    | Precision | Recall | F1 Score | MCC    |
| ------------------- | -------- | ------ | --------- | ------ | -------- | ------ |
| Logistic Regression | 0.8230   | 0.8598 | 0.7442    | 0.4601 | 0.5687   | 0.4863 |
| Decision Tree       | 0.8104   | 0.7511 | 0.6250    | 0.6307 | 0.6278   | 0.5006 |
| KNN                 | 0.8251   | 0.8588 | 0.6761    | 0.5961 | 0.6336   | 0.5211 |
| Naive Bayes         | 0.7984   | 0.8595 | 0.7099    | 0.3471 | 0.4662   | 0.3946 |
| Random Forest       | 0.8560   | 0.9078 | 0.7509    | 0.6464 | 0.6948   | 0.6041 |
| XGBoost             | 0.8684   | 0.9261 | 0.7730    | 0.6810 | 0.7241   | 0.6404 |

# Observations

## Logistic Regression
* Achieved good Accuracy (82.3%) and strong AUC (0.8598).
* However, Recall (0.4601) is relatively low, meaning it misses many positive cases.
* Moderate MCC (0.4863) shows balanced but limited performance.
* Works reasonably well but struggles with complex non-linear patterns.

## Decision Tree
* Slightly lower Accuracy (81.04%) compared to Logistic Regression.
* Balanced Precision (0.6250) and Recall (0.6307).
* Lower AUC (0.7511) suggests weaker probability discrimination.
* Likely prone to overfitting due to tree-based structure.

## K-Nearest Neighbors (KNN)
* Good Accuracy (82.51%) and strong AUC (0.8588).
* More balanced Recall (0.5961) compared to Logistic Regression.
* MCC (0.5211) higher than previous models, indicating better overall classification strength.
* Performs well but computationally expensive for large datasets.

## Naive Bayes
* Lowest Accuracy (79.84%) among models.
* Very low Recall (0.3471) → misses many positive cases.
* Despite high AUC (0.8595), low F1 (0.4662) and MCC (0.3946).
* Performance affected due to strong independence assumption between features.

## Random Forest (Ensemble Model)
* Significant improvement in all metrics.
* High Accuracy (85.60%) and strong AUC (0.9078).
* Good balance between Precision (0.7509) and Recall (0.6464).
* MCC (0.6041) shows strong overall correlation between predictions and true labels.
* Handles non-linearity and feature interactions effectively.

## XGBoost (Ensemble Model)
* Best performing model overall.
* Highest Accuracy (86.84%) and AUC (0.9261).
* Highest F1 Score (0.7241) and MCC (0.6404).
* Excellent balance between Precision and Recall.
* Boosting approach reduces bias and variance effectively.



