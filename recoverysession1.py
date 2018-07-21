from matplotlib import pyplot as plt
import numpy as np

def sigmoid(inputs):
    outputs = []

    for x in inputs:
        cal = 1 / (1+np.exp(-x))
        outputs.append(cal)

    return outputs

def softMax(inputs):
    outputs = np.exp(inputs) / sum(np.exp(inputs))
    return outputs

def tanh(inputs):
    outputs = []

    for x in inputs :
        cal = np.tanh(x)
        outputs.append(cal)
    return outputs

def reLU(inputs):
    outputs = []

    for x in inputs:
        if(x>=0):
            outputs.append(x)
        else:
            outputs.append(0)
    return  outputs

inputs = list(range(-20,21))
#inputs1 = list(range(0,21))

print(inputs)

x1 = inputs
x2 = inputs
x3 = inputs
x4 = inputs

y1 = sigmoid(inputs)
y2 = softMax(inputs)
y3 = tanh(inputs)
y4 = reLU(inputs)

print("Sigmoid ", y1,"SoftMax ", y2, "tanh ",y3 , "reLU ", y4 )


plt.plot(x1,y1,'g',label="Sigmoid")
plt.plot(x2,y2,'c',label="SoftMax")
plt.plot(x3,y3,'b',label="Tanh")
plt.plot(x4,y4,'r',label="ReLU")
plt.xlabel("Inputs")
plt.ylabel("Tanh")
plt.show()