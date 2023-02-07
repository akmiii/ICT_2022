import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection as sksel
import sklearn.preprocessing as skprepro
import sklearn.linear_model as skmod
import sklearn.preprocessing as skprepro
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
if input1 == '4':
# ----------------------EXERCISE 4 - Machine Learning II--------------------------------------
# Instructions:
# You have a list of feature named feature and a list of label named label.
# Make a linear regression with the features and the label and display the equation and the accuracy of your model.
# Do not use scaling or train/test sets. Choose the best printing instructions.

    features = [-4, -3, -6, -10, 9, 3, 9, -4, -5, -9, -1, -2, 7, -2, -3, -2, -4, -1, 6, 5]
    label = [-26.0, -7.0, -48.0, -72.0, 72.0, 22.0, 94.0, -22.0, -26.0, -43.0, 3.0, -3.0, 68.0, -3.0, -9.0, -3.0, -24.0, 4.0, 73.0, 68.0]
    x = np.array(features).reshape(-1, 1)
    y = np.array(label).reshape(-1, 1)

    model = skmod.LinearRegression()
    model = model.fit(x, y)
    w1 = model.coef_[0][0]
    b = model.intercept_[0]
    R2 = model.score(x, y)

    # print(w1)
    # print(b)



# Here is several printings, choose the most appropriate one:
    print("The most accurate linear regression has the following equation: y' = {:0.2f}*x + {:0.2f} and its accuracy is: {:0.3f}".format(w1, b, R2))	