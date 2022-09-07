#簡單函式
# def hello():
#     print('hello')
# hello()

#===================================

#函式參數
# def hello(msg):
#     print(msg)

# hello('hello')
# hello('good morning')

#===================================

# def hello(x,y):
#     z=x+y
#     print(z)

# hello(1,2) #3
# hello(5,6) #11

#===================================

#參數預設值
#如果執行函式時沒有提供參數數值，參數就會自動帶入預設值執行
# def hello(x,y=10):
#     z=x+y
#     print(z)

# hello(1,2) #3
# hello(5) #15

#===================================

#關鍵字引數
# def hello(name,age):
#     msg=f'{name} is {age} years old'
#     print(msg)

# hello('oxxo',18) #oxxo is 18 years old
# hello(18,'oxxo') #18 is oxxo years old (因為18和oxxo對調，所以結果就會對調)
# hello(age=18,name='oxxo') #oxxo is 18 years old(使用關鍵字引數，結果就會是正確的)

#===================================

# def test(a,*,start=0,end=3):
#     for i in a[start:end]:
#         print(i)

# b=[1,2,3,4,5]
# test(b,start=2,end=len(b)) #3 4 5
# test(b) #1 2 3

#===================================

#函式回傳值
# def a(x,y):
#     result=x + y*2
#     return result

# b=a(1,2)
# c=a(2,3)
# print(b) #5
# print(c) #8

#===================================

# def a(x):
#     result=0
#     while result < 10:
#         result=result+x
#         if result==5:
#             return result
#     return result

# b=a(1)
# c=a(2)
# print(b) #5
# print(c) #10

#===================================

# def test(x,y,z):
#     return x+1,y+1,z+1

# a,b,c=test(1,2,3) #賦值給「同樣數量」的變數
# print(a) #2
# print(b) #3
# print(c) #4

#===================================

#函式回傳的多個結果也可以只賦值給一個變數，這時就會將多個結果變成一個 tuple
# def test(x,y,z):
#     return x+1,y+1,z+1
# a=test(1,2,3)
# print(a) #(2, 3, 4)

#===================================

#函式內的函式
# def hello(n,msg):
#     def h1(): #內部函式
#         return msg
#     def h2(): #內部函式
#         return msg*2
#     if n==1:
#         print(h1())
#     if n==2:
#         print(h2())

# hello(1,'ok') #ok
# hello(2,'ok') #okok
# print(h2()) #錯誤 name 'h2' is not defined

#===================================

#函式內的變數
# a=123 #全域變數a
# b=123 #全域變數b
# def hello(msg):
#     a=msg #區域變數a，更動區域變數不影響全域變數
#     print(a)
#     global b #宣告變數b是使用全域變數b，更動變數等同更動全域變數
#     b=msg
# hello(456) #456
# print(a) #123
# print(b) #456

#===================================

# def hello(msg):
#     a=123
#     b=123
#     def h1():
#         nonlocal a #宣告a為自由變數
#         a=a+msg
#         print(a)
#     def h2():
#         b=b+msg
#         print(b)
#     h1() #579
#     h2() #錯誤 local variable 'b' referenced before assignment
# hello(456)

#===================================

#*args、**kwargs運算子
#如果把函式的參數設定帶有 args ( 一個星號 * ) 運算子的參數，則傳入的所有參數，都會被組合成 tuple 的型態，
# 下方的函式使用了「*args」的參數，執行函式時不論給予多少引數，最後都會組合成 tuple。
# def test(*args):
#     print(args)

# test(1,2,3,'a','b','c') #(1, 2, 3, 'a', 'b', 'c')

#===================================

#帶有 kwargs ( 兩個星號 ** ) 運算子的參數，則傳入的所有「帶有關鍵字引數」的參數，都會被組合成字典的型態
# def test(**kwargs):
#     print(kwargs)

# test(name='oxxo',age=18,like='book') #{'name': 'oxxo', 'age': 18, 'like': 'book'}

#===================================

# def a(*args,**kwargs):
#     print(args)
#     print(kwargs)

# a([123,456],x=1,y=2,z=3)
# #([123, 456],)
# #{'x': 1, 'y': 2, 'z': 3}

#===================================

#如果將一個星號套用在 print() 裡 ( print() 算是一個內建函式 )，就會將可迭代的物件打散後印出。
# a=[1,2,3,4,5]
# b=(1,2,3,4,5)
# c={'x':1,'y':2,'z':3}
# d={'x','y','z'}

# print(*a) #1 2 3 4 5
# print(*b) #1 2 3 4 5 
# print(*c) #x y z
# print(*d) #x y z

#===================================

#使用 pass
# def test():
#     pass

#===================================

a=int(input('>'))
if a>10:
    pass #如果輸入的數字大於10，不做任何事情
else:
    print(a)