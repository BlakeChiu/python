#int(x, base)
# a=int('123')
# b=int(123.999)
# c=int()
# d=int(True)
# e=int(False)
# print(a) #123
# print(b) #123
# print(c) #0
# print(d) #1
# print(e) #0

#======================================

# a=int('123')
# b=int('123',base=8)
# c=int('123',base=16)
# print(a) #123
# print(b) #83 ，123 等於 83的八進位
# print(c) #291 ，123 等於 291的十六進位

#======================================

#float(x)
# a=float('123')
# b=float(123)
# c=float()
# d=int(True)
# e=int(False)
# print(a) #123.0
# print(b) #123.0
# print(c) #0.0
# print(d) #1
# print(e) #0

#======================================

# Python 裡表現「無窮大」或「NaN ( 非數字 )」的數值，可以使用「float(inf)」或「float(nan)」的做法
# a=float('inf')
# b=float('-inf')
# c=float('nan')
# print(a) #inf 正無窮大
# print(b) #-inf 負無窮大
# print(c) #nan 正無窮大

#======================================

#abs(x)
# a=abs(-123)
# print(a) #123

#======================================

#divmod(x, y)
# a=divmod(5,3)
# b=divmod(9,2)
# print(a) #(1,2)
# print(b) #(4,1)

#======================================

#max(iter)
# a=max('100200300')
# b=max([100,200,300])
# c=max((100,200,300))
# print(a) #3(因為字串拆開後只有0 1 2 3)
# print(b) #300
# print(c) #300

#======================================

#min(iter)
# a=min('100200300')
# b=min([100,200,300])
# c=min((100,200,300))
# print(a) #0(因為字串拆開後只有0 1 2 3)
# print(b) #100
# print(c) #100

#======================================

#pow(x, y, z)
# a=pow(2,3)
# b=pow(2,3,3)
# print(a) #8(2的3次方)
# print(b) #2(8除以3的餘數)

#======================================

#round(x, y)
# a=round(3.14159)
# b=round(3.14159,3)
# print(a) #3
# print(b) #3.142

#======================================

#不過需要特別注意的是，當遇到 .5 的數值時容易出現問題，因為 .5 的數字其實是 .44444444X 或 .5000000X 之類的數字，這時使用 round() 會發生預期外的狀況
# print(round(1.5)) #2
# print(round(2.5)) #2(因為2.5不是真正的2.5)
# print(round(3.5)) #4
# print(round(4.5)) #4(因為4.5不是真正的4.5)
# print(round(5.5)) #6

#======================================

#sum(iter, y)
# a=sum([1,2,3,4])
# b=sum((1,2,3,4))
# c=sum((1,2,3,4),5)
# print(a) #10
# print(b) #10
# print(c) #15(最後再加上5)

#======================================

#complex(x, y)
# a=complex(1,2)
# print(a) #(1+2j)

#======================================

#bool(x)
a=bool(1)
b=bool(0)
c=bool()
d=bool(999)
e=bool('hello')
f=bool([0])
g=bool([])
print(a) #True
print(b) #False
print(c) #False
print(d) #True
print(e) #True
print(f) #True
print(g) #False