### How to compile the code: 
- Code is in written Python and no compilation is necessary

### How to execute the code
- Update desired input values in `input_deck.py` then run the main method in `main.py`

### Status of the code
- Creation of averaged out matrices with edge/ corner cases works fully
- Population of A for inner points is commplete with boundary conditions

### System parameters and behavior:
- Currently the code (specifically the discretization process and A matrix creation) only works on square matricies (m = n where m > 2)

### General code framework:
1. Main Module: calls subroutines listed in specific sequence, prints execution time, and
terminates execution

2. Version data subroutine: writes code name, version number, author name, date and time of execution to an output file (perhaps also print to screen). Also writes out the source type that was used. This is performed upon termination and the information is written (appended) to the "output.txt" file. The output file is intended to serve as an archive of different scenarios that were carried out.

3. Input data subroutine: reads and processs the input data to (m-1) x (n-1) matrices. This routine checks that all input values for correctness/sensibility, e.g., all values are positive, array dimensions are correct, etc. Print an error message and terminate if one or more errors occur, otherwise print notification of successful input checking.

4. Input echo subroutine: prints the input data for each cell to the output file as a colormap to show the relationship of the value with respect to the whole system for the inputted diffusion coefficients, absorption cross sections, and source term.

5. Diffusion solver subroutine: implement the discretized diffusion solver here (iteratively). Upon execution prints “solving diffusion equation here”.