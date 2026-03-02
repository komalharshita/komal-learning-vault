# ============================================================
# WEEK 3 - Predictive Modeling & Forecast Insights
# AI Powered Data Analyst Internship
# ============================================================

# ----------------------------
# 1. IMPORT LIBRARIES
# ----------------------------
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# ----------------------------
# 2. LOAD DATA
# ----------------------------
df = pd.read_excel("Cleaned_Preprocessed_Dataset_Week1.xlsx")

# Ensure Apply Date is datetime
df['Apply Date'] = pd.to_datetime(df['Apply Date'])

# ----------------------------
# ============================================================
# PART A: FORECASTING APPLICATION VOLUME
# ============================================================
# ----------------------------

# 3. AGGREGATE MONTHLY APPLICATION COUNTS
monthly_apps = df.groupby(['Apply_Year', 'Apply_Month']).size().reset_index(name='Application_Count')

# Create a time index
monthly_apps['Time_Index'] = range(len(monthly_apps))

# Features for forecasting
X_forecast = monthly_apps[['Time_Index', 'Apply_Month']]
y_forecast = monthly_apps['Application_Count']

# Train-Test Split (chronological)
split_index = int(len(monthly_apps) * 0.8)

X_train_f = X_forecast.iloc[:split_index]
X_test_f = X_forecast.iloc[split_index:]
y_train_f = y_forecast.iloc[:split_index]
y_test_f = y_forecast.iloc[split_index:]

# 4. BUILD RANDOM FOREST REGRESSOR
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X_train_f, y_train_f)

# 5. PREDICT
y_pred_f = rf_reg.predict(X_test_f)

# 6. EVALUATE FORECAST MODEL
mae = mean_absolute_error(y_test_f, y_pred_f)
rmse = np.sqrt(mean_squared_error(y_test_f, y_pred_f))
r2 = r2_score(y_test_f, y_pred_f)

print("Forecasting Model Evaluation:")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 3))

# 7. PLOT ACTUAL VS PREDICTED
plt.figure(figsize=(8,5))
plt.plot(y_test_f.values, label='Actual')
plt.plot(y_pred_f, label='Predicted')
plt.title("Actual vs Predicted Application Counts")
plt.legend()
plt.show()

plt.figure(figsize=(10,5))
plt.plot(y_test_f.values, label='Actual Applications')
plt.plot(y_pred_f, label='Predicted Applications')
plt.title("Actual vs Predicted Application Trends")
plt.xlabel("Time Index")
plt.ylabel("Application Count")
plt.legend()
plt.show()

residuals = y_test_f.values - y_pred_f



# ----------------------------
# ============================================================
# PART B: APPLICATION ACCEPTANCE PREDICTION
# ============================================================
# ----------------------------

# 8. SELECT FEATURES
features = [
    'Lead_Time_Days',
    'Opportunity_Popularity',
    'Opportunity_Duration_Days',
    'Days_Until_Opportunity_Start',
    'Age'
]

# Encode categorical variables
categorical_cols = ['Opportunity Category', 'Apply_Season', 'Country_Group', 'Gender']

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    features.append(col)

X_class = df[features]
y_class = df['Application_Accepted']

# 9. TRAIN-TEST SPLIT (Chronological)
df_sorted = df.sort_values(by='Apply Date')
split_index_class = int(len(df_sorted) * 0.8)

X_train_c = X_class.iloc[:split_index_class]
X_test_c = X_class.iloc[split_index_class:]
y_train_c = y_class.iloc[:split_index_class]
y_test_c = y_class.iloc[split_index_class:]

# 10. BUILD RANDOM FOREST CLASSIFIER
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train_c, y_train_c)

# 11. PREDICT
y_pred_c = rf_clf.predict(X_test_c)

# 12. EVALUATE CLASSIFICATION MODEL
accuracy = accuracy_score(y_test_c, y_pred_c)
precision = precision_score(y_test_c, y_pred_c)
recall = recall_score(y_test_c, y_pred_c)
f1 = f1_score(y_test_c, y_pred_c)

print("\nClassification Model Evaluation:")
print("Accuracy:", round(accuracy, 3))
print("Precision:", round(precision, 3))
print("Recall:", round(recall, 3))
print("F1 Score:", round(f1, 3))

# Confusion Matrix
cm = confusion_matrix(y_test_c, y_pred_c)
print("\nConfusion Matrix:\n", cm)

# ----------------------------
# 13. FEATURE IMPORTANCE
# ----------------------------
importances = pd.Series(rf_clf.feature_importances_, index=features)
importances = importances.sort_values(ascending=False)

print("\nTop Feature Importances:")
print(importances.head(10))

# Plot Feature Importance
plt.figure(figsize=(8,5))
importances.head(10).plot(kind='bar')
plt.title("Top 10 Feature Importances")
plt.show()

# ----------------------------
# 14. SAVE PREDICTIONS
# ----------------------------
forecast_output = pd.DataFrame({
    'Actual_Applications': y_test_f.values,
    'Predicted_Applications': y_pred_f
})

classification_output = pd.DataFrame({
    'Actual_Accepted': y_test_c.values,
    'Predicted_Accepted': y_pred_c
})

forecast_output.to_csv("forecast_predictions.csv", index=False)
classification_output.to_csv("classification_predictions.csv", index=False)

plt.figure(figsize=(8,5))
plt.scatter(range(len(residuals)), residuals)
plt.axhline(y=0, color='red')
plt.title("Forecast Residuals Over Time")
plt.xlabel("Time Index")
plt.ylabel("Residual (Actual - Predicted)")
plt.show()

# Predict probabilities
y_prob = rf_clf.predict_proba(X_test_c)[:,1]

temp_df = X_test_c.copy()
temp_df['Acceptance_Probability'] = y_prob

plt.figure(figsize=(8,5))
plt.scatter(temp_df['Lead_Time_Days'], temp_df['Acceptance_Probability'], alpha=0.3)
plt.title("Acceptance Probability vs Lead Time")
plt.xlabel("Lead_Time_Days")
plt.ylabel("Predicted Acceptance Probability")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(temp_df['Opportunity_Popularity'], temp_df['Acceptance_Probability'], alpha=0.3)
plt.title("Acceptance Probability vs Opportunity Popularity")
plt.xlabel("Opportunity_Popularity")
plt.ylabel("Predicted Acceptance Probability")
plt.show()

season_acceptance = df.groupby('Apply_Season')['Application_Accepted'].mean()

plt.figure(figsize=(8,5))
season_acceptance.plot(kind='bar')
plt.title("Acceptance Rate by Season")
plt.xlabel("Season")
plt.ylabel("Average Acceptance Rate")
plt.show()

import seaborn as sns

plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

importances = pd.Series(rf_clf.feature_importances_, index=features)
importances = importances.sort_values(ascending=False)

plt.figure(figsize=(8,5))
importances.head(10).plot(kind='bar')
plt.title("Top Feature Importances")
plt.ylabel("Importance Score")
plt.show()

print("\nPrediction files saved successfully.")