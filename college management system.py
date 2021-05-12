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

    label = Label(top, text="Student Information", font=('arial', 20, "bold"), bg="sky blue", padx=10, pady=10)
    label.place(x=0, y=50, )

    name = Label(top, text="Name",font=('arial',15,'bold'), bg="sky blue")
    name.place(x=20, y=190)
    e1 = Entry(top, font=('arial',15,'bold'),).place(x=150, y=180, width=250, height=30)

    father_name = Label(top, text="Father Name",font=('arial',15,'bold'), bg="sky blue")
    father_name.place(x=5, y=260)
    e2 = Entry(top,font=('arial',15,'bold'),).place(x=150, y=250, width=250, height=30)

    mother_name = Label(top, text="Mother Name",font=('arial',15,'bold'), bg="sky blue")
    mother_name.place(x=2, y=310)
    e3 = Entry(top,font=('arial',15,'bold'),).place(x=150, y=310, width=250, height=30)

    address = Label(top, text="Address",font=('arial',15,'bold'), bg="sky blue")
    address.place(x=10, y=360)
    e4 = Entry(top,font=('arial',15,'bold'),).place(x=150, y=360, width=250, height=30)

    mobiile_number = Label(top, text="Mobile Number",font=('arial',15,'bold'), bg="sky blue")
    mobiile_number.place(x=0, y=400)
    e5 = Entry(top,font=('arial',15,'bold'),).place(x=150, y=400, width=250, height=30)

    dob = Label(top, text="Date of Birth",font=('arial',15,'bold'), bg="sky blue")
    dob.place(x=0, y=450)
    e6 = Entry(top,font=('arial',15,'bold'),).place(x=150, y=450, width=250, height=30)

    gender = Label(top, text="Gender",font=('arial',15,'bold'), bg="sky blue")
    gender.place(x=0, y=500)

    savebutton = Button(top, text="SAVE", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    savebutton.place(x=200, y=630)

    displaybutton = Button(top, text="DISPLAY", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    displaybutton.place(x=400, y=630)

    resetbutton = Button(top, text="RESET", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    resetbutton.place(x=600, y=630)

    updatebutton = Button(top, text="UPDATE", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    updatebutton.place(x=800, y=630)

    deletebutton = Button(top, txt="DELETE", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    deletebutton.place(x=1000, y=630)

    searchbutton = Button(top, text="SEARCH", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    searchbutton.place(x=1200, y=630)

    exitbutton = Button(top, text="EXT", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    exitbutton.place(x=1400, y=630)


def marksheet():
    top = Toplevel()
    top.title('Marksheet')
    top.geometry('1350x750')
    top.config(bg='sky blue')

    ern = Label(top, text="Enter Roll Number", font=('arial', 20, 'bold'), bg="sky blue")
    ern.place(x=200, y=250)
    e1 = Entry(top, font=('arial', 15, 'bold')).place(x=500, y=250, width=250, height=40)

    sbutton= Button(top, text="SEARCH",font=('arial',15,'bold'), width=15, height=1,bg="lightgrey")
    sbutton.place(x=200, y=330)

    createbutton = Button(top, text="CREATE NEW ", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    createbutton.place(x=500, y=330)

    frame = LabelFrame(top, x=500, y=500, bg="black")
    frame.place(x=100, y=100)

def feereport():
    top = Toplevel()
    top.title('Fee Report')
    top.geometry('1350x750')
    top.config(bg='sky blue')

    label = Label(top, text="Informations", font=('arial', 20, "bold"), bg="sky blue", padx=10, pady=10)
    label.place(x=0, y=100)

    myLabel = Label(top, text= "Fee Report ", font=('arial',50, "bold"),bg="sky blue")
    myLabel.pack()

    receipt = Label(top, text="Receipt No", font=('arial', 15, 'bold'), bg="sky blue")
    receipt.place(x=20, y=190)
    e1 = Entry(top, font=('arial', 15, 'bold'), ).place(x=150, y=180, width=250, height=30)

    student_name = Label(top, text="Student Name", font=('arial', 15, 'bold'), bg="sky blue")
    student_name.place(x=5, y=260)
    e2 = Entry(top, font=('arial', 15, 'bold'), ).place(x=150, y=250, width=250, height=30)

    admission = Label(top, text="Admission No", font=('arial', 15, 'bold'), bg="sky blue")
    admission.place(x=2, y=310)
    e3 = Entry(top, font=('arial', 15, 'bold'), ).place(x=150, y=310, width=250, height=30)

    date = Label(top, text="Date", font=('arial', 15, 'bold'), bg="sky blue")
    date.place(x=10, y=390)
    e4 = Entry(top, font=('arial', 15, 'bold'), ).place(x=150, y=390, width=250, height=30)

    branch = Label(top, text="Branch", font=('arial', 15, 'bold'), bg="sky blue")
    branch.place(x=0, y=450)
    e5 = Entry(top, font=('arial', 15, 'bold'), ).place(x=150, y=450, width=250, height=30)

    semester= Label(top, text="Semester", font=('arial', 15, 'bold'), bg="sky blue")
    semester.place(x=0, y=530)
    e6 = Entry(top, font=('arial', 15, 'bold'), ).place(x=150, y=530, width=250, height=30)

    savebutton = Button(top, text="SAVE", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    savebutton.place(x=200, y=630)

    displaybutton = Button(top, text="DISPLAY", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    displaybutton.place(x=400, y=630)

    resetbutton = Button(top, text="RESET", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    resetbutton.place(x=600, y=630)

    updatebutton = Button(top, text="UPDATE", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    updatebutton.place(x=800, y=630)

    deletebutton = Button(top, txt="DELETE", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    deletebutton.place(x=1000, y=630)

    searchbutton = Button(top, text="SEARCH", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    searchbutton.place(x=1200, y=630)

    receiptbutton = Button(top, text="RECEIPT NO", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    receiptbutton.place(x=1400, y=630)

    exitbutton = Button(top, text="EXT", font=('arial', 15, 'bold'), width=15, height=1, bg="lightgrey")
    exitbutton.place(x=1600, y=630)


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