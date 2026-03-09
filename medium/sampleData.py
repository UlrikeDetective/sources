import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Define our levels and regions
levels = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
regions = ["North", "South", "East", "West"]

# Create 30 rows of data
data = {
    "Respondent_ID": range(1, 131),
    "question_1": np.random.choice(levels, 130),
    "question_2": np.random.choice(levels, 130),
    "question_3": np.random.choice(levels, 130),
    "question_4": np.random.choice(levels, 130),
    "Region": np.random.choice(regions, 130)
}

df = pd.DataFrame(data)

# To match your R code 'skip = 1', we add a dummy header row
dummy_row = pd.DataFrame([["Metadata", "v1.0", "", "", "", ""]], columns=df.columns)
final_df = pd.concat([dummy_row, df])

# Export to Excel
final_df.to_excel("customer_feedback.xlsx", sheet_name="survey_data", index=False)
print("File 'customer_feedback.xlsx' created successfully!")