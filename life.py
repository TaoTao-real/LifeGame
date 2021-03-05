'''
Author: your name
Date: 2020-10-15 15:17:17
LastEditTime: 2021-03-05 15:56:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/lifeGame/life.py
'''
import numpy as np
import  matplotlib.pyplot as plt

def iterate(Z):
    # count the neighbors of every inner cell
    N = (Z[0:-2, 0:-2] + Z[0:-2, 1:-1] + Z[0:-2, 2:] +
         Z[1:-1, 0:-2]                 + Z[1:-1, 2:] +
         Z[2:  , 0:-2] + Z[2:  , 1:-1] + Z[2:  , 2:])

    # change the cell status
    birth = (N == 3) & (Z[1:-1, 1:-1] == 0)
    survive = ((N == 2) | (N == 3)) & (Z[1:-1, 1:-1] == 1)
    Z[...] = 0
    Z[1:-1, 1:-1][birth | survive] = 1
    return Z

Z = np.random.randint(0,2,(256,512))

plt.ion()
size = np.array(Z.shape)
dpi = 72.0
figsize = size[1] / float(dpi), size[0] / float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi, facecolor="white")
fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)

for i in range(100): 
    iterate(Z)
    plt.imshow(Z, interpolation='nearest', cmap=plt.cm.gray_r)
    plt.xticks([]), plt.yticks([])
    plt.pause(0.1)
    fig.clf()

plt.ioff()