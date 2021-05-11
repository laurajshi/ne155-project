import numpy as np

def gs(A, b, xk):
    newX = []
    n = len(b)
    for i in range(0, n):
        sum1 = 0
        sum2 = 0
        for j in range(0, n):
            if (j < i):
                sum1= sum1 + A[i][j]*newX[j]
            elif (j > i):
                sum2 = sum2 + A[i][j]*xk[j]
        
        xi = (1/(A[i][i]))* (b[i] - sum1 - sum2)
        newX.append(xi)
    return np.array(newX)

def sor(A, b, xk, w):
    newX = []
    n = len(b)
    for i in range(0, n):
        sum1 = 0
        sum2 = 0
        for j in range(0, n):
            if (j < i):
                sum1= sum1 + A[i][j]*newX[j]
            elif (j > i):
                sum2 = sum2 + A[i][j]*xk[j]
        xi = (1- w)*xk[i] + (w/(A[i][i]))* (b[i] - sum1 - sum2)
        newX.append(xi)
    return np.array(newX)

#general convergence checker that is general per method
def performIteration(A, b, xk, tol, method, *w):
    iter_count = 0
    err = np.inf
    while err > tol:
        X_new = method(A, b, xk, *w)
        err = (np.linalg.norm((X_new - xk))) / (np.linalg.norm(X_new)) #relative error
        iter_count = iter_count + 1
        xk = X_new
    return xk, err, iter_count