#簡單閉包closure
# def a(msg):
#     i='!!!' #-----------------閉包開始
#     def b(): #A函式內定義了B函式
#         print(msg+i) #B函式使用了A函式的變數
#     return b #將B函式當作回傳值-閉包結束
# s=a('hello')
# s() #hello

#============================================

#閉包的範例應用
# def count(): #建立一個count函式
#     a=[] #函式內有區域變數a是串列
#     def avg(val): #建立內置函式avg(閉包)
#         a.append(val) #將數值加入變數a
#         print(a) #印出a
#         return sum(a)/len(a) #回傳a串列所有數值的平均
#     return avg #回傳avg

# test=count()
# test(10) #將10存入a
# test(11) #將11存入a
# test(12) #將12存入a 同時用debug看avg會因為line 18回傳11

#============================================

#自由變數nonlocal
#不過如果將上方的例子，改成變數的做法，可能就會發生錯誤，因為在 cal 函式裡的變數 a 後方使用了「等號」，
# 意義等同於變數的「賦值」，換句話說是新建了一個區域變數 a，就造成了名稱空間裡名稱重疊的問題。
# def count(): #建立一個count函式
#     a=1
#     def cal(val):
#         a=a+val
#         return a
#     return cal

# test=count()
# test(10)
# test(11)
# test(12)

#============================================

#使用 nonlocal 的方式，宣告這個變數是「自由變數」( 不是這個區域裡的變數 )，就能正常使用這個變數。
def count():
    a=1
    def cal(val):
        nonlocal a #宣告a為自由變數
        a=a+val
        print(a)
        return a
    return cal

test=count()
test(10)
test(11)
test(12)
