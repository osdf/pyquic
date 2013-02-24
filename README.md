Summary
=======

A python wrapper for [QUIC](http://www.cs.utexas.edu/~sustik/QUIC/),
computing a sparse inverse covariance matrix estimation using quadratic 
approximation. It is based on Version 1.1 of the QUIC software. The wrapper was 
successfully tested on OSX (10.6), Ubuntu (11.04) and Arch Linux.

The modifications to the original C++ source (from the above website) are minimal:
See the diff for the second overall commit.

Requirements
------------

* [numpy](numpy.scipy.org)
* [cython](cython.org)
* [lapack](http://www.netlib.org/lapack/). Tested version is 3.4.1 (not necessary for OSX).


More Information
----------------
See *Sparse Inverse Covariance Matrix Estimation Using Quadratic Approximation* by
Cho-Jui Hsieh, Mátyás A. Sustik, Inderjit S. Dhillon, Pradeep Ravikumar.
