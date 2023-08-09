from scripts.simple_model import Model, Model2
from scripts.spiral import Spiral
import numpy as np
import torch
from torch import nn 
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
from itertools import chain
import importlib
import scripts.simple_model
importlib.reload(scripts.simple_model)

n = 100000

spiral1 = Spiral(spiral_thickness=0.07)
data1: np.ndarray = spiral1.sample_normalized(n)

spiral2 = Spiral(initial_angle=np.pi, spiral_thickness=0.07)
data2: np.ndarray = spiral2.sample_normalized(n)
data = np.vstack((data1, data2), dtype=float)
data = torch.from_numpy(data)
data = data.to(torch.float32)

labels = torch.from_numpy(np.hstack((np.zeros(n, dtype=int), np.ones(n, dtype=int)))).to(torch.long)
dataset = list(zip(data, labels))

# Create dataloader
dataloader = DataLoader(dataset, batch_size=256, shuffle=True)

model = Model2()


# Define loss function
loss_fn = nn.CrossEntropyLoss()
# Define optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

# Define training schedule
def train(dataloader, model, loss_fn, optimizer):
    model.train()
    for batch_i, (points, labels) in enumerate(dataloader):
        pred = model(points)
        loss = loss_fn(pred, labels)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if batch_i % 50 == 0:
            print(f"batch {batch_i}, loss {loss.item()}")
    print(loss.item())

train(dataloader, model, loss_fn, optimizer)
#train(dataloader, model, loss_fn, optimizer)




