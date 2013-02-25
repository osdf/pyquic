import py_quic
import numpy as np


def quic(S, L, mode="default", tol=1e-6, max_iter=1000, X0=None, W0=None,\
        path=None, msg=0):
    """
    @param S        The empirical nxn covariance matrix.

    @param L        Regularization parameters per element of the inverse
                    covariance matrix. Can be a scalar or nxn matrix.

    @param mode     Computation mode: one of "default", "path", "trace".

    @param tol      Convergence threshold.

    @param max_iter Maximum number of Newton iterations.

    @param X0       Initial guess for the inverse covariance matrix. If
                    not provided, the diagonal identity matrix is used.

    @param W0       Initial guess for the covariance matrix. If not provided
                    the diagonal identity matrix is used.

    @param path     In "path" mode, an array of float values for scaling L.

    @param msg      Verbosity level.
    """

    assert mode in ["default", "path", "trace"], "QUIC:arguments\n" +\
        "Invalid mode, use: 'default', 'path' or 'trace'."

    # Empircal covariance matrix S
    Sn, Sm = S.shape
    #assert S.dtype is np.float64, "QUIC:type\n" +\
    #        "Expected a double covariance matrix S."
    assert Sn==Sm, "QUIC:dimensions\n" +\
            "Expected a square empircal covariance matrix S."

    # Regularization parameter matrix L
    if type(L) is float:
        _L = np.empty((Sn, Sm))
        _L[:] = L
    else:
        Ln, Lm = L.shape
        assert (Ln==Sn) and (Lm==Sn), "QUIC:dimensions\n" +\
                "The regularization parameter L is not a scalar or a matching matrix."
        assert L.dtype is np.float64, "QUIC:type\n" +\
            "Expected a double regularization parameter matrix L."
        _L = L
 
    # Path
    if mode is "path":
        assert path is not None, "QUIC:dimensions\n" +\
                "Please specify the path scaling values."
        #assert (type(path) is np.ndarray) and (path.dtype is np.float64), "QUIC:type\n" +\
        #        "Expected a double array for path."
        pathLen = path.shape[0]
    else:
        path = np.empty(1)
        pathLen = 1

    if X0 is None:
        assert W0 is None, "QUIC:initializations\n" +\
                "You specified an initial value for W0 but not for X0."
        if mode is "path":
            # Note here: memory layout is important:
            # a row of X/W holds a flattened Sn x Sn matrix,
            # one row for every element in _path_.
            X = np.empty((pathLen, Sn*Sn))
            X[0,:] = np.eye(Sn).ravel()
            W = np.empty((pathLen, Sn*Sn))
            W[0,:] = np.eye(Sn).ravel()
        else:
            X = np.eye(Sn)
            W = np.eye(Sn)
    else:
        assert W0 is not None, "QUIC:initializations\n" +\
                "You specified an initial value for X0 but not for W0."

        assert X0.dtype is np.float64, "QUIC:type\n" +\
            "Expected a double initial inverse covariance matrix X0."

        assert W0.dtype is np.float64, "QUIC:type\n" +\
            "Expected a double initial covariance matrix W0."

        X0n, X0m = X0.shape
        assert (X0n==Sn) and (X0m==Sn), "QUIC:dimensions\n" +\
                "Matrix dimensions should match for initial inverse covariance matrix X0."

        W0n, W0m = W0.shape
        assert (W0n==Sn) and (W0m==Sn), "QUIC:dimensions\n" +\
                "Matrix dimensions should match for initial covariance matrix W0"

        if mode is "path":
            # See note above wrt memory layout
            X = np.empty((pathLen, Sn*Sn))
            X[0,:] = X0.ravel()
            W = np.empty((pathLen, Sn*Sn))
            W[0,:] = W0.ravel()
        else:
            X = np.empty(X0.shape)
            X[:] = X0
            W = np.empty(W0.shape)
            W[:] = W0
    

    if mode is "path":
        optSize = pathLen
        iterSize = pathLen
    elif mode is "trace":
        optSize = max_iter
        iterSize = 1
    else:
        optSize = 1
        iterSize = 1

    opt = np.zeros(optSize)
    cputime = np.zeros(optSize)
    dGap = np.zeros(optSize)
    iters = np.zeros(iterSize, dtype=np.uint32)

    py_quic.quic(mode, Sn, S, _L, pathLen, path, tol, msg, max_iter,\
            X, W, opt, cputime, iters, dGap)

    if optSize == 1:
        opt = opt[0]
        cputime = cputime[0]
        dGap = dGap[0]

    if iterSize == 1:
        iters = iters[0]

    return X, W, opt, cputime, iters, dGap
