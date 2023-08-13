import torch
import plotly
import plotly.graph_objects as go


def create_prediciton_map(transform,
                          box = None,
                          nx = 500,
                          ny = 500):
    """
    :param transform: Function from (m, 2) -> (m)
    """
    if box is None:
        box = dict()
    if not 'x0' in box:
        box['x0'] = -2
    if not 'x1' in box:
        box['x1'] = 2
    if not 'y0' in box:
        box['y0'] = -2
    if not 'y1' in box:
        box['y1'] = 2

    x_axis = torch.linspace(box['x0'], box['x1'], nx)
    y_axis = torch.linspace(box['y0'], box['y1'], ny)
    Y, X = torch.meshgrid(y_axis, x_axis)
    points = torch.stack((X, Y)).reshape((2, -1)).T


    t_points = transform(points)

    Z = t_points.reshape((ny, nx))

    return Z, x_axis, y_axis


Z, x_axis, y_axis = create_prediciton_map(lambda x: torch.sin(5*x.pow(2).sum(1)),
                                          box={'x0' : -5})

fig = go.Figure(
    data = go.Heatmap(
        z = Z,
        x = x_axis,
        y = y_axis
    )
)

fig.show()