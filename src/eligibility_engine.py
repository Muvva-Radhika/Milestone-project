import pandas as pd
import joblib
import os

# ==================================================
# PROJECT ROOT DIRECTORY
# ==================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# ==================================================
# FILE PATHS
# ==================================================

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "Student_Attendance_Summary.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "random_forest.pkl"
)

CERTIFIED_PATH = os.path.join(
    BASE_DIR,
    "outputs",
    "eligible_students.csv"
)

INELIGIBLE_PATH = os.path.join(
    BASE_DIR,
    "outputs",
    "ineligible_students.csv"
)

REPORT_PATH = os.path.join(
    BASE_DIR,
    "outputs",
    "final_eligibility_report.csv"
)

# ==================================================
# LOAD DATASET
# ==================================================

print("Loading Student Attendance Dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully!")
print(f"Total Students : {len(df)}")

# ==================================================
# LOAD TRAINED MODEL
# ==================================================

print("\nLoading Random Forest Model...")

model = joblib.load(MODEL_PATH)

print("Random Forest Model Loaded Successfully!")

# ==================================================
# SELECT FEATURES
# ==================================================

X = df[
[
    'Total_Sessions',
    'Sessions_Attended',
    'Average_Attendance_Minutes',
    'Consistency_Score',
    'Domain_Participation_Count',
    'Engagement_Score'
]
]

# ==================================================
# PREDICT CERTIFICATION ELIGIBILITY
# ==================================================

print("\nPredicting Eligibility...")

df['Predicted_Eligible'] = model.predict(X)

print("Prediction Completed!")

PREDICTION_PATH = os.path.join(
    BASE_DIR,
    "outputs",
    "student_predictions.csv"
)

df.to_csv(
    PREDICTION_PATH,
    index=False
)

# ==================================================
# SEPARATE ELIGIBLE STUDENTS
# ==================================================

eligible_students = df[
    df['Predicted_Eligible'] == 1
]

# ==================================================
# SEPARATE INELIGIBLE STUDENTS
# ==================================================

ineligible_students = df[
    df['Predicted_Eligible'] == 0
]

# ==================================================
# SAVE ELIGIBLE STUDENTS
# ==================================================

eligible_students.to_csv(
    CERTIFIED_PATH,
    index=False
)

# ==================================================
# SAVE INELIGIBLE STUDENTS
# ==================================================

ineligible_students.to_csv(
    INELIGIBLE_PATH,
    index=False
)

# ==================================================
# CREATE FINAL REPORT
# ==================================================

total_students = len(df)

eligible_count = len(eligible_students)

ineligible_count = len(ineligible_students)

eligibility_rate = round(
    (eligible_count / total_students) * 100,
    2
)

final_report = pd.DataFrame({
    "Total_Students": [total_students],
    "Eligible_Students": [eligible_count],
    "Ineligible_Students": [ineligible_count],
    "Eligibility_Rate (%)": [eligibility_rate]
})

# ==================================================
# SAVE REPORT
# ==================================================

final_report.to_csv(
    REPORT_PATH,
    index=False
)

# ==================================================
# DISPLAY RESULTS
# ==================================================

print("\n========== FINAL REPORT ==========")

print(final_report)

print("\nFiles Generated Successfully:")

print(f"\n{CERTIFIED_PATH}")
print(f"{INELIGIBLE_PATH}")
print(f"{REPORT_PATH}")

print("\nML-Based Eligibility Process Completed!")