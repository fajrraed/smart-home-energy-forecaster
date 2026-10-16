# Smart Home Energy Consumption Forecaster

A complete machine learning regression pipeline that generates simulated household energy records, engineers chronological time features, and builds a Random Forest prediction engine. It includes a live terminal interface capable of predicting active appliance-level power consumption (kWh) based on environmental characteristics.

## Pipeline Outputs Included
- smart_home_energy.csv: The generated 1,000-row baseline dataset.
- train_model.py: Script training the AI model to a 51.46% R2 accuracy score.
- predict_energy.py: Interactive prediction terminal script.
- output_log.txt: Log file displaying the verified 2.77 kWh live prediction output.

## Requirements
Install processing and machine learning dependencies:
```bash
pip install pandas numpy scikit-learn
```

## How to Run
1. Execute the trainer to view evaluation metrics: python train_model.py
2. Run the interactive interface to input custom environment factors: python predict_energy.py
