import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Define our levels and regions
levels = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
regions = ["North", "South", "East", "West"]

# Create 30 rows of data
data = {
    "Employee_ID": range(1, 101),
    "leadership": np.random.choice(levels, 100),
    "growth_opportunity": np.random.choice(levels, 100),
    "work_environment": np.random.choice(levels, 100),
    "compensation": np.random.choice(levels, 100),
    "culture": np.random.choice(levels, 100),
    "Region": np.random.choice(regions, 100)
}

df = pd.DataFrame(data)

# To match your R code 'skip = 1', we add a dummy header row
dummy_row = pd.DataFrame([["Metadata", "v1.0", "", "", "", "", ""]], columns=df.columns)
final_df = pd.concat([dummy_row, df])

# Export to Excel
final_df.to_excel("engagement_survey.xlsx", sheet_name="engagement_survey", index=False)
print("File 'engagement_survey.xlsx' created successfully!")