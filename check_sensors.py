import yaml
import pandas as pd
import json


with open("config.yml") as f:
       config = yaml.safe_load(f)

sensors = pd.read_excel("sensors.xlsx")
calibrations = pd.read_csv("calibrations.csv")

merged = pd.merge(sensors, calibrations, on="sensor_id")

overdue = merged[merged["days_since_calibration"] > config["max_days_since_calibration"]]

records = overdue.to_dict(orient="records")

with open(config["output_file"], "w") as f:
    json.dump(records, f, indent=2)
