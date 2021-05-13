#INPUT DECK, but in values for absorption cross section, diffusion coefficient, source term
#outputs the matrices of interest
from de_methods import *
import numpy as np

# These are the number of edge points on which we will have the flux values
n = 20 #number of rows
m = 20 #number of columns
sourcetype = 'point'


# Spacing can alternate between the first value and first*spacing_alt
x_first, y_first = 1, 1
x_spacing_alt, y_spacing_alt = 1, 1 #when set to 1, all spacing is uniform

D_default = 10; Sigma_def = 100; Source_def = 10

### getters and setters
def getSysDims():
    return m, n

def getSourceType():
    return sourcetype

def getSpacingArrays(check=True):
    if (check):
        if (m> 1 and n> 1 and x_first > 0 and y_first > 0):
            print('all spacing inputs are valid, proceeding.')
        else:
            print('spacing inputs are not valid, terminating. check to make sure all inputs are positive')
            return
    delta = np.ones(m-1)*x_first
    delta[1::2] = delta[1::2]*x_spacing_alt
    eps = np.ones(n-1)*y_first
    eps[1::2] = eps[1::2]*y_spacing_alt
    return delta, eps

def getMatricesFromInput(show=True, check=True):
    sourceT = sourcetype
    if (check):
        if not(D_default > 1 and Sigma_def > 1 and Source_def > 1):
            print('material inputs are not valid, terminating. check to make sure all inputs are positive.')
            return
        if not(sourcetype in ['point', 'line', 'corner', 'divided']):
            print('source type is invalid, should be a point, line, corner, or divided')
            print('will default to a point source')
            sourceT = 'point'
        else:
            print('all inputs are valid, proceeding')
            
    Dc = createDividedMatrix(n, m, D_default, division = 2, vert= True) #False
    Sigma_a = createDividedMatrix(n, m, Sigma_def,  division = 2, vert= True)
    
    if (sourceT=='point'):
        Source = createPointMatrix(n, m, Source_def)

    if (sourceT == 'line'):
        Source = createLineMatrix(n, m, Source_def)

    if (sourceT == 'divided'):
        Source = createDividedMatrix(n, m, Source_def)

    if (sourceT == 'corner'):
        Source = createCornerMatrix(n, m, Source_def)
    if (show):
        visualize_sys_orig(Dc, Sigma_a, Source)
    print('Displaying input values as graphs, please verify')
    return Dc, Sigma_a, Source

def visualize_sys_orig(Dc, Sigma_a, Source):
    fig, (ax1, ax2, ax3) = plt.subplots(1,3)
    fig.suptitle('Input Value Plots')
    one = ax1.imshow(X = Dc, cmap='Greens', interpolation='none', origin = 'lower')
    ax1.set_title('Diffusion Coefficients', fontsize = 12)
    
    two = ax2.imshow(X = Sigma_a, cmap='Reds', interpolation='none', origin = 'lower')
    ax2.set_title('Absorption Coefficients', fontsize = 12)
    
    three = ax3.imshow(X = Source, cmap='Blues', interpolation='none', origin = 'lower')
    ax3.set_title('Source Term', fontsize = 12)

    fig.colorbar(one, ax = ax1, shrink=0.35)
    fig.colorbar(two, ax = ax2, shrink=0.35)
    fig.colorbar(three, ax = ax3, shrink=0.35)
    ax1.set_xlim([0, Dc.shape[0]-1]); ax1.set_ylim([0, Dc.shape[1]-1])
    ax2.set_xlim([0, Sigma_a.shape[0]-1]); ax2.set_ylim([0, Sigma_a.shape[1]-1])
    ax3.set_xlim([0, Source.shape[0]-1]); ax3.set_ylim([0, Source.shape[1]-1])
    plt.show()