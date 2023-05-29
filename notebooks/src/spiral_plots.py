from typing import List, Dict, Optional
from plotly import graph_objects as go
import pandas as pd

def create_spiral_plot(spirals: List[pd.DataFrame], plot_radius:float, pad_factor:float=1.1, colors: Optional[List[str]] = None, fig = None):
    pad_factor= 1.1
    if colors is None:
        colors = [None]*len(spirals)
    if fig is None:
        fig = go.Figure()
    for s_i, spiral in enumerate(spirals):
        fig.add_trace(
            go.Scatter(x = spiral.x, y=spiral.y,
                    name= "Spirals", 
                    mode = 'markers',
                    marker = dict(
                        color = colors[s_i]
                    )
            )
        )

    fig.update_layout(
        autosize=False,
        width=500,
        height=500,
        xaxis = dict(
            range = [-pad_factor*plot_radius , pad_factor*plot_radius]
        ),
        yaxis = dict(
            range = [-pad_factor*plot_radius, pad_factor*plot_radius]
        ),
        margin=dict(
            l=40,
            r=0,
            b=40,
            t=0,
            pad=0
        ),
        paper_bgcolor="White",
    )

    return fig















