#基本遞歸
def a(n):
    if n==0 or n==1:
        return 1
    else:
        return n+a(n-1) #使用遞歸
print(a(3))

#n階乘
# def a(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*a(n-1) #使用遞歸
# print(a(4))

#費波那契數列
# def fib(n):                         #建立函式fib，帶有參數n
#     if n > 1:                       #如果n大於1
#         return fib(n-1)+fib(n-2)    #使用遞歸
#     return n
# for i in range(20):                 #產生20個數字
#     print(fib(i),end=',')           #0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181

#最大公因數
# def f(a,b):
#     if a%b==0:
#         return b
#     else:
#         return f(b,a%b)
# print(f(456,48))