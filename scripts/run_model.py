from scripts.simple_model import Model
from scripts.spiral import Spiral
import numpy as np
import torch

spiral1 = Spiral(spiral_thickness=0.07)
data1: np.ndarray = spiral1.sample_normalized(1000)

spiral2 = Spiral(initial_angle=np.pi, spiral_thickness=0.07)
data2: np.ndarray = spiral2.sample_normalized(1000)
data = np.vstack((data1, data2), dtype=float)
data = torch.from_numpy(data)
data = data.to(torch.float32)

model = Model()
model(data)

torch.tensor([1,2.,3])






