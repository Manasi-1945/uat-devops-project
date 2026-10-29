import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference = pd.DataFrame({
    "temperature": [20, 21, 19, 22, 20, 21, 19, 20, 22, 21],
    "requests": [100, 110, 105, 98, 120, 115, 108, 102, 111, 109],
})

current = pd.DataFrame({
    "temperature": [30, 31, 29, 32, 30, 31, 29, 30, 32, 31],
    "requests": [200, 210, 205, 198, 220, 215, 208, 202, 211, 209],
})

report = Report([DataDriftPreset()])
snapshot = report.run(current, reference)
snapshot.save_html("evidently_report.html")

print("Monitoring complete.")
print("Report saved as evidently_report.html")