import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.io import savemat

log = True


def writeMat(data):
    imgs = int(np.maximum(data[:, 0].max(), data[:, 1].max()))

    img = np.zeros((imgs + 2, imgs + 2), dtype=np.bool)
    for row in data:
        if np.abs(row[0] - row[1]) >= 20:
            img[int(row[0]), int(row[1])] = True

    savemat("gt.mat", {"truth": img.transpose()})


def plot(data):
    imgs = int(np.maximum(data[:, 0].max(), data[:, 1].max()))

    img = np.zeros((imgs + 1, imgs + 1), dtype=np.float32)
    for row in data:
        img[int(row[0]), int(row[1])] = row[2]

    img[img < 10] = 0
    if log:
        # plt.matshow(img, norm=LogNorm())
        plt.imshow(img, norm=LogNorm())
    else:
        plt.imshow(img)
    plt.colorbar()


data1 = np.genfromtxt('sim.csv', delimiter=',')
# data1 = np.genfromtxt(
#     '/home/lars/gitProjects/MILD/build/output/full/gt.csv',
#     delimiter=','
# )
# writeMat(data1)
# plt.subplot(121)
plot(data1)
plt.show()

# data2 = np.genfromtxt('bayes.csv', delimiter=',')
# plt.subplot(122)
# plot(data2)
# plt.show()
