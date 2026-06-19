# Student Participation Eligibility Prediction System

## Overview

The Student Participation Eligibility Prediction System is a Machine Learning based solution developed to automate the identification of student participation eligibility using attendance and engagement data.

The system processes attendance records, performs feature engineering, trains multiple machine learning models, evaluates their performance, and automatically generates eligibility reports for students.

The project helps educational institutions and training organizations reduce manual effort in evaluating participant eligibility and improves the efficiency of report generation.

---

## Problem Statement

Managing and evaluating student participation manually becomes difficult when dealing with large datasets. Traditional methods require significant administrative effort and are prone to errors.

This project automates participation eligibility prediction using Machine Learning techniques and generates reports automatically.

---

## Objectives

* Automate participation eligibility prediction.
* Analyze student participation patterns.
* Generate eligibility reports automatically.
* Train and evaluate Machine Learning models.
* Improve decision-making efficiency.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook

---

## Feature Engineering

The following features are generated:

* Total Sessions
* Sessions Attended
* Average Attendance Minutes
* Attendance Percentage
* Attendance Standard Deviation
* Consistency Score
* Domain Participation Count
* Engagement Score

---

## Machine Learning Models

The following classification algorithms are used:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

---

## Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Generated Outputs

### Reports

* eligible_students.csv
* ineligible_students.csv
* final_eligibility_report.csv
* model_evaluation_report.csv
* student_predictions.csv

### Summary Files

* best_model_summary.txt
* classification_report.txt
* project_execution_log.txt

### Models

* logistic_regression.pkl
* decision_tree.pkl
* random_forest.pkl

### Visualizations

* attendance_distribution.png
* eligible_vs_ineligible.png
* college_wise_participation.png
* attendance_scatter_plot.png
* confusion_matrix.png

---

## Project Structure

Student_Participation_Eligibility_System/

├── data/

├── notebooks/

├── src/

├── models/

├── outputs/

├── visualizations/

├── requirements.txt

├── README.md

└── main.py

---

## How To Run

Install dependencies:

pip install -r requirements.txt

Run the complete project:

python main.py

---

## Output

The system automatically:

* Generates participation eligibility predictions.
* Creates eligible student reports.
* Creates ineligible student reports.
* Produces evaluation reports.
* Saves execution logs.
* Generates visualizations.

---

## Future Enhancements

* Web Dashboard
* Streamlit Interface
* Real-Time Attendance Integration
* Certificate Generation
* Cloud Deployment
* Student Performance Analytics

