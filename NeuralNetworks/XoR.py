#  Neural networks for solving XOR problem:

# 0 0 --> 0
# 0 1 --> 1
# 1 0 --> 1
# 1 1 --> 0
 
import numpy as np
import matplotlib.pyplot as plt

#Activation Function

def sigmoid(x):
  return 1/(1+np.exp(-x))

# Sigmoid Derivative for back propogation

def sigmoid_derivative(x):
  return sigmoid(x)*(1-sigmoid(x))


#Forward function
def forward(x,w1,w2,predict = False):
  a1 = np.matmul(x,w1)
  z1 = sigmoid(a1)

  #Create and add bias 
  bias = np.ones((len(z1), 1))
  z1 = np.concatenate((bias,z1),axis = 1)
  a2 = np.matmul(z1,w2)
  z2 = sigmoid(a2)
  if predict:
    return z2
  return a1,z1,a2,z2

def backprop(a2,z0,z1,z2,y):
  delta2 = z2-y
  Delta2 = np.matmul(z1.T, delta2)
  delta1 = (delta2.dot(w2[1:,:].T))*sigmoid_derivative(a1)
  Delta1 = np.matmul(z0.T, delta1)
  return delta2, Delta1, Delta2

X = np.array([[1,0,0],
              [1,0,1],
              [1,1,0],
              [1,1,1]])

# Outputs
y = np.array([[0],[1],[1],[0]])

#Weights 

w1 = np.random.randn(3,5)
w2 = np.random.randn(6,1)

# init learning rate
lr = 0.09

costs = []

#init epochs
epochs = 150000

m = len(X)
 
#Start training 
for i in range(epochs):

  #Forward
  a1,z1,a2,z2 = forward(X,w1,w2)

  #Back Prop
  delta2, Delta1, Delta2 = backprop(a2,X,z1,z2,y)

  w1 -= lr*(1/m)*Delta1
  w2 -= lr*(1/m)*Delta2

  #Add costs to list for plotting

  c = np.mean(np.abs(delta2))
  costs.append(c)

  if i % 1000 == 0:
    print(f"Iteration: {i}. Error: {c}")

#Training complete 
print("Training Complete...")

#Make predictions 
z3 = forward(X,w1,w2,True)
print("Precentages: ")
print(z3)
print("Predictions: ")
print(np.round(z3))

#plot cost
plt.plot(costs)
plt.show()