import matplotlib.pyplot as plt

#subplot(row, column, index)
# x=[1,2,3,4,5]
# y=[5,4,3,2,1]
# fig=plt.figure()
# plt.subplot(221)
# plt.plot(x)
# plt.subplot(224)
# plt.plot(y)
# plt.show()

#subplots()
# x=[1,2,3,4,5]
# y=[5,4,3,2,1]
# fig,ax=plt.subplots(2,2)
# ax[0][0].plot(x)
# ax[1][1].plot(y)
# plt.show()

#如果不設定參數，預設畫出「一張」子圖表。
# x=[1,2,3,4,5]
# y=[5,4,3,2,1]
# fig,ax=plt.subplots()
# ax.plot(x)
# plt.show()

#使用 add_subplot
# x=[1,2,3,4,5]
# y=[5,4,3,2,1]
# fig=plt.figure()
# fig.add_subplot(221)
# plt.plot(x)
# fig.add_subplot(224)
# plt.plot(y)
# plt.show()

#使用tight_layout()
# x=[1,2,3,4,5]
# y=[5,4,3,2,1]
# fig,ax=plt.subplots(2,2)
# ax[0,0].set_title('xxx')
# ax[0,0].plot(x)
# ax[1,1].set_title('yyy')
# ax[1,1].plot(x)
# plt.tight_layout()
# plt.show()

#使用subplot_tool()
# x=[1,2,3,4,5]
# y=[5,4,3,2,1]
# fig,ax=plt.subplots(2,2)
# ax[0,0].set_title('xxx')
# ax[0,0].plot(x)
# ax[1,1].set_title('yyy')
# ax[1,1].plot(x)
# plt.subplot_tool()
# plt.show()

#建立子圖表時，加入 constrained_layout=True
# x=[1,2,3,4,5]
# y=[5,4,3,2,1]
# fig,ax=plt.subplots(2,2,constrained_layout=True)
# ax[0,0].set_title('xxx')
# ax[0,0].plot(x)
# ax[1,1].set_title('yyy')
# ax[1,1].plot(x)
# plt.show()

x=[1,2,3,4,5]
y=[5,4,3,2,1]
fig=plt.figure()
plt.subplot2grid((3,3),(0,1),rowspan=2,colspan=2)
#(3,3),(0,1) 等同(332)
plt.plot(x)
plt.subplot(331)
plt.plot(x)
plt.subplot(339)
plt.plot(y)
plt.show()