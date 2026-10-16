import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load the dataset
df = pd.read_csv("smart_home_energy.csv")

# 2. Extract useful numerical features from Time
# Converts "14:30" into the integer hour 14
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

# 3. Feature Selection
# We choose our input features (X) and our target variable to predict (y)
feature_cols = ['Outdoor_Temp', 'Household_Size', 'Hour', 'Appliance_Type', 'Season']
X = df[feature_cols]
y = df['Energy_kWh']

# 4. Convert text categories into numerical format (One-Hot Encoding)
X = pd.get_dummies(X, columns=['Appliance_Type', 'Season'], drop_first=True)

# 5. Split data into Training set (80%) and Testing set (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Initialize and train the Machine Learning Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 7. Evaluate the model performance on unseen test data
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("--- AI Model Training Complete ---")
print(f"Mean Absolute Error (MAE): {mae:.2f} kWh")
print(f"Model Accuracy Score (R2 Score): {r2:.2%}")
