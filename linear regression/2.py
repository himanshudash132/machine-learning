import matplotlib.pyplot as plt
import numpy as np
from sklearn import  datasets,linear_model
from sklearn.metrics import mean_squared_error



diabetes = datasets.load_diabetes()
diabetes_X = np.array([[1], [2], [3]])

diabetes_X_train = diabetes_X     # training
diabetes_X_test = diabetes_X      # testing

diabetes_Y_train =np.array([3, 2, 4])      # training
diabetes_Y_test = np.array([3, 2, 4])        # testing

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_Y_train)

diabetes_Y_predicted = model.predict(diabetes_X_test)

print("Mean squared error is: ", mean_squared_error(diabetes_Y_test, diabetes_Y_predicted,))


print("weights:",model.coef_)   # tan@
print("Intercept:",model.intercept_)

plt.scatter(diabetes_X_test, diabetes_Y_test)
plt.plot(diabetes_X_test, diabetes_Y_predicted)
plt.show()




# Mean squared error is:  2561.320427728385
# weights: [941.43097333]
# Intercept: 153.39713623331644

# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
# print(diabetes.keys())
# print(diabetes.data)
# print(diabetes.DESCR)
# print(diabetes_X)
