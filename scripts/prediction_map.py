import torch
import plotly

import plotly.graph_objects as go

box_x0 = -1.
box_y0 = 4.
box_x1 = 1.
box_y1 = -4.

nx = 500
ny = 1000

dx = (box_x1 - box_x0)/nx
dy = (box_y1 - box_y0)/ny

x_axis = torch.linspace(box_x0, box_x1, nx)
y_axis = torch.linspace(box_y0, box_y1, ny)
X, Y = torch.meshgrid((y_axis, x_axis))
points = torch.stack((X.flatten(), Y.flatten())).T
y_axis.shape
x_axis.shape
X.shape

# Z
# softmax = nn.Softmax(1)
# probs = softmax(model(points))[:, 0]
# probs
# Z = probs.reshape((nx, ny)).detach().numpy()


# m = nn.LogSoftmax(dim=0)
# input = torch.randn(2, 3)
# output = m(input)


Z = points.pow(2).sum(1).reshape((nx, ny)).T

fig = go.Figure(
    data = go.Heatmap(
        z = Z,
        x = x_axis,
        y = y_axis
    )
)
fig.show()

Z.shape
X.shape
