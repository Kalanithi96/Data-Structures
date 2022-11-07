import sympy as sp
import numpy as np
import math

f = sp.sympify("2*x^2 + y^2 + 2*x*y -2*y + 2*x")
#f = sp.sympify("x^2 + y^2 -x")

x = sp.Symbol("x")
y = sp.Symbol("y")
L = sp.Symbol("L")


def Descent(S,lam):
    X = [0]*2
    temp = [0]*2
    while True:
        S1 = [S[0].evalf(subs={x:temp[0],y:temp[1]}),
             S[1].evalf(subs={x:temp[0],y:temp[1]})]
        
        X = np.array(temp) - lam * np.array(S1)
        print(X)
        if math.sqrt(np.sum((temp-X)**2)) < 0.0001:
            break
        temp = X
        
        print('\n\n')
        
def smartDescent(S):
    temp = [0]*2
    X1 = [0]*2
    for i in range(20):
        S1 = [S[0].evalf(subs={x:temp[0],y:temp[1]}),
              S[1].evalf(subs={x:temp[0],y:temp[1]})]
        
        X1 = np.array(temp) - L * np.array(S1)
        print(X1)
        print(f.evalf(subs={x:X1[0],y:X1[1]}))
        print(sp.Eq(sp.diff(f.evalf(subs={x:X1[0],y:X1[1]}),L),0))
        cp = sp.solve(sp.Eq(sp.diff(f.evalf(subs={x:X1[0],y:X1[1]}),L),0))
        
        print(cp)
        
        X1 = [X1[0].evalf(subs={L:cp[0]}),
              X1[1].evalf(subs={L:cp[0]})]
        print(X1)
        if math.sqrt(np.sum((np.array(temp)-np.array(X1))**2)) < 0.0001:
            break
        temp = X1
        
        print('\n\n')
        
        
        
S = [sp.diff(f,x),sp.diff(f,y)]
print(S)
temp = [0]*2
X = [0]*2
X1 = [0]*2
lam = 0.1


smartDescent(S)
Descent(S,lam)