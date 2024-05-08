#r論理回路を実装

import numpy as np

# b + w1x1 + w2x2 = tmp
def AND(x1,x2):
    w1,w2,b = 0.5,0.5,-0.7
    x = np.array([x1,x2])
    w = np.array([w1,w2])
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def NAND(x1,x2):
    w1,w2,b = -0.5,-0.5,0.7
    x = np.array([x1,x2])
    w = np.array([w1,w2])
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def OR(x1,x2):
    w1,w2,b = 0.5,0.5,-0.2
    x = np.array([x1,x2])
    w = np.array([w1,w2])
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def NOT(x1):
    w1,w2,b = -0.5,-0.5,0.7
    x = np.array([x1,1])
    w = np.array([w1,w2])
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y

if __name__ == "__main__":
    print(AND(0,0))