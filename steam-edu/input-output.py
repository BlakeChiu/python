#如果有設定 end，則會取代換行符，導致下一個 print 的結果和上一個連在一起
# print(1,2,3) #1 2 3
# print(1,2,3,sep=';') #1;2;3
# print(1,2,3,sep=';',end='!')
# print(1,2,3) #1;2;3!1 2 3

#=========================================

#這段程式在「本機環境運作」，會看到「Loading」後方的「.」每隔 0.5 秒出現，若將 flush 移除或改為 False，會發現結果一次出現六個「.」
# import time
# print('Loading',end='')
# for i in range(6):
#     print('',end='',flush=True)
#     time.sleep(0.5)

#=========================================

#print 的內容前方加上「\r」的命令，就能讓每次印出時的游標位置，移動到該行的開頭
# import time
# n=10
# for i in range(n+1):
#     print(f'\r倒數 {n-i} 秒',end='')
#     time.sleep(1)
# print('\r時間到',end='')

#=========================================

#input(x)
# a=input('輸入文字: ')
# print('您輸入的數字:'+a)

#=========================================

# a=int(input('輸入第一個數字:'))
# b=int(input('輸入第二個數字:'))
# print(f'兩個數字相加結果是:{a+b}')

#=========================================

#追求輸入的速度，也可使用標準函式庫 sys 的 stdin.readline() 進行
import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
print(f'兩個數字相加結果是:{a+b}')