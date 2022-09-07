#class簡單範例
# class human():
#     def __init__(self): #建立預設屬性的寫法
#         self.eye=2
#         self.ear=2
#         self.nose=1
#         self.mouth=1

# oxxo=human() #製作一個名為oxxo的物件
# print(oxxo.eye) #2(印出oxxo的eye屬性)

#==========================================================

#建立類別
# class human():
#     pass #使用pass可以建立一個空類別

#==========================================================

#__init__
# class human():
#     def __init__(self):
#         self.eye=2
#         self.ear=2
#         self.nose=1
#         self.mouth=1
#     def say(self,msg): #定義say
#         print(msg)
#     def play(self,thing): #定義play
#         print(thing)

# #屬性除了可以定義在類別裡，也可以從外部定義
# human.hand=2 #定義hand屬性
# human.leg=2 #定義leg屬性

# oxxo=human()
# # oxxo.say('hello') #hello
# # oxxo.play('baseball') #baseball
# print(oxxo.hand) #2
# print(oxxo.leg) #2

#下方的例子從外部定義了 oxxo.name 的屬性，在 human 裡就能使用 self.name 取得這個屬性。
# class human():
#     def __init__(self):
#         self.eye=2
#         self.ear=2
#         self.nose=1
#         self.mouth=1
#     def say(self,msg):
#         print(f'{self.name} say:{msg}') #使用self.name取得name屬性的值
#     def play(self,thing):
#         print(thing)

# oxxo=human()
# oxxo.name='oxxo' #設定name屬性
# oxxo.say('hello') #oxxo say:hello

#==========================================================

#多個物件同一個類別
# class human():
#     def __init__(self):
#         self.eye=2
#         self.ear=2
#         self.nose=1
#         self.mouth=1
#     def say(self,msg):
#         print(f'{self.name} say:{msg}') #使用self.name取得name屬性的值
#     def play(self,thing):
#         print(thing)

# oxxo=human() #定義oxxo
# gkpen=human() #定義gkpen
# oxxo.name='oxxo' #oxxo的名字叫做oxxo
# oxxo.age=18 #oxxo的age為18

# gkpen.name='gkpen' #gkpen的名字叫做gkpen
# gkpen.weight=70 #gkpen的weight為70

# oxxo.say('hello') #oxxo say:hello
# print(oxxo.age) #18
# gkpen.say('song') #gkpen sat:song
# print(gkpen.weight) #70

#==========================================================

#如果覺得上一個麻煩可以在建立類別時，預先設定好一些參數，接著透過類別建立物件時，在做動態的調整
# class human():
#     def __init__(self,age,weight): #新增age和weight參數
#         self.eye=2
#         self.ear=2
#         self.nose=1
#         self.mouth=1
#         self.age=age       #讀取參數，變成屬性
#         self.weight=weight #讀取參數，變成屬性
#     def say(self,msg):
#         print(f'{self.name} say:{msg}')
#     def play(self,thing):
#         print(thing)

# oxxo=human(18,68)  #建立物件時，設定參數值
# gkpen=human(15,70) #建立物件時，設定參數值
# print(oxxo.age,oxxo.weight)   #18,68
# print(gkpen.age,gkpen.weight) #15,70

#==========================================================

#覆寫屬性
# class human():
#     def __init__(self):
#         self.eye=2
#         self.ear=2
#         self.nose=1
#         self.mouth=1
#     def say(self,msg):
#         print(f'{self.name} say:{msg}')
#     def play(self,thing):
#         print(thing)

# oxxo=human()
# oxxo.play='???' #覆寫play屬性
# print(oxxo.play) #???

#==========================================================

# @property唯讀屬性
class a:
    def a(self):
        return 'aaaaa'
    @property
    def b(self):
        return 'bbbbb'

oxxo=a()
oxxo.a='12345'
print(oxxo.a) #12345
oxxo.b='12345'
print(oxxo.b) #發生錯誤can't set attribute 'b'