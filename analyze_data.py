import pandas as pd

# 1. قراءة ملف البيانات الذي قمنا بتوليده
df = pd.read_csv("smart_home_energy.csv")

# 2. عرض أول 5 أسطر من البيانات لإلقاء نظرة سريعة عليها
print("--- First 5 Rows of the Dataset ---")
print(df.head())
print("\n" + "="*50 + "\n")

# 3. عرض معلومات عامة عن الأعمدة وأنواع البيانات (تأكد من عدم وجود قيم مفقودة)
print("--- Dataset Information ---")
print(df.info())
print("\n" + "="*50 + "\n")

# 4. استخراج إحصاءات سريعة للأرقام (المتوسط، أقل قيمة، أعلى قيمة)
print("--- Statistical Summary ---")
print(df.describe())
print("\n" + "="*50 + "\n")

# 5. معرفة أكثر الأجهزة استهلاكاً للطاقة في المتوسط
print("--- Average Energy Consumption per Appliance (Top Consumers) ---")
appliance_summary = df.groupby("Appliance_Type")["Energy_kWh"].mean().sort_values(ascending=False)
print(appliance_summary)
