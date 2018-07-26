import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def cost(theta0,theta1,x,y):
    J = 0
    m = len(x)
    for i in range(m):
        h = theta1*x[i]+theta0
        J +=(h-y[i])**2
    J /=2*m
    return J

def partial_cost_theta1(theta0,theta1,x,y):
    h = theta0+theta1*x
    diff = (h-y)*x
    partial = diff.sum()/x.shape[0]
    return partial

def partial_cost_theta0(theta0,theta1,x,y):
    h = theta0+theta1*x
    diff = h-y
    partial = diff.sum()/x.shape[0]
    return partial

def gradient_descent(x,y,alpha=0.1,theta0=0,theta1=1):
    max_epochs = 1000
    counter = 0
    c =cost(theta0,theta1,x,y)
    costs =[c]
    convergence = 0.00000001
    cprev = c+10
    theta0s=[theta0]
    theta1s=[theta1]
    while (np.abs(cprev-c)>convergence) and (counter<max_epochs):
        cprev = c
        update0 = alpha*partial_cost_theta0(theta0,theta1,x,y)
        update1 = alpha*partial_cost_theta1(theta0,theta1,x,y)

        theta0 -= update0
        theta1 -= update1
        theta0s.append(theta0)
        theta1s.append(theta1)

        c = cost(theta0,theta1,x,y)

        costs.append(c)
        counter +=1
    return {"theta0":theta0,"theta1":theta1,"costs":costs}


pga = pd.read_csv("../data/pga.csv")

print(pga.head())

pga.distance = (pga.distance - pga.distance.mean())/pga.distance.std()
pga.accuracy = (pga.accuracy - pga.accuracy.mean())/pga.accuracy.std()
print(pga.head())

plt.scatter(pga.distance,pga.accuracy)
plt.xlabel("normalized distance")
plt.ylabel("normalized accuracy")
plt.show()

print(cost(0,1,pga.distance,pga.accuracy))

theta0 = 100
thetals = np.linspace(-3,2,100)
costs = [cost(theta0,x,pga.distance,pga.accuracy) for x in thetals ]
plt.plot(thetals,costs)
plt.show()


print("theta1 =",gradient_descent(pga.distance,pga.accuracy)["theta1"])
descend = gradient_descent(pga.distance,pga.accuracy, alpha=0.01)
plt.scatter(range(len(descend["costs"])),descend["costs"])
plt.show()