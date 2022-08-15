
import os
import sys
import csv
import torch
import numpy

import matplotlib
from matplotlib import pyplot

from mpl_toolkits.axes_grid1 import AxesGrid

# Loading CSV files provided on the command line

if not os.path.exists('data.pt'):
    tags = []
    labels = []
    pairs = []
    X = {}
    Y = {}
    Z = {}
    for path in sys.argv[1:]:
        tag = path.split('_')[-1].split('.')[0] # expects: path = X_X_X_tag.X
        tags.append(tag)
        X.update({ tag : [] })
        Y.update({ tag : [] })
        Z.update({ tag : [] })
        print(path)
        with open(path) as F:
            for (k0, k1, sim) in csv.reader(F):
                t0 = k0.split('-')[0]
                t1 = k1.split('-')[0]

                X[tag].append(t0)
                Y[tag].append(t1)
                Z[tag].append(float(sim))

                labels.append(t0)
                labels.append(t1)
                pairs.append((t0,t1))

    labels = list(set(labels))
    rlabels = { lbl : i for (i,lbl) in enumerate(labels) }
    pairs = list(set(pairs))

    for tag in tags:
        X[tag] = numpy.array([ rlabels[lbl] for lbl in X[tag] ])
        Y[tag] = numpy.array([ rlabels[lbl] for lbl in Y[tag] ])
        Z[tag] = numpy.array(Z[tag])

    torch.save({
      'tags'   : tags,
      'labels' : labels,
      'pairs'  : pairs,
      'X' : X, 
      'Y' : Y,
      'Z' : Z
    }, 'data.pt')
else:
    data = torch.load('data.pt')
    tags   = data['tags']
    labels = data['labels']
    pairs  = data['pairs']
    X = data['X']
    Y = data['Y']
    Z = data['Z']

# Standardization

if not os.path.exists('norm.pt'):
    normZ = {}
    for tag in tags:
        T = Z[tag]
        T = T[T < 1.]
        zmean = T.mean()
        zstddev = T.std()
        normZ.update({ tag : (Z[tag] - zmean) / zstddev })

        zmin = normZ[tag].min()
        zmax = normZ[tag].max()
        normZ[tag] = (normZ[tag] - zmin) / (zmax - zmin)

    torch.save({
      'Z'   : normZ
    }, 'norm.pt')
else:
    norm = torch.load('norm.pt')
    normZ = norm['Z']

#######################
# Plotting
######################

# overwrite tags to force order
tags = [ 'distanceBase', 'codeBERT', 'POJ', 'DRB' ]
LBLs = [ 'cosine Similarity', 'CodeBERT(M1)', 'POJ(M2)', 'DRB(M3)' ]

matplotlib.rcParams.update({
  'image.cmap': 'RdBu_r'
})

if True: # both original and normalized
    fig = pyplot.figure(figsize=(16,8))
    grid = AxesGrid(
      fig, 111,
      nrows_ncols=(2, 4),
      axes_pad=0.05,
      share_all=True,
      label_mode="L",
      cbar_location="right",
      cbar_mode="single",
    )

    ims = []
    for (tag, lbl, ax) in zip(tags,LBLs,grid[0:4]):
        im = numpy.zeros(shape=(len(labels),len(labels)), dtype=numpy.float32)
        im[X[tag], Y[tag]] = Z[tag]
        ims.append(ax.imshow(im, vmin=0, vmax=1))
        ax.set_title(lbl)
    for (tag, lbl, ax) in zip(tags,LBLs,grid[4:8]):
        im = numpy.zeros(shape=(len(labels),len(labels)), dtype=numpy.float32)
        im[X[tag], Y[tag]] = normZ[tag]
        ims.append(ax.imshow(im, vmin=0, vmax=1))

    for cax in grid.cbar_axes:
        cax.toggle_label(False)
    grid.cbar_axes[0].colorbar(ims[-1])
    grid.cbar_axes[0].toggle_label(True)

    fig.savefig("all.png")
    #fig.show()

if True: # normalized only
    fig = pyplot.figure(figsize=(16,4))
    grid = AxesGrid(
      fig, 111,
      nrows_ncols=(1, 4),
      axes_pad=0.05,
      share_all=True,
      label_mode="L",
      cbar_location="right",
      cbar_mode="single",
    )

    ims = []
    for (tag, lbl, ax) in zip(tags,LBLs,grid):
        im = numpy.zeros(shape=(len(labels),len(labels)), dtype=numpy.float32)
        im[X[tag], Y[tag]] = normZ[tag]
        ims.append(ax.imshow(im, vmin=0, vmax=1))
        ax.set_title(lbl)

    for cax in grid.cbar_axes:
        cax.toggle_label(False)
    grid.cbar_axes[0].colorbar(ims[-1])
    grid.cbar_axes[0].toggle_label(True)

    fig.savefig("norm.png")
    #fig.show()

