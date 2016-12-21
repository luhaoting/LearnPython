#coding:utf-8

import tkinter
import tkinter.font

# 计算函数
def pp(ev=None):
    foodl = ''
    try:
        foodl = eval( text.get())
    except:
        pass
    if isinstance(foodl, (int,float,int)):
        pass
    else:
        foodl = 'Error..'
    # 显示结果
    label.config(text=foodl)


# 主窗口
top = tkinter.Tk()
top.title(u'计算器') # 窗口标题
top.wm_grid(1, 1,220,220)
top.positionfrom
ft = tkinter.font.Font(family = ('Verdana'), size = 8) # 字体

# 注册组件
text = tkinter.Entry(top, font= ft)
Enter = lambda x: x.keycode == 13 and pp()
Key = lambda x: label.config(text=u'运算符: + - * / % **')
text.bind('<Key>', Enter) # 回车事件
text.focus()  # 获得焦点
text.bind('<Button-1>', Key)
text.pack()

# 计算，按钮
button = tkinter.Button(top, text=u'计算(注意先后运算)', command=pp)
button.pack()

# 文字显示
label = tkinter.Label(text=u'运算符: + - * / % **', font=ft)
label.pack()

tkinter.mainloop()


