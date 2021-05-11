import scipy as sc
from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

# Set some parameters for plotting
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (12, 9)
plt.rcParams['font.size'] = 16

#### methods to create the input deck matrices
def createDividedMatrix(n, m, def_val, division = 2 , dF = 2, vert = True):
    sV = int((1/division) * n)
    output = np.ones((n-1, m-1))*def_val #coeffient grid, initialize all to default value
    if (vert):
        output[:, :sV] = output[:, :sV]*dF #left regime greater by diff fact
    else:
        output[:sV, :] = output[:sV, :]*dF
    return output
def createLineMatrix():
    return 0

def createPointMatrix(n, m, def_val): #add in functionality for center and corner
    output = np.ones((n-1, m-1))
    output[int((n-1)/2), int((m-1)/2)] = def_val
    return output

### methods to average out the matrix
def make_av_matrix(orig_matrix, eps, delta):
    a, b = orig_matrix.shape
    n, m = a + 1, b + 1 #set values for returned array
    av_matrix = np.zeros((n, m))
    
    #corner cases, only keep 1/4th because on the corner (throws out 3 other points):
    av_matrix[0][0] = (1/4)*orig_matrix[0][0]*eps[0]*delta[0]
    av_matrix[0][m-1] = (1/4)*orig_matrix[0][m-2]*eps[0]*delta[m-2]
    av_matrix[n-1][0] = (1/4)*orig_matrix[n-2][0]*eps[n-2]*delta[0]
    av_matrix[n-1][m-1] = (1/4)*orig_matrix[n-2][m-2]*eps[n-2]*delta[m-2]
    
    #edge cases, will be half of center magnitude because throw out 2 points:
    # left edge, y = 0; right edge, y = m-2 in original
    for x in range(1, n-1):
        av_matrix[x][0] = (1/4)* (orig_matrix[x-1][0]*eps[x-1]*delta[0] + orig_matrix[x][0]*eps[x]*delta[0])
        av_matrix[x][m-1] = (1/4)* (orig_matrix[x-1][m-2]*eps[x-1]*delta[m-2] + orig_matrix[x][m-2]*eps[x]*delta[m-2])
        
    #top edge, x = 0; bottom edge, x = n-2 in original
    for y in range(1, m-1):
        av_matrix[0][y] = (1/4)* (orig_matrix[0][y-1]*eps[0]*delta[y-1] + orig_matrix[0][y]*eps[0]*delta[y])
        av_matrix[n-1][y] = (1/4)* (orig_matrix[n-2][y-1]*eps[n-2]*delta[y-1] + orig_matrix[n-2][y]*eps[n-2]*delta[y])
    
    #center cases:
    for x in range(1, (n-1)):
        for y in range(1, (m-1)):
            av_matrix[x][y] = (1/4)*(orig_matrix[x-1][y-1]*eps[x-1]*delta[y-1] + #topL
                                     orig_matrix[x][y-1]*eps[x]*delta[y-1] + #botL
                                     orig_matrix[x-1][y]*eps[x-1]*delta[y] + #topR
                                     orig_matrix[x][y]*eps[x]*delta[y]) #botR
    return av_matrix

def applySourceBC(Source):
    Source[:, 0] = 0 #all left elements have no flux b/c vacuum
    Source[0, :] = 0 #all bottom elements have no flux b/c vacuum
    return Source

def reshape_source(source_in):
    n, m = source_in.shape
    # no need to flip np.flip(source_in, 0).reshape((n*m), 1) 
    # since would just end up flipping back everything, reduces complication, just use current grid
    reshaped = source_in.reshape((n*m), 1)
    return reshaped

#### Sanity Check to visualize the system
def visualize_sys(input_matrix, color, title, figSize= (8, 8)):
    plt.figure(figsize = figSize)
    plt.imshow(X = input_matrix, cmap=color, interpolation='none', origin = 'lower')
    plt.colorbar()
    plt.xticks(np.linspace(0, input_matrix.shape[0]-1, input_matrix.shape[0]))
    plt.yticks(np.linspace(0, input_matrix.shape[1]-1, input_matrix.shape[1]))
    plt.xlim([0, input_matrix.shape[0]-1])
    plt.ylim([0, input_matrix.shape[1]-1])
    plt.title(title, fontsize = 12)
    plt.show()