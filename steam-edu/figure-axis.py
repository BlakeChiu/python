import matplotlib.pyplot as plt

#隱性建立figure
# x=[1,2,3,4,5]
# plt.plot(x)
# plt.show()

#=================================

#顯性建立figure
#方法一
# x=[1,2,3,4,5]
# f=plt.figure()
# plt.subplot()
# plt.plot(x)
# plt.show()

#方法二
x=[1,2,3,4,5]
fig,ax=plt.subplots()
ax.plot(x)
plt.show()