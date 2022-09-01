#定義建立生成器函式
# def test() :
#     print("第一階段")
#     yield 5
#     print("第二階段")
#     yield 10
#呼叫並回傳生成器
# gen=test()
#搭配for迴圈中使用
# for d in gen:
#     print(d) 

def generateEven(maxNumber):
    number=0
    while number<=maxNumber:
        yield number
        number+=2

evenGenerator=generateEven(16)
for data in evenGenerator:
    print(data)