Summary
=======

A python wrapper for [QUIC](http://www.cs.utexas.edu/~sustik/QUIC/),
computing a sparse inverse covariance matrix estimation using quadratic 
approximation. It is based on Version 1.2 of the [QUIC](http://www.cs.utexas.edu/~sustik/QUIC/) code. 
The wrapper was  successfully tested on OSX (10.6), Ubuntu (11.04) and Arch Linux.

The modifications to the original C++ source (from the above website) are minimal:
See the diff for the second overall commit.

Requirements
------------

* [numpy](numpy.scipy.org)
* [cython](cython.org)
* [lapack](http://www.netlib.org/lapack/). Tested version is 3.4.1 (not necessary for OSX).


Building
--------
In the directory```py_quic/```, run ```make```. Make sure that your lapack library is available.
If necessary, add ```library_dirs``` in ```py_quic/setup.py```.


Testing
-------
For testing the algorithm, run ```python test.py``` after a successful build. Note that
the file ```ER_692.mat``` has to be in the main directory. It is contained in the
MEX package archive from the [QUIC](http://www.cs.utexas.edu/~sustik/QUIC/).

More Information
----------------
See *Sparse Inverse Covariance Matrix Estimation Using Quadratic Approximation* by
Cho-Jui Hsieh, Mátyás A. Sustik, Inderjit S. Dhillon, Pradeep Ravikumar, available
on the [QUIC](http://www.cs.utexas.edu/~sustik/QUIC/) website.
