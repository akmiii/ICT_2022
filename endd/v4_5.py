# ----------------------EXERCISE 5 - Machine Learning III--------------------------------------
# Instructions:
# You have two features : feature1 and feature2. You objective is to make a two columns matrix and
# to separate them into a train and a test set. The size of train set is 80 % of the original matrix.
# Remember to use shuffle = False in the train_test_split function of the scikit-learn package.
# At the end print only the test arrays. 
# You can find the desired matrix in the document Ex_5_x_tests_matrix_V4.txt
import numpy as np
import sklearn.linear_model as skmod
import sklearn.model_selection as sksel
import sklearn.preprocessing as skprepro
import matplotlib.pyplot as plt

feature1 = [-16, -965, -813, -619, -334, 151, 74, 154, -269, -833, -976, -652, -713, -880, 37, -707, -352, 177, 179, 91, -702, -189, 308, -999, -660, 354, -209, 272, -73, -45]
feature2 = [-3, -8, -7, 0, -9, 1, 0, -7, -9, -1, -6, 0, -9, -8, -3, -5, 2, 0, -7, -9, 3, 0, -5, -6, -5, -1, 3, 2, -3, -9]

feature1 = np.array(feature1).reshape(-1, 1)
feature2 = np.array(feature2).reshape(-1, 1)

arr_x = np.hstack([feature1, feature2])

scaler = skprepro.StandardScaler()
scaler_f = scaler.fit(arr_x)
data_x_stan = scaler_f.transform(arr_x)

# print(data_x_stan)

# data_x_train, data_x_test = sksel.train_test_split(arr_x,
#                                                train_size = 0.8, 
#                                                shuffle = False)

data_x_train, data_x_test = sksel.train_test_split(data_x_stan,
                                               train_size = 0.8, 
                                               shuffle = False)
print(data_x_test)       