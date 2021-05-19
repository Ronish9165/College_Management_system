from tkinter import *

top =Tk()


f_Frame = LabelFrame(top, font=('arial', 50, 'bold'), width=1330, height=300, bg='skyblue', bd=13)
f_Frame.place(x=15, y=20)

Label = Label(f_Frame, text='Student Details', font=('arial', 20, 'bold'), bg='light grey')
Label.place(x=20, y=0)
mainloop()