#計算1+2+3+.....max的裝飾器
def calculateFactory(max):
    def calculate(callback):
        def run():
            total=0
            for n in range(max+1):
                total+=n
            callback(total)
        return run
    return calculate

@calculateFactory(100)
def show(result):
    print("結果是",result)

@calculateFactory(10)
def showEnglish(result):
    print("Result is",result)

show()
showEnglish()

# def myFactory(base):
#     def myDeco(cb):
#         def run():
#             print("裝飾器內的程式",base)
#             result=base*2
#             cb(result)
#         return run
#     return myDeco

# @myFactory(5)
# def test(result):
#     print("普通函式的程式",result)

# test()