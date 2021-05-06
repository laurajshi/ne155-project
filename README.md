### How to compile the code: 
- Ideally will be done in Python so now compilation needed or written in Java and compiled with javac/ IntelliJ IDE


### How to execute the code

### Status of the code
- Creation of averaged out matrices with edge/ corner cases works fully
- Right now, population of A matrix for inner points needs to be tweaked
- Also need to add information about boundary conditions

### System parameters and behavior:
- expected input, resulting output, limitations/ restrictions

### General code framework:
1. Main Module: calls subroutines listed in specific sequence, prints execution time, and
terminates execution


2. Version data subroutine: write code name, version number, author name, date andtime of execution to an output file (perhaps also print to screen).

3. Input data subroutine: read and/or process the input data. Check all input values for correctness/sensibility, e.g., all values are positive, array dimensions are correct, etc. Print an error message and terminate if one or more errors occur, otherwise print notification of successful input checking.

4. Input echo subroutine: print the input data for each cell to the output file (this is good for reproducibility). Please format this in some useful way.

5. Diffusion solver subroutine: implement the discretized diffusion solver here. While building the surrounding structure you can just have this print “will solve DE here”.