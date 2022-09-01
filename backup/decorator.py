#定義一個裝飾器，計算1+2+....+50的總和
def calculate(callback):
    def run():
        #裝飾器想要執行的程式碼
        result=0
        for n in range(51):
            result+=n
        #把計算結果透過參數傳到被裝飾的普通函式中
        callback(result)
    return run

#使用裝飾器
@calculate
def show(n):
    print("計算結果是",n)

@calculate
def showEnglish(n):
    print("Result is",n)

show()
showEnglish()


# #定義裝飾器
# def myDeco(cb):
#     def run():
#         print("裝飾器中的程式碼")
#         cb(3) #這個回呼函式，其實就是被裝飾的普通函式
#     return run
# #使用裝飾器
# @myDeco
# def test(n):
#     print("普通函式的程式碼",n)

# test()