#if
# a=2
# b=3
# if a>b:
#     print('hello') #不會印出，因為結果為False
# print('ok') #ok

#===============================================

#if、else
# a=2
# b=3
# if a>b:
#     print('hello') #不會印出，因為結果為False
# else:
#     print('world') #world
# print('ok') #ok

#===============================================

#if、elif、else
# a=2
# b=3
# if a>b:
#     print('a>b') #不會印出
# elif a<b:
#     print('a<b') #a<b
# else:
#     print('a=b') #不會印出
# print('ok') #ok

#===============================================

#可以使用「pass」作為空式子
# a=2
# b=3
# if a>b:
#     pass #不作任何動作
# elif a<b:
#     print('a<b') #a<b
# else:
#     print('a=b') #不會印出
# print('ok') #ok

#===============================================

#巢狀判斷
# a=2
# b=3
# if a<b:
#     print('a<b') #a<b
#     if a==1:
#         print('a=1') #不會印出
#     elif a==2:
#         print('a=2') #a=2
#     elif a==3:
#         print('a=3') #不會印出
# elif a>b:
#     print('a>b') #不會印出
# else:
#     print('a=b') #不會印出
# print('ok') #ok

#===============================================

#三元運算式(條件運算式)
# a=1
# b=2
# c=''
# if a>b:
#     c='a'
# else:
#     c='b'
# print(c) #b

#===============================================

#三元運算式化簡之後
a=1
b=2
c=''
c='a' if a>b else 'b'
print(c) #b