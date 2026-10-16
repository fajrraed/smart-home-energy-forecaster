import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# 1. Load data and rebuild the exact processing structure
df = pd.read_csv("smart_home_energy.csv")
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

X = df[['Outdoor_Temp', 'Household_Size', 'Hour', 'Appliance_Type', 'Season']]
y = df['Energy_kWh']

# One-hot encode categories to save reference structures
X_encoded = pd.get_dummies(X, columns=['Appliance_Type', 'Season'], drop_first=True)
model_columns = X_encoded.columns.tolist()

# 2. Train the production model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

print("--- Live Energy Forecaster Initialized ---")
print("Enter your environment details to estimate usage. Type 'exit' anytime to stop.\n")

while True:
    appliance = input("Appliance Type (Fridge, Oven, Heater, Air Conditioning, Lights): ").strip()
    if appliance.lower() == 'exit': break

    season = input("Current Season (Winter, Spring, Fall, Summer): ").strip()
    try:
        temp = float(input("Outdoor Temperature (in Celsius): "))
        size = int(input("Household Size (Number of people): "))
        hour = int(input("Hour of the Day (0-23): "))
    except ValueError:
        print("Invalid numerical inputs. Please try again.\n")
        continue

    # Create a single row matching our model configuration layout
    input_data = pd.DataFrame([{
        'Outdoor_Temp': temp,
        'Household_Size': size,
        'Hour': hour,
        'Appliance_Type': appliance,
        'Season': season
    }])

    # Process inputs identically to training data layout
    input_encoded = pd.get_dummies(input_data, columns=['Appliance_Type', 'Season'])
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Predict and print calculations
    predicted_kwh = model.predict(input_encoded)[0]
    print(f"\n>> Estimated Power Consumption: {predicted_kwh:.2f} kWh\n" + "-" * 40)
