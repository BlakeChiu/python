#建立tuple
# a=('apple','banana','orange','grap')
# b=('apple',)
# print(type(a))
# print(type(b))

#=========================================

#tuple(串列)
# a=['apple','banana','orange','grap']
# b=tuple(a)
# print(b) #('apple', 'banana', 'orange', 'grap')

#=========================================

#讀取 tuple 的內容
# t=('apple','banana','orange','grap')
# a,b,c,d=t
# print(a) #apple
# print(b) #banana
# print(c) #orange
# print(d) #grap

#=========================================

# t1=('apple','banana','orange')
# t2=('grap','pineapple')
# t=t1+t2
# print(t) #('apple', 'banana', 'orange', 'grap', 'pineapple')

#=========================================

#使用*號重複項目
# a=('apple','banana','orange')
# b=a*3
# print(b) #('apple', 'banana', 'orange', 'apple', 'banana', 'orange', 'apple', 'banana', 'orange')

#=========================================

#強制修改 tuple 
a=('apple','banana','orange')
b=list(a)
b.append('grpe')
a=tuple(b)
print(a) #('apple', 'banana', 'orange', 'grpe')