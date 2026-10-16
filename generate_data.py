import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# تثبيت الأرقام العشوائية لكي تظهر نفس النتائج دائماً
np.random.seed(42)

# إعداد المتغيرات الأساسية لتوليد 1000 سجل
records = 1000
start_date = datetime(2026, 1, 1)

# توليد التواريخ ومعرفات المنازل والأجهزة المتاحة
dates = [start_date + timedelta(hours=int(i)) for i in range(records)]
home_ids = [f"Home_{np.random.randint(1, 6)}" for _ in range(records)]
appliances = ["Fridge", "Oven", "Heater", "Air Conditioning", "Lights"]
chosen_appliances = np.random.choice(appliances, size=records)
household_sizes = np.random.choice([1, 2, 3, 4, 5], size=records)

# توليد درجات الحرارة الخارجية وتحديد الفصول بناءً عليها
temps = np.random.uniform(-5, 38, size=records)
seasons = []
for t in temps:
    if t < 10: seasons.append("Winter")
    elif t < 22: seasons.append("Spring")
    elif t < 30: seasons.append("Fall")
    else: seasons.append("Summer")

# توليد استهلاك الطاقة (kWh) بطريقة منطقية تعتمد على نوع الجهاز والفصل
base_energy = np.random.uniform(0.1, 1.5, size=records)
for i in range(records):
    if chosen_appliances[i] == "Air Conditioning" and seasons[i] == "Summer":
        base_energy[i] += np.random.uniform(1.5, 3.0)
    elif chosen_appliances[i] == "Heater" and seasons[i] == "Winter":
        base_energy[i] += np.random.uniform(1.0, 2.5)

# تجميع البيانات في جدول منظّم (DataFrame)
df = pd.DataFrame({
    "Home_ID": home_ids,
    "Date": [d.strftime("%Y-%m-%d") for d in dates],
    "Time": [d.strftime("%H:%M") for d in dates],
    "Appliance_Type": chosen_appliances,
    "Outdoor_Temp": np.round(temps, 2),
    "Season": seasons,
    "Household_Size": household_sizes,
    "Energy_kWh": np.round(base_energy, 2)
})

# حفظ الجدول كملف CSV في مجلد المشروع
df.to_csv("smart_home_energy.csv", index=False)
print("Dataset smart_home_energy.csv generated successfully with 1000 records!")
