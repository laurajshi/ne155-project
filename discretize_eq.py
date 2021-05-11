import numpy as np
from input_deck import *

# system parameters

# flags for boundary conditions
leftVac = True
botVac = True
rightRef = True
topRef = True

delta, eps = getSpacingArrays(check=False)
D_c, Sigma_a, Source = getMatricesFromInput(show=False, check=False)
#get averaged values for an (n x m system)
Sigma_av = make_av_matrix(Sigma_a, eps, delta)
        

def buildFullA(n): #assuming n is greater than or equal to 2
    A = np.zeros((n**2, n**2))
    A[0:n, 0:n], A[0:n, n:2*n] = buildCenter(n, 0), buildTop(n, 0)
    for k in range(1, (n-1)): 
        A[(k*n):(k+1)*n, (k-1)*n:(k*n)] = buildBot(n, k) #dimensions n, k is value to invoke
        A[(k*n):(k+1)*n, (k*n):(k+1)*n] = buildCenter(n, k)
        A[(k*n):(k+1)*n, (k+1)*n:(k+2)*n] = buildTop(n, k)
    A[(n-1)*n:n*n, (n-2)*n:(n-1)*n]= buildBot(n, (n-1))
    A[(n-1)*n:n*n, (n-1)*n:n*n] = buildCenter(n, (n-1))
    #submatrix creation
    #adjust to take non square matrices
    return A

def buildCenter(n, m): #right now produces a square n x n submatrix
        #n x n is dimension of individual matrix, m is the relative matrix number
        A = np.zeros((n, n)) 
        A[0, 0], A[0, 1] = aC(0, m), aR(0, m) #first line
        for j in range(1, (n-1)):
            A[j, (j-1)], A[j, j], A[j, (j+1)] = aL(j, m), aC(j, m), aR(j, m) #middle lines
        A[(n-1), (n-2)], A[(n-1), (n-1)] = aL(n-1, m), aC((n-1), m) #last line
        return A

def buildBot(n, m):
    A = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                A[i][j] = aB(j, m)
    return A

def buildTop(n, m):
    A = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                A[i][j] = aT(j, m)
    return A
# Definitions of left, right, bottom, top and center influence including BCs
def aL(i, j):
    if ((leftVac and i == 0) or (botVac and j == 0)):
        return 0
    if (topRef and j == m - 1): #top reflecting condition, nothing above
        return -(D_c[j-1][i-1]*eps[j-1])/(2*delta[i-1])
    return -(D_c[j-1][i-1]*eps[j-1] + D_c[j][i-1]*eps[j])/(2*delta[i-1])

def aR(i, j):
    if ((leftVac and i == 0) or (botVac and j == 0) or (rightRef and i == n - 1)):
        return 0
    if (topRef and j == m - 1): #top reflecting condition, nothing above
        return -(D_c[j-1][i]*eps[j-1])/(2*delta[i])
    return -(D_c[j-1][i]*eps[j-1] + D_c[j][i]*eps[j])/(2*delta[i])

def aB(i, j):
    if ((leftVac and i == 0) or (botVac and j == 0)):
        return 0
    if (rightRef and i == n - 1):
        return -(D_c[j-1][i-1]*delta[i-1])/(2*eps[j-1])
    return -(D_c[j-1][i-1]*delta[i-1] + D_c[j-1][i]*delta[i])/(2*eps[j-1])

def aT(i, j):
    if ((leftVac and i == 0) or (botVac and j == 0) or (topRef and j == m - 1)):
        return 0 #no contribution from top if have reflecting bc
    if (rightRef and i == n - 1):
        return (D_c[j][i-1]*delta[i-1])/(2*eps[j])
    return -(D_c[j][i-1]*delta[i-1] + D_c[j][i]*delta[i])/(2*eps[j])

def aC(i, j):
    if ((leftVac and i == 0) or (botVac and j == 0)):
        return 1
    return Sigma_av[i][j]- (aL(i, j) + aR(i, j) + aB(i, j) + aT(i, j)) 

