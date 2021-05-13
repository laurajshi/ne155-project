from datetime import datetime
import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)
# file1 = open('output.txt', 'w')
# file1.write('diffusion equation 2.0, author = laurashi,\nterminated at:')
# s = datetime.now()
# file1.write(s)
# file1.write(A)
# file1.close()
# print('diffusion equation 2.0 terminated, author = laurashi at:', datetime.now())

with open('output.txt', 'w') as file:
    file.write('Recorded at: %s\n'  %datetime.now())
    np.savetxt(file, A, fmt='%1.2e')
    # for row in A:
    #     np.savetxt(file, row, fmt='%1.2e')
file.close()
#file.close()