from tkinter import*


window=Tk()
window.title("button_making")
window.geometry("600x400")
window.resizable(0,0)

def bt1(event):
    window['bg']= 'Aqua'
    Lab=Label(window, text= 'you pushed button1', font='Times 20', fg= 'black')
    Lab.place(x=150, y = 150)

def bt2(event):
    window['bg']= 'pink'
    Lab=Label(window, text= 'you pushed button2', font='Times 20', fg= 'yellow')
    Lab.place(x=150, y = 150)

bt01 = Button (window, width=10, height = 2, fg = 'violet', text = 'Button 1', font='Times 12')
bt01.place(x=40, y=250)
bt01.bind('<Button>', bt1)

bt02 = Button (window, width=10, height = 2, fg = 'violet', text = 'Button 2', font='Times 12')
bt02.place(x=400, y=250)
bt02.bind('<Button>', bt2)

window.mainloop()
