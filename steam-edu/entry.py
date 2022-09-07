from cProfile import label
import tkinter as tk

root=tk.Tk()
root.title('OuO.studio')
root.geometry('200x200')

# entry=tk.Entry(root) #放入單行輸入框
# entry.pack()
a=tk.StringVar() #建立文字變數
b=tk.StringVar()
a.set('') #一開始設定沒有內容

# tk.Label(root,textvariable=a).pack()
# tk.Entry(root,textvariable=a).pack()

def show():
    a.set(b.get()) #顯示輸入文字

def clear():
    b.set('') #設定變數b為空字串
    entry.delete(0,'end') #清空輸入欄位內容

label=tk.Label(root,textvariable=a) #放入標籤
label.pack()
entry=tk.Entry(root,textvariable=b) #放入輸入欄位(變數為b)
entry.pack()
btn1=tk.Button(root,text='顯示',command=show) #放入顯示按鈕，點擊後執行show函式
btn1.pack()
btn2=tk.Button(root,text='清除',command=clear) #放入清空按鈕，點擊後執行clear函式
btn2.pack()

root.mainloop()
