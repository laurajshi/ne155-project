#pasting in code from noteboook to encapsulate processes
import scipy as sc
from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

# Set some parameters for plotting
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (12, 9)
plt.rcParams['font.size'] = 16

def tester():
    print('hello world')
    
def getGridSpacing(n, m, x_first=1, y_first=1, x_spacing_alt=1, y_spacing_alt=1):
    # Spacing can alternate between the first value and first*spacing_alt
    delta = np.ones(m-1)*x_first
    delta[1::2] = delta[1::2]*x_spacing_alt
    eps = np.ones(n-1)*y_first
    eps[1::2] = eps[1::2]*y_spacing_alt
    return eps, delta

def getMatrices(n, m, D_default, Sigma_def, Source_def, splitval, diff_fact):
    D = np.ones((n-1, m-1))*D_def #diffusion coeffient grid, initialize all to 10
    D[:, :splitval] = D[:, :splitval]*diff_fact #left regime

    Sigma_a = np.ones((n-1, m-1))*Sigma_def
    Sigma_a[:, :splitval] = Sigma_a[:, :splitval]*diff_fact

    Source = np.ones((n-1, m-1))*Source_def
    Source[:, :splitval] = Source[:, :splitval]*diff_fact
    return D, Sigma_a, Source