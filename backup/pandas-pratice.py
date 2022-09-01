import pandas as pd

# data=pd.Series([20,10,15])
# print(data)
# print("Max:",data.max())
# print("Median",data.median())
# data=data*2
# print(data)
# data=data==20
# print(data)

#建立DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
})
#建立DataFrame操作
# print(data)
# print(data["salary"]) #取得特定的欄位
print(data)
print("--------------")
print(data.iloc[1]) #取得特定的列


