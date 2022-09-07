#for迴圈
# for i in 'abc':
#     print(i) #a b c(字串)

# for i in ['a','b','c']:
#     print(i) #a b c(串列)

# for i in {'a','b','c'}:
#     print(i) #c b a(集合)

# for i in {'a':1,'b':2,'c':3}:
#     print(i) #a b c(字典)

#========================================

# for a in ['x','y','z']:
#     for b in [1,2,3]:
#         print(b)
#     print(a)

#1 2 3 x 1 2 3 y 1 2 3 z

#========================================

# for a in ['x','y','z']:
#     for b in [1,2,3]:
#         print(f'{a}{b}')

#x1 x2 x3 y1 y2 y3 z1 z2 z3

#========================================

#while迴圈
# a=1
# while a<=5:
#     print(a)
#     a+=1

#1 2 3 4 5

#========================================

#break 和 continue
# for a in ['x','y','z']:
#     for b in [1,2,3]:
#         if(b==2):
#             break
#         print(f'{a}{b}')
# print('ok')

#x1 y1 z1 ok

#========================================

for a in ['x','y','z']:
    for b in [1,2,3]:
        if(b==2):
            continue
        print(f'{a}{b}')
print('ok')

#x1 x3 y1 y3 z1 z3 ok