# a=[i for i in range(10)] #串列生成式
# b=(i for i in range(10)) #產生器表示式
# print(a) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(b) #<generator object <genexpr> at 0x0000026D60DE9A10> 備註:產生一個物件在記憶體位址中


#和串列相同，也可以使用類似 for 迴圈的方式取出產生器的值，但所有的值都只能取出一次，以下方的程式為例，如果是串列生成式
# # ，因為記憶體中保留了整份串列，所以再次取值時還是能得到數值，如果是使用產生器表示式，再次取值時，就完全取不到值。
# a=[i**2 for i in range(10)]
# for i in a:
#     print(i,end=' ') #0 1 4 9 16 25 36 49 64 81
# for i in a:
#     print(i,end=' ') #0 1 4 9 16 25 36 49 64 81
# print()
# b=(i**2 for i in range(10))
# for i in b:
#     print(i,end=' ') #0 1 4 9 16 25 36 49 64 81 
# for i in b:
#     print(i,end=' ') #取不到值

# a=(i**2 for i in range(10))
# print(next(a)) #0
# print(next(a)) #1
# print(next(a)) #4
# print(next(a)) #9
# print(next(a)) #16
# print(next(a)) #25
# print(next(a)) #36
# print(next(a)) #49
# print(next(a)) #64
# print(next(a)) #81
# print(next(a)) #發生錯誤，因為取不到值

#yield陳述式
# def f(max):
#     n=0
#     a=2
#     while n < max:
#         yield(a) #print換成yield
#         a=a**2
#         n=n+1
# f(5)

# def f():
#     yield(1) #使用yield
#     yield(2)
#     yield(3)
# g=f() #賦予值給變數g
# print(next(g)) #1
# print(next(g)) #2
# print(next(g)) #3

# def f():
#     yield(1) #使用yield
#     yield(2)
#     yield(3)
# print(next(f())) #1
# print(next(f())) #1
# print(next(f())) #1

# def f(max):
#     n=0
#     while n<max:
#         yield(n)
#         n=n+1
# g=f(10)
# a=[]
# b=[]
# for i in range(5):
#     a.append(next(g))
# for i in range(5):
#     b.append(next(g))
# print(a)
# print(b)

#使用產生器找質數
# a=range(2,100)
# print(*a)
# b=[i for i in a if i==a[0] or i%a[0]>0] #找出第一個質數(2的)，並將串列裡該質數的倍數剔除
# print(*b)
# c=[i for i in a if i==b[1] or i%b[1]>0] #找出第二個質數(3的)，並將串列裡該質數的倍數剔除
# print(*c)
# d=[i for i in a if i==c[2] or i%c[2]>0] #找出第三個質數(4的)，並將串列裡該質數的倍數剔除
# print(*d)

