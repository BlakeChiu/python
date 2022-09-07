# a=input('輸入文字')
# print(a+1) #錯誤
# print('hello') #因前面錯誤造成也不能執行

#=============================================

# try: #使用try，測試內容是否正確
#     a=input('輸入數字:')
#     print(a+1)
# except: #如果try的內容發生錯誤，就執行except裡的內容
#     print('發生錯誤')
# print('hello')
#輸入數字:1
#發生錯誤
#hello

#=============================================

# try:
#     a=input('輸入數字:')
#     print(a+1)
# except:
#     pass #略過
# print('hello')

#=============================================

# try:
#     print(a)
# except TypeError:
#     print('型別發生錯誤')
# except NameError:
#     print('使用沒有被定義的對象')
# print('hello')
#使用沒有被定義的對象
#hello

#=============================================

#raise 和 assert 
# try:
#     a=int(input('輸入0~9:'))
#     if a>9: #如果輸入的a大於9
#         raise #強制中斷，拋出錯誤訊息席
#     print(a)
# except:
#     print('有錯誤喔~')
#輸入0~9:13
#有錯誤喔~

#=============================================

#raise 後方可以加上錯誤資訊，錯誤資訊可以包含要呈現的訊息，以下方的例子而言，
#強制停止時回報 ValueError 資訊，接著使用 except 區隔錯誤資訊，就能呈現真實的錯誤狀況。
# try:
#     a=int(input('輸入0~9:'))
#     if a>10:
#         raise ValueError('數字不在範圍內')
#     print(a)
# except ValueError as msg: #如果輸入範圍外的數字，執行這邊的程式
#     print(msg)
# except: #如果輸入的不是數字，執行這邊的程式
#     print('有錯誤喔~')
# print('繼續執行')
#輸入0~9:123
#數字不在範圍內
#繼續執行

#=============================================

# try:
#     a=int(input('輸入0~9:'))
#     if a>10:
#         assert False,'數字不在範圍內'
#     print(a)
# except AssertionError as msg:
#     print(msg)
# except:
#     print('有錯誤喔')
# print('繼續執行')
#輸入0~9:123
#數字不在範圍內
#繼續執行

#輸入0~9:abc
#有錯誤喔      
#繼續執行 

#=============================================

#加入 else 和 finally
try:
    a=int(input('輸入0~9:'))
    if a>10:
        raise
    print(a)
except:
    print('有錯誤喔~')
else:
    print('沒有錯!繼續執行') #完全沒錯才會執行這行
finally:
    print('管他有沒有錯，繼續啦') #不論有沒有錯都會執行這行
#輸入0~9:6
#6
#沒有錯!繼續執行     
#管他有沒有錯，繼續啦

#輸入0~9:123
#有錯誤喔~
#管他有沒有錯，繼續啦