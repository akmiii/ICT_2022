# ----------------------EXERCISE 1 - Data Cleaning--------------------------------------
# Instructions:
# Open the dataframe (Ex_1_price_to_clean_v3.parquet) with the read_parquet() function of the pandas package.
# If you upload your code to codepost use the the following path in the read_parquet() function : "Ex_1_price_to_clean_v3.parquet".
# Remove the line(s) with the data under the wrong format from the dataframe, reset the indexes, sort it by the date column and print it.
# Keep the same format for the date column and be sure than the other columns are in float format.

import numpy as np
import pandas as pd
import sklearn.preprocessing as skprepro
import sklearn.linear_model as skmod

df = pd.read_parquet("Ex_1_price_to_clean_v3.parquet")

# print(df)

for index, lines in df.iterrows():
    try:
        if(lines['Low'] == 'no_value_here'): 
            df.loc[index, 'Low'] = np.nan
    except:
        pass

df.dropna(inplace= True)

df['Open'] = [float(i) for i in df['Open']]
df['High'] = [float(i) for i in df['High']]
df['Low'] = [float(i) for i in df['Low']]
df['Close'] = [float(i) for i in df['Close']]
df['Adj Close'] = [float(i) for i in df['Adj Close']]
df['Volume'] = [float(i) for i in df['Volume']]

# print(df)

# print(df.isnull().sum())
df = df.sort_values(['Date'], ignore_index=True)
print(df)