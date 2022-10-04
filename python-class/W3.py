import pandas as pd
import numpy as np


housing=pd.read_csv("housing.csv")
housing.info()

print(housing.describe())
print(housing["ocean_proximity"].value_counts())

#matplotlib inline
import matplotlib.pyplot as plt
housing.hist(bins=50,figsize=(20,15))
plt.show()

housing["income_cat"]=pd.cut(housing["median_income"],
                             bins=[0.,1.5,3.0,4.5,6.,np.inf],
                             labels=[1,2,3,4,5])


from sklearn.model_selection import StratifiedShuffleSplit

                        