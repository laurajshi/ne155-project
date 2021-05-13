# Main module for diffusion solver project
# Version 2.0
from datetime import datetime
from input_deck import *
from de_methods import *
from discretize_eq import *
from iterative_solve import *

#get system matrices from input deck
sourcetype = getSourceType()
m, n = getSysDims()
delta, eps = getSpacingArrays()
D_c, Sigma_a, Source = getMatricesFromInput(show=True)

#get averaged values for an (n x m system)
Sigma_av = make_av_matrix(Sigma_a, eps, delta)
Source_av = make_av_matrix(Source, eps, delta)
Source_av = applySourceBC(Source_av) #apply BCs to the left and bottom edges

visualize_sys(Sigma_av, 'Reds', 'Absorption Cross Section Averaged')
visualize_sys(Source_av, 'Blues', 'Source Term Averaged with Boundary Conditions')

#build the A matrix, currently only works for a square system
A_matrix = buildFullA(m)
print("verifying the shape of the A matrix, should be n**2 x n**2", A_matrix.shape)
#build the b vector
Source_solve = reshape_source(Source_av)

#solve the system!
print("solving the system!")
x0 = np.zeros(m*m) 
tol = 10**(-6)
flux_sols_GS, err, count = performIteration(A_matrix, Source_solve, x0, tol, gs)
#print('solution vector GS:', flux_sols_GS)
print('iteration count:', count)
print('error:', err)


#output results of the flux
flux_solve = flux_sols_GS
flux_array = flux_solve.reshape(m, n)
# visualizing the flux of the system
visualize_sys(flux_array, 'Reds', 'Corresponding Flux Values for the System')


##write output with version data
with open('output.txt', 'a') as file:
    file.write('**** diffusion equation solver 2.1 with %s source, author = laurashi ****\n' %sourcetype)
    file.write('Terminated at: %s\n'  %datetime.now())
    file.write('Flux Output:\n')
    np.savetxt(file, flux_array, fmt='%1.2e')
file.close()
print('diffusion equation 2.0 terminated, author = laurashi at:', datetime.now())