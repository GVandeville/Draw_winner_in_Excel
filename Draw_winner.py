import pandas as pd
import numpy as np

# read the Excel file
df_sheet_index = pd.read_excel('Players_for_08-31-2022.xlsx')

# get the number of rows
rows = df_sheet_index.shape[0]

# get the index of the winner
index = np.random.randint(0, rows)

# read the winner
print(df_sheet_index.iloc[index])
