import pandas as pd
import numpy as np
from statsmodels.formula.api import logit

data = pd.read_csv('projects/DataCamp_projects/project_7_car/car_insurance.csv')

# Identify the single feature of the data that is the best predictor of whether a customer will put in a claim (the "outcome" column), excluding the "id" column.

def test_variable(col, df):
  mdl = logit(f'outcome ~ {col}', data=df).fit()

  matrix = mdl.pred_table()

  TN = matrix[0,0]
  TP = matrix[1,1]
  FN = matrix[1,0]
  FP = matrix[0,1]

  accuracy = (TN + TP) / (TN + TP + FN + FP)
  return accuracy

result = dict()

print(test_variable('annual_mileage', data))

for col_name, col_series in data.items():
  if col_name == 'outcome': continue
  col_accuracy = test_variable(col_name, data)
  result[col_name] = float(col_accuracy)

print(result) 

result = pd.DataFrame([result])

# Store as a DataFrame called best_feature_df, containing columns named "best_feature" and "best_accuracy" with the name of the feature with the highest accuracy, and the respective accuracy score.