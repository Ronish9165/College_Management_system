from tkinter import *

top =Tk()

f_Frame = LabelFrame(top, font=('arial', 50, 'bold'), width=1290, height=190, bg='white', bd=13)
f_Frame.place(x=0, y=50)

Label = Label(f_Frame, text='', font=('arial', 30, 'bold'), bg='light grey')
Label.place(x=150, y=0)

mainloop()