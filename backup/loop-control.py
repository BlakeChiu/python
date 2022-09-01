# n=0
# while n<5:
#     if n==3:
#         break
#     print(n)
#     n+=1
# print("最後的n:",n)

# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue #0 2碰到不會執行下方程式，會直接進到下一圈
#     print(x)
#     n+=1
# print("最後的n:",n)

# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum) #印出0+2+...10的結果

#綜合範例:找出整數平方根
#輸入9，得到3
#輸入11，得到【沒有】整數的平方根
n=input("輸入一個正整數:")
n=int(n)
for i in range(n): #i從0~n-1
    if i*i==n:
        print("整數平方根",i)
        break #用break強制結束迴圈時，不會執行else區塊
else:
    print("沒有整數平方根")