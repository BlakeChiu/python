# class father(): #father類別
#     def __init__(self): #father的方法
#         self.eye=2
#         self.ear=2
#         self.nose=1
#         self.mouth=1

#簡單案例
# class son(father): #son類別繼承了father類別裡所有的方法
#     def language(self): #son類別具有language的方法
#         print('chinese') #從father繼承了5官，然後自己學會講中文

# oxxo=son() #設定oxxo為son()
# print(oxxo.eye) #印出2
# oxxo.language() #印出chinese

#繼承時會覆寫方法
# class son(father):
#     def __init__(self): #使用了__init__方法
#         self.eye=100

# oxxo=son()
# print(oxxo.eye) #100
# print(oxxo.ear) #錯誤

#使用super()
# class son(father):
#     def __init__(self):
#         super().__init__() #使用super繼承father __init__裡所有屬性
#         self.eye=100

# oxxo=son()
# print(oxxo.eye) #100
# print(oxxo.ear) #2

#多重繼承
# class mother(): #mother類別
#     def language(self): #mother的方法
#         print('english')
#     def skill(self):
#         print('painting')

# class son(father,mother): #繼承father 和 mother
#     def play(self): #son自己的方法
#         print('ball')

# oxxo=son()
# print(oxxo.eye) #2
# oxxo.skill() #painting
# oxxo.play() #ball

#==============================================================================

# class a():
#     def says(self):
#         print('a')

# class b():
#     def says(self):
#         print('b')

# class c(a,b): #先讀取a再b，就會將a裡的方法，覆寫b裡同名的方法
#     pass

# class d(b,a): #先讀取b再a，就會將b裡的方法，覆寫a裡同名的方法
#     pass

# ccc=c()
# ddd=d()
# ccc.says() #a
# ddd.says() #b

#==============================================================================

#多層繼承
# class grandpa():
#     def __init__(self):
#         self.eye=2
#         self.ear=2
#         self.nose=1
#         self.mouth=1
# class father(grandpa):
#     def language(self):
#         print('english')
#     def skill(self):
#         print('painting')

# class son(father):
#     def play(self):
#         print('ball')

# oxxo=son()
# print(oxxo.eye) #2
# oxxo.skill() #painting
# oxxo.play() #ball

#==============================================================================

#私有方法(雙底線)
class grandpa():
    def __init__(self):
        self.mouth=1
    def __money(self): #建立一個私有方法 __money
        print('$1000')
    def getMoney(self): #建立一個getMoney的方法，執行私有方法 __money
        self.__money()

class father(grandpa):
    def skill(self):
        print('painting')

class son(father):
    def play(self):
        print('ball')

oxxo=son()
oxxo.getMoney() #1000
# oxxo.__money() #發生錯誤'son' object has no attribute '__money'
