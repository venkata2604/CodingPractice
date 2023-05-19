import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from scipy.io import loadmat
data = loadmat('ex5data1.mat')
# print(data.keys())

y_train = np.c_[data['y']]
X_train = np.c_[np.ones_like(data['X']), data['X']]

yval = np.c_[data['yval']]
Xval = np.c_[np.ones_like(data['Xval']), data['Xval']]


# print('X_train:', X_train.shape)
# print('y_train:', y_train.shape)
# print('Xval:', Xval.shape)
# print('yval:', yval.shape)

# X_test = np.c_[data['Xtest']]
X_test = np.c_[np.ones_like(data['Xtest']), data['Xtest']]
# print(X_test)

y_test = np.c_[data['ytest']]
# print(y_test)


plt.scatter(X_train[:,1], y_train, s=50, c='r', marker='x', linewidths=1)
plt.xlabel('Change in water level (x)')
plt.ylabel('Water flowing out of the dam (y)')
plt.ylim(ymin=0);
plt.show();


mean_ciw = sum((X_train[:,1]))/(len(X_train[:,1]))
print(mean_ciw)

mean_wfo = float(sum(y_train[:])/float((len(y_train[:]))))
print(mean_wfo)

def variance(values, mean):
    variance = 0
    for val in values:
        variance = float(variance + ((val-mean)**2))
    return variance

# A simple way to write the above def for variance
# def variance(values, mean):
#     return sum([(val-mean)**2 for val in values])
# variance(X_train[:,1], mean_ciw)

variance_ciw = variance(X_train[:,1], mean_ciw)
print(variance_ciw)

variance_wfo = variance(y_train, mean_wfo)
print(variance_wfo)

# calculating covariance

def covariance(inparm, output, mean_input, mean_output):
    covariance = 0
    for i in range(len(output)):
        covariance = (covariance + ((inparm[i] - mean_input)*(output[i] - mean_output)))
    return covariance

covariance_final = float(covariance(X_train[:,1], y_train[:], mean_ciw, mean_wfo))
print(covariance_final)

# Linear Fitting of parameters
# guiding equation Y = mX+c
# slope(m), constant(c)
m = covariance_final/variance_ciw
c = mean_wfo - (m*mean_ciw)
print(m,c)

# prediction
wfo = (m*float(input("enter the change in reservoir levels"))+c)
print('the predicted water flowing out from model =', wfo)

# fitting the obtained regression equation to the data

x = X_train[:,1]
y = (m*x)+c

# fig = plt.figure()
plt.plot(x,y, label = 'prediction curve')


plt.scatter(X_train[:,1], y_train, s=50, c='r', marker='x', linewidths=1)
plt.xlabel('Change in water level (x)')
plt.ylabel('Water flowing out of the dam (y)')
plt.ylim(ymin=-5, ymax=50)
plt.xlim(xmin = -60, xmax=50)
plt.legend(loc = 1);
plt.show()

# calculating linear regression error
# J is the cost function
# Jtest is the test set error
# H is the hypothesis (y) = mx + c
for i in range(len(X_test)):
    H = (m * X_test[i,1])+c
    # print(H)
    Jtest = (1/(2*m))*(sum((H - y_test[i])**2))
    # print(Jtest)
    plt.scatter(i, Jtest, s=50, c='r', marker ='x', linewidths=1)
    plt.xlabel('iterations')
    plt.ylabel('Test set error J()')
plt.show()

