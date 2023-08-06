import numpy as np
from scripts import spiral
from scripts.spiral import Spiral
from scripts.spiral_plots import create_spiral_plot
import plotly
import pandas as pd
import os
import plotly.graph_objects as go

spiral1 = Spiral(spiral_thickness=0.07)
data1: np.ndarray = spiral1.sample_normalized(1000)
df1 = pd.DataFrame(data = {'x': data1[:,0], 'y': data1[:,1]})

spiral2 = Spiral(initial_angle=np.pi, spiral_thickness=0.07)
data2: np.ndarray = spiral2.sample_normalized(1000)
df2 = pd.DataFrame(data = {'x': data2[:,0], 'y': data2[:,1]})

fig = go.Figure()
fig = create_spiral_plot([df1, df2],2.)
fig.show()





