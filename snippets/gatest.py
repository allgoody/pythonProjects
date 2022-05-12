import pandas as pd

csvData = pd.read_csv('./test_data/ga_test_data.csv')
print(csvData.head(5))