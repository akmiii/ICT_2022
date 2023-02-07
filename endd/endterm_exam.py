'''
-------------------------ENDTERM EXAM-----------------
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
except:
    pass
'''
In the following file, do not delete anything (comments, code, ...). Just add you code in every part (one per exercise).
Use my variable for input (if there is any), use my printing for output (if there is any).
You can upload your code to codepost.io to check the tests. A sucess in one test doesn't always mean than your exercise is correct,
a fail doesn't always mean that your exercise is wrong. I will check all codes.
At the end of exam, you should upload the last version of your code to codepost.io or to the online folder on Teams.
The only authorized packages are:
- pandas
- pyarrow
- fastparquet
- numpy
- sklearn
- matplotlib
- datetime

'''
import pandas as pd
import numpy as np
import sklearn.linear_model as skmod

if input1 == '1':

# ----------------------EXERCISE 1 - Data Cleaning--------------------------------------
# Instructions:
# Open the dataframe (Ex_1_price_to_clean_v8.parquet) with the read_parquet() function of the pandas package.
# If you upload your code to codepost use the the following path in the read_parquet() function : "Ex_1_price_to_clean_v8.parquet".
# Remove the duplicated line(s) from the dataframe, reset the indexes, sort it by the date column and print it.
# Do not change the format of columns (for example, if one column has int values, don't change it to float)

    df = pd.read_parquet("Ex_1_price_to_clean_v8.parquet")
    df = df.drop_duplicates()
    df = df.reset_index(drop = True)
    df = df.sort_values(by = 'Date')

# Here is the printing instruction (where df is the final dataframe cleaned, sorted by date and with reset indexes)
    print(df)
# ---------------------End of EXERCISE 1 --------------------------------------

elif input1 == '4':
# ----------------------EXERCISE 4 - Machine Learning II--------------------------------------
# Instructions:
# You have a list of feature named feature and a list of label named label.
# Make a linear regression with the features and the label and display the equation and the accuracy of your model.
# Do not use scaling or train/test sets. Choose the best printing instructions.
 features = [-7, -7, -9, -3, 8, -4, -5, 7, 8, -4, -4, -2, 4, -2, -4, 1, -10, -5, 1, -9]

 label = [-46.0, -75.0, -103.0, -46.0, 94.0, -50.0, -67.0, 56.0, 79.0, -46.0, -46.0, -24.0, 33.0, -16.0, -56.0, 3.0,-116.0, -48.0, 4.0, -113.0]

 features = np.array(features).reshape(-1,1)
 label = np.array(label).reshape(-1,1)

 model = skmod.LinearRegression()
 model = model.fit(features,label)
 w1 = model.coef_[0][0]
 b = model.intercept_[0]
 R2 = model.score(features,label)

# Here is several printings, choose the most appropriate one.
 print("The most accurate linear regression has the following equation: y' = {:0.2f}*x + {:0.2f} and its accuracy is: {:0.3f}".format(w1, b, R2))
    # print("The most accurate linear regression has the following equation: y' = {:0.2f}*x + {:0.2f} and its accuracy is: {:0.3f}".format(b, w1, R2))
    # print("The most accurate linear regression has the following equation: y' = {:0.2f}*x + {:0.2f} and its accuracy is: {:0.3f}".format(R2, w1, b))
# ----------------------End of EXERCISE 4 --------------------------------------
