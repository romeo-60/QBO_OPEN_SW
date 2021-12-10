#!/usr/bin/python3
#test perception
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
X, y = datasets.make_blobs(n_samples=10,n_features=2,
                           centers=2,cluster_std=1.5,
                           random_state=2)
#Plotting
#fig = plt.figure(figsize=(10,8))
#plt.plot(X[:, 0][y == 0], X[:, 1][y == 0], 'g^')
#plt.plot(X[:, 0][y == 1], X[:, 1][y == 1], 'bo')
#plt.xlabel("feature 1")
#plt.ylabel("feature 2")
#plt.title('Random Classification Data with 2 classes')
#plt.show()
print("X","\n", X) 
print ("-----------")
print ("y","\n", y)
print ("-----------")
def step_func(z):
        return 1.0 if (z > 0) else 0.0

def perceptron(X, y, lr, epochs):
    
    # X --> Inputs.
    # y --> labels/target.
    # lr --> learning rate.
    # epochs --> Number of iterations.
    
    # m-> number of training examples
    # n-> number of features 
    m, n = X.shape
    print("m,", m, "\t", "n", n)
    print("-------------")
    # Initializing parapeters(theta) to zeros.
    # +1 in n+1 for the bias term.
    theta = np.zeros((n+1,1))
    
    # Empty list to store how many examples were 
    # misclassified at every iteration.
    n_miss_list = []
    
    # Training.
    print ("epochs", epochs)
    for epoch in range(epochs):
        print(epoch)
        # variable to store #misclassified.
        n_miss = 0
        
        # looping for every example.
        for idx, x_i in enumerate(X):
            
            # Insering 1 for bias, X0 = 1.
            x_i = np.insert(x_i, 0, 1).reshape(-1,1)
            
            # Calculating prediction/hypothesis.
            y_hat = step_func(np.dot(x_i.T, theta))
            
            # Updating if the example is misclassified.
            if (np.squeeze(y_hat) - y[idx]) != 0:
                theta += lr*((y[idx] - y_hat)*x_i)
                
                # Incrementing by 1.
                n_miss += 1
        
        # Appending number of misclassified examples
        # at every iteration.
        n_miss_list.append(n_miss)
        
    return theta, n_miss_list 
    
    
def plot_decision_boundary(X, theta):
    
    # X --> Inputs
    # theta --> parameters
    
    # The Line is y=mx+c
    # So, Equate mx+c = theta0.X0 + theta1.X1 + theta2.X2
    # Solving we find m and c
    x1 = [min(X[:,0]), max(X[:,0])]
    m = -theta[1]/theta[2]
    c = -theta[0]/theta[2]
    x2 = m*x1 + c
    print("x1",x1, "\t", "x2", x2, "\t", "c", c)
   
    # Plotting
    fig = plt.figure(figsize=(10,8))
    plt.plot(X[:, 0][y==0], X[:, 1][y==0], "g^")
    plt.plot(X[:, 0][y==1], X[:, 1][y==1], "bo")
    plt.xlabel("feature 1")
    plt.ylabel("feature 2")
    plt.title("Perceptron Algorithm")
    plt.plot(x1, x2, 'y-')
    plt.show()
    
    
theta, miss_l = perceptron(X, y, 0.5, 5)
plot_decision_boundary(X, theta) 

  