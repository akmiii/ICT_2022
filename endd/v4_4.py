# ----------------------EXERCISE 4 - Machine Learning II--------------------------------------
import sklearn.linear_model as skmod
import numpy as np
import matplotlib.pyplot as plt

feature1 = np.array([-1, -8, 8, -5, 9, 1, 1, 8, -3, 9, 6, 1, -3, -7, 5, -5, 3, -1, -8, -6])
label = np.array([9.0, 66.0, -35.0, 31.0, -75.0, -5.0, -7.0, -58.0, 23.0, -50.0, -34.0, -8.0, 23.0, 32.0, -48.0, 46.0, -30.0, 7.0, 60.0, 30.0])
model = skmod.LinearRegression().fit(feature1.reshape(-1,1), label.reshape(-1,1))
plt.scatter(feature1, label)
plt.plot([-10,10], model.predict(np.array([[-10], [10]])))
plt.show()