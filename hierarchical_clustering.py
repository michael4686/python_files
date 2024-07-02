import numpy_1 as np
import matplotlib.pyplot as plt
import seaborn as sns
X1 = np.array([[1,1], [3,2], [9,1], [3,7], [7,2], [9,7], [4,8], [8,3],[1,4]])
print(X1)

plt.figure(figsize=(6, 6))
plt.scatter(X1[:,0], X1[:,1], c='r')
# Create numbered Labels for each point
for i in range(X1.shape[0]):
    plt.annotate(str(i), xy=(X1[i,0], X1[i,1]), xytext=(3, 3), textcoords='offset points')
plt.xlabel('x coordinate' )
plt.ylabel('y coordinate' )
plt.title('Scatter Plot of the data')
plt.xlim([0,10]), plt.ylim([0,10])
plt.xticks(range(10)), plt.yticks(range(10) )
plt.grid()
plt.show()

from scipy.cluster.hierarchy import dendrogram, linkage
Z1 = linkage(X1, method='single', metric='euclidean' )
Z2 = linkage(X1, method='complete', metric='euclidean' )
Z3 = linkage(X1, method='average', metric='euclidean' )
Z4 = linkage(X1, method='ward', metric='euclidean' )  

plt.figure(figsize=(15, 10))
plt.subplot(2,2,1), dendrogram(Z1), plt.title( 'Single' )
plt.subplot(2,2,2), dendrogram(Z2), plt.title( 'Complete' )
plt.subplot(2,2,3), dendrogram(Z3), plt.title( 'Average')
plt.subplot(2,2,4), dendrogram(Z4), plt.title( 'Ward' )
plt.show()

from scipy.cluster.hierarchy import fcluster
f1 = fcluster(Z1, 2) # 2 no. of dimantion
# f1 = fcluster(Z1, 2, criterton='maxclust') # criterion to Finds a minimum
print(f"Clusters: {f1}")


# other way 
from sklearn.cluster import AgglomerativeClustering
Z1 = AgglomerativeClustering(n_clusters=1, linkage='single' )
Z1.fit_predict(X1)
print(Z1.labels_)
fig, ax = plt.subplots(figsize=(6, 6))
scatter = ax.scatter(X1[:,0], X1[:,1], c=Z1.labels_, cmap='rainbow' )
legend = ax.legend(*scatter.legend_elements(), title="Clusters", bbox_to_anchor=(1, 1))
ax.add_artist (legend)
plt.title('Scatter plot of clusters')
plt.show()

import pandas as pd
#The data stored online
df = pd.read_csv('https://raw.githubusercontent.com/LearnDataSci/glossary/main/data/protein.csv')
print(df.head())
X2 = df.iloc[:,1:10]
print(X2.head())
Z2 = linkage(X2, method='single', metric='euclidean' )
labelList = list(df['Country'])
plt.figure(figsize=(13, 12))
dendrogram (
Z2,
orientation='right',
labels=labelList,
distance_sort='descending',
leaf_font_size=16
)
plt.show()
df['Clusters'] = fcluster(Z2, 2)
print(df)