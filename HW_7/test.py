import sklearn
from sklearn import datasets, preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import TruncatedSVD
import cv2
from sklearn.metrics.pairwise import euclidean_distances
sklearn.random.seed(42)
np.random.seed(42)

X = pd.read_csv('./IMDB_SMALL/train_X.csv') # 为了方便起见，这里只采用前6000个MNIST数据
y = pd.read_csv('./IMDB_SMALL/train_y.csv')
X, y = np.array(X), np.array(y)
X_std = StandardScaler().fit_transform(X)
model = PCA(n_components=2)
X_2d = model.fit_transform(X_std)
kmeans_std = KMeans(n_clusters=10, n_init=10)
y_std = kmeans_std.fit(X_2d)

kmeans_2d = KMeans(n_clusters=10, n_init=10)
y_2d = kmeans_2d.fit(X_2d)

fig,ax=plt.subplots(2,1,figsize=(10,20))
ax[0].scatter(X_2d[:, 0], X_2d[:, 1], c=y_2d)
ax[0].set_title('KMeans with X_2d',fontsize=20)
ax[1].scatter(X_2d[:, 0], X_2d[:, 1], c=y_std)
ax[1].set_title('KMeans with X_std',fontsize=20)
