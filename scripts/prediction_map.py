import torch
import plotly
import plotly.graph_objects as go



box_x0 = -3.
box_y0 = 4.
box_x1 = 3.
box_y1 = -4.
nx = 500
ny = 1000


x_axis = torch.linspace(box_x0, box_x1, nx)
y_axis = torch.linspace(box_y0, box_y1, ny)
Y, X = torch.meshgrid(y_axis, x_axis)
points = torch.stack((X, Y)).reshape((2, -1)).T

transform = lambda x: x.pow(2).sum(1)

t_points = transform(points)

Z = t_points.reshape((ny, nx))

fig = go.Figure(
    data = go.Heatmap(
        z = Z,
        x = x_axis,
        y = y_axis
     )
)
fig.show()

