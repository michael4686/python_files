import numpy_1 as np
from sklearn_extra.cluster import KMedoids
import pandas as pd 
list1=pd.read_excel("D:\Book2.xlsx")
list1=pd.DataFrame(list1)
print(list1.isnull().sum())
list1=list1.dropna()
list1=list1.drop_duplicates()
print(list1.isnull().sum())
data=np.array(list1)
k=2
km=KMedoids(n_clusters=2).fit(list1)
print("clusters ",km.labels_)
print("clusters ",km.cluster_centers_)
for i in range(k):
    for j in range(len(data)):
        if(km.labels_[j]==i):
            x=data[j]
            print(i,":",x)