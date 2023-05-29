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


def f_between_vectors(v1, v2, f, num_points, pad_factor = 0):
    thetas = np.linspace(0-pad_factor, 1 + pad_factor, num_points)
    values = np.zeros((num_points,), dtype = float)
    for i, theta in enumerate(thetas):
        v = theta*v1+(1-theta)*v2
        values[i] = f(v)
    return v





