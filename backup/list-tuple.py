# grades=[12,60,15,70,90] 
# grades=grades+[12,33] #列表串接
# grades[1:4]=[] #刪除列表中從編號1到4(但不包含4)的資料
# length=len(grades) #取得列表的長度len(列表資料)
# print(length)

# data=[[3,4,5],[6,7,8]]
# print(data)
# data[0][0:2]=[5,5,5] #replace[3,4]換成[5,5,5]
# print(data)

data=(3,4,5)
data[0]=5 #錯誤:Tuple資料不可變動
print(data)