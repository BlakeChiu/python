import pandas as pd
from sklearn import datasets
from jqmcvi import base
from sklearn import cluster 
#loading the dataset
X = datasets.load_iris()
df = pd.DataFrame(X.data)
 
#We store the clusters
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(df)
y_pred = k_means.predict(df)

prediction = pd.concat([df, pd.DataFrame(y_pred, columns=['pred'])], axis = 1)

clus0 = prediction.loc[prediction.pred == 0]
clus1 = prediction.loc[prediction.pred == 1]
clus2 = prediction.loc[prediction.pred == 2]
cluster_list = [clus0.values, clus1.values,clus2.values]
 
print(base.dunn(cluster_list))