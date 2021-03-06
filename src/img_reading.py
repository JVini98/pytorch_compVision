import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
from torchvision.transforms import ToTensor


data_train = torchvision.datasets.MNIST('./data',
    download=True,
    train=True,
    transform=ToTensor())
data_test = torchvision.datasets.MNIST('./data',
    download=True,
    train=False,
    transform=ToTensor())

print('Training samples:',len(data_train))
print('Test samples:',len(data_test))

print('Tensor size:',data_train[0][0].size())
print('First 10 digits are:', [data_train[i][1] for i in range(10)])

fig,ax = plt.subplots(1,7)
for i in range(7):
    ax[i].imshow(data_train[i][0].view(28,28))
    ax[i].set_title(data_train[i][1])
    ax[i].axis('off')
plt.show()