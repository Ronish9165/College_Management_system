from tkinter import *

# Defining the title of project
root = Tk()
root.title("College Management System")
root.iconbitmap('college.ico')
root.geometry('1350x750')
root.config(bg='sky blue')

def information():
    top = Toplevel()
    top.title('Registration')
    top.geometry('1350x750')
    top.config(bg='sky blue')


    Frame(top, width=50, height=500, bd=6).place(x=500, y=200)
    label = Label(top, text="Student Information", font=('arial', 20, "bold"), bg="sky blue", padx=10, pady=10)
    label.place(x=0, y=50, )

    name = Label(top, text="Name",font=('arial',15,'bold'), bg="sky blue")
    name.place(x=20, y=180)
    e1 = Entry(top, font=('arial',15,'bold'),).place(x=150, y=180, width=250, height=50)

    father_name = Label(top, text="Father Name",font=('arial',15,'bold'), bg="sky blue")
    father_name.place(x=5, y=250)
    e2 = Entry(top,font=('arial',15,'bold'),).place(x=150, y=250, width=250, height=50)

    mother_name = Label(top, text="Mother Name",font=('arial',15,'bold'), bg="sky blue")
    mother_name.place(x=2, y=310)
    e3 = Entry(top,font=('arial',15,'bold'),).place(x=150, y=310, width=250, height=50)

    address = Label(top, text="Address",font=('arial',15,'bold'), bg="sky blue")
    address.place(x=10, y=390)
    e4 = Entry(top,font=('arial',15,'bold'),).place(x=150, y=390, width=250, height=50)

    mobiile_number = Label(top, text="Mobile Number",font=('arial',15,'bold'), bg="sky blue")
    mobiile_number.place(x=0, y=450)
    e5 = Entry(top,font=('arial',15,'bold'),).place(x=150, y=450, width=250, height=50)

    dob = Label(top, text="Date of Birth",font=('arial',15,'bold'), bg="sky blue")
    dob.place(x=0, y=530)
    e6 = Entry(top,font=('arial',15,'bold'),).place(x=150, y=530, width=250, height=50)

    # gender = Label(top, text="Gender", bg="sky blue").place(x=0, y=310)


def marksheet():
    top = Toplevel()
    top.title('Marksheet')
    top.geometry('1350x750')
    top.config(bg='sky blue')

def feereport():
    top = Toplevel()
    top.title('Fee Report')
    top.geometry('1350x750')
    top.config(bg='sky blue')


    myLabel = Label(top, text= "Fee Report ", font=('arial',50, "bold"),bg="sky blue")
    myLabel.pack()

    receipt = Label(top, text="Receipt No.", bg="sky blue")
    receipt.place(x=10, y=50)
    e1 = Entry(top).place(x=80, y=50, )

    student_name = Label(top, text="Student Name", bg="sky blue")
    student_name.place(x=0, y=90)
    e2 = Entry(top).place(x=80, y=90, )

    admission = Label(top, text="Admission No.", bg="sky blue")
    admission.place(x=2, y=130)
    e3 = Entry(top).place(x=80, y=130)

    date = Label(top, text="Date", bg="sky blue")
    date.place(x=10, y=170)
    e4 = Entry(top).place(x=80, y=170)

    branch = Label(top, text="Branch", bg="sky blue")
    branch.place(x=0, y=210)
    e5 = Entry(top).place(x=80, y=210)

    semester = Label(top, text="Semester", bg="sky blue")
    semester.place(x=0, y=250)
    e6 = Entry(top).place(x=80, y=250)




def menu():
    title_Frame = LabelFrame(root, font=('arial', 50, 'bold'), width=1000, height=100, bg='light grey', bd=13)
    title_Frame.grid(row=0, column=0, pady=50)

    title_Label = Label(title_Frame, text='MENU', font=('arial', 30, 'bold'), bg='light grey')
    title_Label.grid(row=0, column=0, padx=150)

    #
    Frame_1 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='light grey')
    Frame_1.grid(row=1, column=0, padx=280)

    Frame_2 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='light grey')
    Frame_2.grid(row=2, column=0, padx=130, pady=40)

    Frame_3 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='light grey')
    Frame_3.grid(row=3, column=0, pady=7)

    # Defining the labels
    Label_1 = Label(Frame_1, text='STUDENT PROFILE', font=('arial', 25, 'bold'), bg='light grey')
    Label_1.grid(row=0, column=0, padx=50, pady=5)

    Label_2 = Label(Frame_2, text='FEE REPORT', font=('arial', 25, 'bold'), bg='light grey')
    Label_2.grid(row=0, column=0, padx=100, pady=5)

    Label_3 = Label(Frame_3, text='MARKSHEET', font=('arial', 25, 'bold'), bg='light grey')
    Label_3.grid(row=0, column=0, padx=101, pady=5)

    # Defining the buttons
    Button_1 = Button(Frame_1, text='VIEW', font=('arial', 16, 'bold'), width=8, command=information )
    Button_1.grid(row=0, column=3, padx=50)

    Button_2 = Button(Frame_2, text='VIEW', font=('arial', 16, 'bold'), width=8,command=feereport )
    Button_2.grid(row=0, column=3, padx=50)

    Button_3 = Button(Frame_3, text='VIEW', font=('arial', 16, 'bold'), width=8,command=marksheet )
    Button_3.grid(row=0, column=3, padx=50)


menu()

root.mainloop()