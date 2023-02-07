# ----------------------EXERCISE 5 - Machine Learning III--------------------------------------
# Instructions:
# You have one feature. You objective is to transform it into a matrix for a polynomial regression  of degree 4.
# In the matrix, the first column is the feature, the second : the feature power 2, ... until power 4.
# You can find an example of the desired matrix in the document Ex_5_poly_matrix_V3.txt
import numpy as np
import pandas as pd
import sklearn.preprocessing as skprepro
import sklearn.linear_model as skmod

feature = [373, 349, -910, -110, -790, 468, 70, 104, -164, -874, 307, -515, -392, -406, 79, 326, -340, -875, 411, -207, -391, -299, -488, -236, -856, 153, -675, -909, 451, 459]
feature = np.array(feature).reshape(-1, 1)


poly4 = skprepro.PolynomialFeatures(4, include_bias = False)
x_polymial = poly4.fit_transform(feature)


# Here is the print instructions to print the polynomial matrix rounded.
print(np.around(x_polymial,3))