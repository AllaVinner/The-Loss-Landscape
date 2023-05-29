import numpy as np



def create_heatmap(x, y, f, f_is_vectorized = True):
    if f_is_vectorized:
        X, Y = np.meshgrid(x, y)
        Z = f(X,Y)
    else:
        Z = np.zeros((len(y), len(x)), dtype = float)
        for i, x_val in enumerate(x):
            for j, y_val in enumerate(y):
                Z[j, i] = f(x_val, y_val)
    return Z