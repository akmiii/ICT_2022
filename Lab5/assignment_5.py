'''
The objective of this assignment is to clean the csv file of the attendance.
The path to the csv file is "attendance_to_clean.csv"
You can find it in the instruction folder.
List of installed and authorized packages :
    - csv
    - pandas
    - datetime
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:

import pandas as pd
import numpy as np

missing_values = ['_', 'NaN', 'error']
df = pd.read_csv(r"attendance_to_clean.csv", 
    na_values = missing_values)
    
# print(df)

for index, lines in df.iterrows():
    try:
        a = int(lines['COUNT'])
        if(a > 2):
            df.loc[index, 'COUNT'] = np.nan
    except:
        pass

for index, lines in df.iterrows():
    try:
        if(lines['COUNT'] == 'two'):
            df.loc[index, 'COUNT'] = np.nan
    except:
        pass


for index, lines in df.iterrows():
    try:
        if (lines['DATE'] < '2022-09-01'):
        # if(lines['DATE'] == '1968-09-27' or 
        # lines['DATE'] == '2020-10-07' or 
        # lines['DATE'] == '2022-07' or 
        # lines['DATE'] == '2022-01-13'): 
            df.loc[index, 'DATE'] = np.nan
    except:
        pass

for index, lines in df.iterrows():
    try:
        if (lines['BEGIN_HOUR'] < 9 or lines['BEGIN_HOUR'] > 17):
            df.loc[index, 'BEGIN_HOUR'] = np.nan
    except:
        pass

for index, lines in df.iterrows():
    try:
        if(lines['NAME_STUDENT'] == '10'): 
            df.loc[index, 'NAME_STUDENT'] = np.nan
    except:
        pass


df.dropna(inplace=True)
df.drop_duplicates(inplace = True)


# print(df.isnull().sum())

df['COUNT'] = [float(i) for i in df['COUNT']]

df = df.sort_values(['NAME_STUDENT', 'DATE', 'BEGIN_HOUR', 'WEEK'], ignore_index=True)

print(df)