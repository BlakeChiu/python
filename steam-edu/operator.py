#賦值運算子
# a='hello'
# b=123
# c=[1,2,3]

# a=3*(3+2)
# print(a) #15

# a=1 #a賦值1
# a=a+1 #a賦值1+1(此時右邊的a等於1)
# print(a) #2

# b=5 #b賦值5
# b=b-1 #b賦值5-1(此時右邊的b等於5)
# print(b)

# print(4**0.5) #2.0

#===================================
#比較運算子
# a=5
# b=3

# print(a<b) #False
# print(b<=a) #True
# print(a !=b) #True
# print(a==b) #False

#===================================

#邏輯運算子
# a=True
# b=False
# c=True

# print(a & b) #False
# print(a and b) #False
# print(a & c) #True
# print(a and c) #True

#===================================

# a=True
# b=False
# c=True

# print(a | b)  #True
# print(a or b) #True
# print(a | c)  #True
# print(a or c) #True

#===================================

# a=True
# b=False

# print(not a) #False
# print(not b) #True

#===================================

# a=1
# b=2
# c=3

# print((a>b)&(c>b)) #False
# print((a>b)|(c>b)) #True
# print(not ((a>b)&(c>b))) #True (因為(a>b)&(c>b)為False，而根據not語法會倒過來)

#===================================

#in與is運算子
#使用「in 運算子」可以判斷 b 是否包含 a，使用「is 運算子」可以判斷 a 和 b 是否為相同物件
# a=2
# b=4
# c=[1,2,3]
# print(a in c) #True
# print(b in c) #False

# x=[1,2,3]
# y=[1,2,3]
# z=x
# print(x is y) #False
# print(x is z) #True

#===================================

#位元運算子
# print(4&5) #4
# print(4|5) #5
# print(4^5) #1
# print(~4) #-5
# print(4>>2) #1
# print(5<<2) #20

#===================================

#跨列運算子
a=(1+2+3+
   4+5+6+
   7+8+9)

b=1+2+3+\
  4+5+6+\
  7+8+9

print(a) #45
print(b) #45