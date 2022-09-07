# a=1
# b=2
# c=3
# if a<b and a<c:
#     print('ok1') #ok1
# if a<b or a>c:
#     print('ok2') #ok2

#=============================================

#越左方 ( 越前方 ) 會越先判斷，逐步往右邊判斷。
# a=2
# b=3
# c=0
# if a>b or a<c or a==2:
#     print('ok1') #印出 ok1

#=============================================

#如果同時有 and 和 or，則會先判斷 and，然後再接著從左向右判斷
# a=2
# b=3
# c=0
# if a>b or a<c or a==2 and b==4: #效果等同(a>b or a<c) or (a==2 and b==4)
#     print('ok1')
# else:
#     print('XXX') #印出XXX

#=============================================

#下方的例子也會先判斷 and，然後再接著從左向右判斷
# a=2
# b=3
# c=0
# if a>b or a<c and a==2 or b==4: #效果等同(a>b or (a<c and a==2)) or b==4
#     print('ok1')
# else:
#     print('XXX') #印出XXX

#=============================================

# a=1 and 2 and 3
# print(a) #3，全部都True，所以回傳最右邊的值

# b=1 and 0 and 2
# print(b) #0，遇到0(False)，回傳第一個False的值就是0

# c=1 or 2 or 3
# print(c) #1，全部都True，所以回傳第一個值

# d=1 or 0 or 3
# print(c) #1，遇到0(False)，回傳第一個True的值就是1

# e=1 and 2 or 3
# print(e) #2，效果等同1 and (2 or 3)

# f1=1 or 2 and 3
# print(f1) #1，效果等同1 or (2 and 3)，2和3先取出3，之後變成1 or 3

# g=1 and 2 or 3 and 4 or 5
# print(g) #2，效果等同1 and(2 or (3 and(4 or 5)))

#=============================================

#如果將回傳值應用在判斷式裡，就會直接當作 True 或 False 使用
# a=1
# b=2
# c=3
# if(a and b and c): #回傳3-->True
#     print('ok') #印出ok

#=============================================

a=1
b=0 #b 等於 0
c=3
if(a and b and c): #回傳 0-->False
    print('ok')
else:
    print('not ok') #印出not ok