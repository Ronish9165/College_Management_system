from tkinter import *

top =Tk()


f_Frame = LabelFrame(top, font=('arial', 50, 'bold'), width=1000, height=500, bg='skyblue', bd=13)
f_Frame.place(x=15, y=20)

Label = Label(f_Frame, text='Fee Receipt', font=('arial', 20, 'bold'), bg='light grey')
Label.place(x=790, y=120)
mainloop()