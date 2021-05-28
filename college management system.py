from tkinter import *
from tkinter import ttk

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

    #create frames
    f_Frame = LabelFrame(top, font=('arial', 50, 'bold'), width=1330, height=500, bg='skyblue', bd=13)
    f_Frame.place(x=15, y=20)

    Labelb = Label(f_Frame, text='', font=('arial', 30, 'bold'), bg='light grey')
    Labelb.place(x=80, y=0)

    f_Framec = LabelFrame(top, font=('arial', 50, 'bold'), width=1220, height=115, bg='skyblue', bd=13)
    f_Framec.place(x=50, y=570)

    Labelc = Label(f_Frame, text='', font=('arial', 30, 'bold'), bg='light grey')
    Labelc.place(x=50, y=570)

    f_Framed = LabelFrame(top, font=('arial', 50, 'bold'), width=700, height=380, bg='white', )
    f_Framed.place(x=600, y=97)

    Labeld = Label(f_Frame, text='', font=('arial', 30, 'bold'), bg='light grey')
    Labeld.place(x=600, y=97)

    label = Label(top, text="STUDENT INFORMATION", font=('arial', 17, "bold"), bg="sky blue", padx=10, pady=10)
    label.place(x=30, y=50, )

    label = Label(top, text="STUDENT DATABASE", font=('arial', 17, "bold"), bg="sky blue", padx=10, pady=10)
    label.place(x=600, y=50, )

    #Defining names and labels
    name = Label(top, text="Name",font=('arial',15,'bold'), bg="sky blue")
    name.place(x=50, y=120)
    e1 = Entry(top, font=('arial',15,'bold'))
    e1.place(x=200, y=120, width=250, height=30)

    father_name = Label(top, text="Father Name",font=('arial',15,'bold'), bg="sky blue")
    father_name.place(x=50, y=160)
    e2 = Entry(top,font=('arial',15,'bold'))
    e2.place(x=200, y=160, width=250, height=30)

    mother_name = Label(top, text="Mother Name",font=('arial',15,'bold'), bg="sky blue")
    mother_name.place(x=50, y=200)
    e3 = Entry(top,font=('arial',15,'bold'))
    e3.place(x=200, y=200, width=250, height=30)

    address = Label(top, text="Address",font=('arial',15,'bold'), bg="sky blue")
    address.place(x=50, y=240)
    e4 = Entry(top,font=('arial',15,'bold'))
    e4.place(x=200, y=240, width=250, height=30)

    mobile_number = Label(top, text="Mobile Number",font=('arial',15,'bold'), bg="sky blue")
    mobile_number.place(x=50, y=280)
    e5 = Entry(top,font=('arial',15,'bold'))
    e5.place(x=200, y=280, width=250, height=30)

    dob = Label(top, text="Date of Birth", font=('arial', 15, 'bold'), bg="sky blue")
    dob.place(x=50, y=320)
    e6 = Entry(top, font=('arial', 15, 'bold'))
    e6.place(x=200, y=320, width=250, height=30)

    gender = Label(top, text="Gender",font=('arial',15,'bold'), bg="sky blue")
    gender.place(x=50, y=360)
    e7 = ttk.Combobox(top, values=(' ', 'Male', 'Female', 'Others'),font=('arial', 17, 'bold'), textvariable=gender, width=19)
    e7.place(x=200, y=360, width=250, height=30)

    # Creating a buttons
    savebutton = Button(top, text="SAVE", font=('arial', 15, 'bold'), width=11, height=2, bg="lightgrey")
    savebutton.place(x=80, y=590)

    displaybutton = Button(top, text="DISPLAY", font=('arial', 15, 'bold'), width=11, height=2, bg="lightgrey")
    displaybutton.place(x=250, y=590)

    resetbutton = Button(top, text="RESET", font=('arial', 15, 'bold'), width=11, height=2, bg="lightgrey")
    resetbutton.place(x=420, y=590)

    updatebutton = Button(top, text="UPDATE", font=('arial', 15, 'bold'), width=11, height=2, bg="lightgrey")
    updatebutton.place(x=580, y=590)

    deletebutton = Button(top, text="DELETE", font=('arial', 15, 'bold'), width=11, height=2, bg="lightgrey")
    deletebutton.place(x=750, y=590)

    searchbutton = Button(top, text="SEARCH", font=('arial', 15, 'bold'), width=11, height=2, bg="lightgrey")
    searchbutton.place(x=920, y=590)

    exitbutton = Button(top, text="EXT", font=('arial', 15, 'bold'),command=top.quit, width=11, height=2, bg="lightgrey")
    exitbutton.place(x=1090, y=590)


def marksheet():
    top = Toplevel()
    top.title('Search Page')
    top.geometry('1350x750')
    top.config(bg='sky blue')

    def create_new_win():
        new = Toplevel()
        new.title('Marksheet')
        new.geometry('1350x750')
        new.config(bg='sky blue')

        # Defining name and labels
        name = Label(new, text="Name", font=('arial', 15, 'bold'), bg="sky blue")
        name.place(x=50, y=70)
        e1 = Entry(new, font=('arial', 15, 'bold'))
        e1.place(x=200, y=70, width=250, height=30)

        father_name = Label(new, text="Father Name", font=('arial', 15, 'bold'), bg="sky blue")
        father_name.place(x=50, y=110)
        e2 = Entry(new, font=('arial', 15, 'bold'))
        e2.place(x=200, y=110, width=250, height=30)

        dob = Label(new, text="Date of Birth", font=('arial', 15, 'bold'), bg="sky blue")
        dob.place(x=50, y=150)
        e3 = Entry(new, font=('arial', 15, 'bold'))
        e3.place(x=200, y=150, width=250, height=30)

        school_name = Label(new, text="School Name", font=('arial', 15, 'bold'), bg="sky blue")
        school_name.place(x=50, y=190)
        e4 = Entry(new, font=('arial', 15, 'bold'))
        e4.place(x=200, y=190, width=250, height=30)

        roll = Label(new, text="Roll Number", font=('arial', 15, 'bold'), bg="sky blue")
        roll.place(x=700, y=70)
        e5 = Entry(new, font=('arial', 15, 'bold'))
        e5.place(x=900, y=70, width=250, height=30)

        mother_name = Label(new, text="Mother Name", font=('arial', 15, 'bold'), bg="sky blue")
        mother_name.place(x=700, y=110)
        e6 = Entry(new, font=('arial', 15, 'bold'))
        e6.place(x=900, y=110, width=250, height=30)

        gender = Label(new, text="Gender", font=('arial', 15, 'bold'), bg="sky blue")
        gender.place(x=700, y=150)
        e7 = ttk.Combobox(new, values=(' ', 'Male', 'Female', 'Others'),font=('arial', 15, 'bold'), textvariable=gender, width=19)
        e7.place(x=900, y=150, width=250, height=30)

        subject = Label(new, text="SUBJECT", font=('arial', 17, 'bold'), bg="sky blue")
        subject.place(x=100, y=300)

        marksobt = Label(new, text="MARKS OBTAINED", font=('arial', 17, 'bold'), bg="sky blue")
        marksobt.place(x=300, y=300)

        passmarks = Label(new, text="PASSING MARKS", font=('arial', 17, 'bold'), bg="sky blue")
        passmarks.place(x=550, y=300)

        total = Label(new, text="TOTAL MARKS", font=('arial', 17, 'bold'), bg="sky blue")
        total.place(x=800, y=300)

        english = Label(new, text="ENGLISH", font=('arial', 17,), bg="sky blue")
        english.place(x=90, y=350)
        eng = Entry(new, font=('arial', 15, 'bold'))
        eng.place(x=360, y=350, width=70, height=30)

        eng1 = Entry(new, font=('arial', 15, 'bold'))
        eng1.place(x=600, y=350, width=70, height=30)

        eng2 = Entry(new, font=('arial', 15, 'bold'))
        eng2.place(x=850, y=350, width=70, height=30)

        physics = Label(new, text="PHYSICS", font=('arial', 17,), bg="sky blue")
        physics.place(x=90, y=400)
        phy = Entry(new, font=('arial', 15, 'bold'))
        phy.place(x=360, y=400, width=70, height=30)

        phy1 = Entry(new, font=('arial', 15, 'bold'))
        phy1.place(x=600, y=400, width=70, height=30)

        phy2 = Entry(new, font=('arial', 15, 'bold'))
        phy2.place(x=850, y=400, width=70, height=30)

        chemistry = Label(new, text="CHEMISTRY", font=('arial', 17,), bg="sky blue")
        chemistry.place(x=90, y=450)
        che = Entry(new, font=('arial', 15, 'bold'))
        che.place(x=360, y=450, width=70, height=30)

        che1 = Entry(new, font=('arial', 15, 'bold'))
        che1.place(x=600, y=450, width=70, height=30)

        che2 = Entry(new, font=('arial', 15, 'bold'))
        che2.place(x=850, y=450, width=70, height=30)

        math = Label(new, text="MATHEMATICS", font=('arial', 17,), bg="sky blue")
        math.place(x=70, y=500)
        mat = Entry(new, font=('arial', 15, 'bold'))
        mat.place(x=360, y=500, width=70, height=30)

        mat1 = Entry(new, font=('arial', 15, 'bold'))
        mat1.place(x=600, y=500, width=70, height=30)

        mat2 = Entry(new, font=('arial', 15, 'bold'))
        mat2.place(x=850, y=500, width=70, height=30)

        computer = Label(new, text="COMPUTER SCIENCE", font=('arial', 16,), bg="sky blue")
        computer.place(x=80, y=550)
        com = Entry(new, font=('arial', 15, 'bold'))
        com.place(x=360, y=550, width=70, height=30)


        com1 = Entry(new, font=('arial', 15, 'bold'))
        com1.place(x=600, y=550, width=70, height=30)

        com2 = Entry(new, font=('arial', 15, 'bold'))
        com2.place(x=850, y=550, width=70, height=30)

        grandtotal = Label(new, text="GRAND TOTAL", font=('arial', 17,), bg="sky blue")
        grandtotal.place(x=70, y=600)
        gran = Entry(new, font=('arial', 15, 'bold'))
        gran.place(x=360, y=600, width=70, height=30)

        gran1 = Entry(new, font=('arial', 15, 'bold'))
        gran1.place(x=850, y=600, width=70, height=30)

        percentage = Label(new, text="PERCENTAGE", font=('arial', 19,"bold"), bg="sky blue")
        percentage.place(x=70, y=650)
        per = Entry(new, font=('arial', 15, 'bold'))
        per.place(x=360, y=650, width=70, height=30)

        division = Label(new, text="DIVISION", font=('arial', 19,"bold"), bg="sky blue")
        division.place(x=100, y=700)
        div = Entry(new, font=('arial', 15, 'bold'))
        div.place(x=340, y=700, width=100, height=30)

        gpa = Label(new, text="GPA", font=('arial', 20, "bold"), bg="sky blue")
        gpa.place(x=600, y=650)

        gpa1 = Entry(new, font=('arial', 15, 'bold'))
        gpa1.place(x=850, y=650, width=70, height=30)

        result = Label(new, text="RESULT", font=('arial', 20, "bold"), bg="sky blue")
        result.place(x=600, y=700)
        res1 = Entry(new, font=('arial', 15, 'bold'))
        res1.place(x=830, y=700, width=100, height=30)

        grade = Label(new, text="GRADE", font=('arial', 20, "bold"), bg="sky blue")
        grade.place(x=1050, y=650)

        grade1 = Entry(new, font=('arial', 15, 'bold'))
        grade1.place(x=1200, y=650, width=70, height=30)

        #Creating buttons
        combutton = Button(new, text="COMPUTE", font=('arial', 15, 'bold'), width=11, height=0, bg="lightgrey")
        combutton.place(x=1050, y=350)

        savebutton = Button(new, text="SAVE", font=('arial', 15, 'bold'), width=11, height=0, bg="lightgrey")
        savebutton.place(x=1050, y=400)

        updatebutton = Button(new, text="UPDATE", font=('arial', 15, 'bold'), width=11, height=0, bg="lightgrey")
        updatebutton.place(x=1050, y=450)

        resetbutton = Button(new, text="RESET", font=('arial', 15, 'bold'), width=11, height=0, bg="lightgrey")
        resetbutton.place(x=1050, y=500)

        exitbutton = Button(new, text="EXIT", font=('arial', 15, 'bold'), width=11, height=0, bg="lightgrey")
        exitbutton.place(x=1050, y=550)

    f_Framea = LabelFrame(top, font=('arial', 50, 'bold'), width=1000, height=200, bg='skyblue', bd=13)
    f_Framea.place(x=150, y=200)

    Labela = Label(f_Framea, text='', font=('arial', 30, 'bold'), bg='light grey')
    Labela.place(x=150, y=200)

    ern = Label(top, text="Enter Roll Number", font=('arial', 23, 'bold'), bg="sky blue")
    ern.place(x=300, y=250)
    e1 = Entry(top, font=('arial', 15, 'bold')).place(x=700, y=250, width=250, height=45)

    # create Buttons
    sbutton= Button(top, text="SEARCH",font=('arial',15,'bold'), width=15, height=1,bg="lightgrey")
    sbutton.place(x=300, y=330)

    createbutton = Button(top, text="CREATE NEW ", font=('arial', 15, 'bold'),command=create_new_win, width=15, height=1, bg="lightgrey")
    createbutton.place(x=700, y=330)



def feereport():
    top = Toplevel()
    top.title('Fee Report')
    top.geometry('1350x750')
    top.config(bg='sky blue')

    t_Frame = LabelFrame(top, font=('arial', 50, 'bold'), width=1000, height=90, bg='light grey', bd=13)
    t_Frame.place(x=150, y=0)

    t_Label = Label(t_Frame, text='FEE REPORT', font=('arial', 36, 'bold'), bg='light grey')
    t_Label.place(x=280, y=0)

    f_Frame = LabelFrame(top, font=('arial', 50, 'bold'), width=1300, height=350, bg='skyblue', bd=13)
    f_Frame.place(x=0, y=100)

    Labela = Label(f_Frame, text='', font=('arial', 30, 'bold'), bg='light grey')
    Labela.place(x=150, y=0)

    f_Frameb = LabelFrame(top, font=('arial', 50, 'bold'), width=1290, height=90, bg='skyblue', bd=13)
    f_Frameb.place(x=20, y=630)

    Labelb = Label(f_Frame, font=('arial', 30, 'bold'), bg='light grey')
    Labelb.place(x=20, y=630)

    f_Framec = LabelFrame(top, font=('arial', 50, 'bold'), width=1300, height=170, bg='white', bd=13)
    f_Framec.place(x=25, y=455)

    Labelc = Label(f_Frame, text='', font=('arial', 30, 'bold'), bg='light grey')
    Labelc.place(x=25, y=455)

    f_Framed = LabelFrame(top, font=('arial', 50, 'bold'), width=480, height=255, bg='white', )
    f_Framed.place(x=790, y=165)

    Labeld = Label(f_Frame, text='', font=('arial', 30, 'bold'), bg='light grey')
    Labeld.place(x=790, y=165)

    label = Label(top, text="Informations", font=('arial', 15, "bold"), bg="sky blue", padx=10, pady=10)
    label.place(x=20, y=120)

    label = Label(top, text="Fee Receipt", font=('arial', 15, "bold"), bg="sky blue", padx=10, pady=10)
    label.place(x=790, y=120)

    receipt = Label(top, text="Receipt No", font=('arial', 14, 'bold'), bg="sky blue")
    receipt.place(x=30, y=170)
    e1 = Entry(top, font=('arial', 15, 'bold'), ).place(x=150, y=170, width=250, height=30)

    student_name = Label(top, text="Student Name", font=('arial', 14, 'bold'), bg="sky blue")
    student_name.place(x=20, y=210)
    e2 = Entry(top, font=('arial', 15, 'bold'), ).place(x=150, y=210, width=250, height=30)

    admission = Label(top, text="Admission No", font=('arial', 14, 'bold'), bg="sky blue")
    admission.place(x=20, y=250)
    e3 = Entry(top, font=('arial', 15, 'bold'), ).place(x=150, y=250, width=250, height=30)

    date = Label(top, text="Date", font=('arial', 14, 'bold'), bg="sky blue")
    date.place(x=20, y=290)
    e4 = Entry(top, font=('arial', 15, 'bold'), ).place(x=150, y=290, width=250, height=30)

    branch = Label(top, text="Branch", font=('arial', 14, 'bold'), bg="sky blue")
    branch.place(x=20, y=330)
    e5 = ttk.Combobox(top, values=(' ', 'Bsc Hons Computing', 'Bsc Hons Ethical Hacking And Cyber Security',),font=('arial', 15, 'bold'), textvariable=branch, width=19)
    e5.place(x=150, y=330, width=250, height=30)

    semester= Label(top, text="Semester", font=('arial', 14, 'bold'), bg="sky blue")
    semester.place(x=20, y=370)
    e6 = ttk.Combobox(top, values=(' ', 'FIRST', 'SECOND', 'THIRD','FOURTH', 'FIFTH', 'SIXTH', 'SEVENTH', 'EIGHTH'),font=('arial', 15, 'bold'), textvariable=semester, width=19)
    e6.place(x=150, y=370, width=250, height=30)

    # Creating a buttons
    savebutton = Button(top, text="SAVE", font=('arial', 14, 'bold'), width=11, height=1, bg="lightgrey")
    savebutton.place(x=50, y=655)

    displaybutton = Button(top, text="DISPLAY", font=('arial', 15, 'bold'), width=11, height=1, bg="lightgrey")
    displaybutton.place(x=210, y=655)

    resetbutton = Button(top, text="RESET", font=('arial', 15, 'bold'), width=11, height=1, bg="lightgrey")
    resetbutton.place(x=360, y=655)

    updatebutton = Button(top, text="UPDATE", font=('arial', 15, 'bold'), width=11, height=1, bg="lightgrey")
    updatebutton.place(x=520, y=655)

    deletebutton = Button(top, text="DELETE", font=('arial', 15, 'bold'), width=11, height=1, bg="lightgrey")
    deletebutton.place(x=680, y=655)

    searchbutton = Button(top, text="SEARCH", font=('arial', 15, 'bold'), width=11, height=1, bg="lightgrey")
    searchbutton.place(x=840, y=655)

    receiptbutton = Button(top, text="RECEIPT NO", font=('arial', 15, 'bold'), width=11, height=1, bg="lightgrey")
    receiptbutton.place(x=1000, y=655)

    exitbutton = Button(top, text="EXT", font=('arial', 15, 'bold'), width=11, height=1, bg="lightgrey")
    exitbutton.place(x=1150, y=655)


def menu():
    title_Frame = LabelFrame(root, font=('arial', 50, 'bold'), width=1000, height=100, bg='light grey', bd=13)
    title_Frame.grid(row=0, column=0, pady=50)

    title_Label = Label(title_Frame, text='MENU', font=('arial', 30, 'bold'), bg='light grey')
    title_Label.grid(row=0, column=0, padx=150)

    #create a frames
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
    Button_1 = Button(Frame_1, text='VIEW', font=('arial', 16, 'bold'), width=8, command=information)
    Button_1.grid(row=0, column=3, padx=50)

    Button_2 = Button(Frame_2, text='VIEW', font=('arial', 16, 'bold'), width=8,command=feereport)
    Button_2.grid(row=0, column=3, padx=50)

    Button_3 = Button(Frame_3, text='VIEW', font=('arial', 16, 'bold'), width=8,command=marksheet)
    Button_3.grid(row=0, column=3, padx=50)



menu()

root.mainloop()