import torch
import plotly
import plotly.graph_objects as go
        


def create_prediction_map(transform,
                          box_x0 = -1.,
                          box_y0 = 4.,
                          box_x1 = 1.,
                          box_y1 = -4.,
                          nx = 500,
                          ny = 1000
                          ):


    dx = (box_x1 - box_x0)/nx
    dy = (box_y1 - box_y0)/ny

    x_axis = torch.linspace(box_x0, box_x1, nx)
    y_axis = torch.linspace(box_y0, box_y1, ny)
    Y, X = torch.meshgrid((y_axis, x_axis))
    points = torch.stack((X, Y))
    
    Z = transform(torch.stack(X,Y))

    fig = go.Figure(
        data = go.Heatmap(
            z = Z,
            x = x_axis,
            y = y_axis
        )
    )
