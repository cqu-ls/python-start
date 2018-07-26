import numpy as np
import matplotlib.pyplot as plt
from sklearn import  datasets

class LinearRegression():
    def __init__(self):
        self.w=None

    def fit(self,X,y):
        print(X.shape)
        X = np.insert(X,0,1,axis=1)
        X_ = np.linalg.inv(X.T.dot(X))
        self.w = X_.dot(X.T).dot(y)

    def predict(self,X):
        X = np.insert(X,0,1,axis=1)
        y_pred = X.dot(self.w)
        return y_pred


def main():
    diabetes = datasets.load_diabetes()
    X = diabetes.data[:,np.newaxis,2]
    print("************")
    print(X.shape)

    x_train,x_test = X[:-20],X[-20:]
    y_train,y_test = diabetes.target[:-20],diabetes.target[-20:]

    clf = LinearRegression()
    clf.fit(x_train,y_train)
    y_pred = clf.predict(x_test)
    plt.scatter(x_test[:,0],y_test,color="b")
    plt.plot(x_test[:,0],y_pred,color="r")
    plt.show()


if __name__ == '__main__':
    main()
