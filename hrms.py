from cgitb import text
from distutils.log import error
from doctest import master
from pickle import TRUE
from re import X
import tkinter as tk
from tkinter import BOTH, CENTER, LEFT, Button, Entry, Label, ttk
from turtle import bgcolor, left
from emoji import emojize

# textfield("Name",30,20,10,y[1])
#             textfield("Age",30,20,10,y[2])
#             textfield("Job",30,20,10,y[3])
#             textfield("Email",30,20,10,y[4])
#             textfield("Gender",30,20,10,y[5])
#             textfield("Mobile",30,20,10,y[6])
#             textfield("Address",30,20,10,y[7])
#             textfield("Paid",30,20,10,y[8])

import sv_ttk

import sqlite3
from tokenize import String
with sqlite3.connect("HRMS.db") as db:
    cursor=db.cursor()

# cursor.execute ("""DROP TABLE Employess""")
# cursor.execute ("""DROP TABLE employee""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS employee (id integer PRIMARY KEY AUTOINCREMENT 
, name text NOT NULL ,age int NOT NULL,
job text NOT NULL,email text NOT NULL UNIQUE,gender text NOT NULL
,mobile text NOT NULL UNIQUE,address text NOT NULL
,paid bool NOT NULL default false) """)

cursor.execute(""" CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY AUTOINCREMENT 
, name text NOT NULL ,username text NOT NULL UNIQUE,password text NOT NULL
,role text NOT NULL ) """)


class textfield:
    ent1=""
    
    def __init__(self,app,title,entwidth,fontsize,pady,text) :
        self.fram1 = ttk.Frame(app.master, width=300, height=300)
        self.fram1.pack(pady=pady)
        self.lbl1 = ttk.Label(self.fram1, text=title,font=('calibri',fontsize))
        self.lbl1.pack(side=tk.LEFT)
        self.ent1=ttk.Entry(self.fram1,text="",width=entwidth)
        self.ent1.insert(0, text)
        self.ent1.pack(side=tk.LEFT,padx=10)
    def get_value(self):
        return self.ent1.get()


class app:

    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x800")
        root.title('HR Management System')
        root.geometry("1200x800")
        theme ="light"
        sv_ttk.set_theme(theme)
        self.login()
    
    

    def create_button(self,text,command,width):
        self.framesign = ttk.Frame(self.master, width=300, height=300)
        self.framesign.pack()
        self.register_btn = ttk.Button(self.framesign, text=text, command=command,width=width)
        self.register_btn.pack()

    def auth(self,error,username,password):
        cursor.execute("SELECT * from users WHERE username=? AND password=?",(username,password))
        user=cursor.fetchall()
        if user:
            self.register(user)
        else:
            error["text"]="Invalid Username or Password"

    def login(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame1 = ttk.Frame(self.master, width=300, height=150)
        self.frame1.pack(pady=100)

        usernameTextField=textfield(self,"Username",30,20,12,"")
        passwordTextField=textfield(self,"Password",30,20,12,"")
        
        error=tk.Message(text="",width=200)
        error.pack()
        self.create_button("Sign in",lambda : self.auth(error,usernameTextField.get_value(),passwordTextField.get_value()),20)
        # self.framesign = ttk.Frame(self.master, width=300)
        # self.framesign.pack()
        # self.register_btn = ttk.Button(self.framesign, text="Sign in", command=self.register)
        # self.register_btn.pack()
        
        sv_ttk.set_theme("light")

    def getdata(self):
        x=self.tv.selection()
        y=self.tv.item(x)['values']
        print(y)
        return y
    
    def register(self,user):
        for i in self.master.winfo_children():
            i.destroy()
        print("user",user)

        welcome_message="Welcome " + user[0][1] + "..... 👋"
        self.frame2 = ttk.Frame(self.master)
        self.text2 = tk.Label(self.frame2, text=welcome_message,font = ('calibri', 33))
        self.text2.pack(side="left" )

        # self.button = self.button(self.frame2, text='Add' , command=edit)
        # self.button.pack(side="right", padx=10)
        self.button = ttk.Button(self.frame2, text="Sign Out", command=self.login)
        self.button.pack(side="right", padx=10)



        self.button = ttk.Button(self.frame2, text="Delete Employee",command=lambda : self.delete_empoyee(user))
        self.button.pack(side="right")

        self.button = ttk.Button(self.frame2, text="Add Employee",command=lambda : self.add_emploee(user))
        self.button.pack(side="right", padx=10)


        self.accentbutton = ttk.Button(self.frame2, text="Edit", style="Accent.TButton",command=lambda : self.Editing(user))
        self.accentbutton.pack(side="right", padx=10)



        self.frame1 = ttk.Frame(self.master, padding=10)




        # style = ttk.Style()
        # style.configure("mystyle.Treeview",font=('calibri',13),rowheight=50)
        # style.configure("mystyle.Treeview.Heading",font=('calibri',13))
        self.tv = ttk.Treeview(self.frame1, columns=(1,2,3,4,5,6,7,8,9))
        self.tv.pack(fill="both",padx=20, pady=20)

        self.tv.heading("1", text="ID")
        self.tv.column("1", width="40")
        self.tv.heading("2", text="Name")
        self.tv.column("2", width="140")
        self.tv.heading("3", text="Age")
        self.tv.column("3", width="50")
        self.tv.heading("4", text="Job")
        self.tv.column("4", width="150")
        self.tv.heading("5", text="Email")
        self.tv.column("5", width="180")
        self.tv.heading("6", text="Gender")
        self.tv.column("6", width="90")
        self.tv.heading("7", text="Mobile")
        self.tv.column("7", width="120")
        self.tv.heading("8", text="Address")
        self.tv.column("8", width="180")
        self.tv.heading("9", text="Paid")
        self.tv.column("9", width="50")
        self.tv['show']= 'headings'

        cursor.execute("SELECT * from employee ORDER BY id ASC")
        employees=cursor.fetchall()
        print(employees)
        for employee in employees:
            self.tv.insert('', employee[0],values=employee)

        # self.tv.place(x=1,y=1)
        # text1 = tk.Text(self.frame1, borderwent1th=0, highlightthickness=0, wrap="word",
        #                 width=40, height=4)
        # text1.pack(fill="both", expand=True
        # )
        # text1.bind("<FocusIn>", lambda event: self.frame1.state(["focus"]))
        # text1.bind("<FocusOut>", lambda event: self.frame1.state(["!focus"]))
        # text1.insert("end", "This went1get has the focus")



        self.frame2.pack(side="top", fill="x", padx=20, pady=10)

        self.frame1.pack(side="top", fill="x", padx=20, pady=10)

     
        sv_ttk.set_theme("light")

    storeddata=["","","","","","",""]
    
    def delete_empoyee(self,user):
        selecteddata=self.getdata()
        print("selecteddata", selecteddata)
        cursor.execute("DELETE FROM employee WHERE id="+str(selecteddata[0]))
        db.commit()
        self.register(user)

        

    def create(self,title,entwidth,fontsize,pady,text):
        self.fram1 = ttk.Frame(self.master, width=300, height=300)
        self.fram1.pack(pady=pady)
        self.lbl1 = ttk.Label(self.fram1, text=title,font=('calibri',fontsize))
        self.lbl1.pack(side=tk.LEFT)
        self.ent1=ttk.Entry(self.fram1,text="",width=entwidth)
        self.ent1.insert(0, text)
        self.ent1.pack(side=tk.LEFT,padx=10)
    def Editing(self,user):
        y=self.getdata()
        self.Edit_employee(y,user)

    def insertEmployee(self,error,name, age, job, email, gender, mobile, address):
        try: 
            cursor.execute("INSERT INTO employee (name,age,job,email,gender,mobile,address) VALUES (?,?,?,?,?,?,?)",(name,age,job,email,gender,mobile,address))
            db.commit()
            error["text"]="User is ADDED sucessfully"
            print('name', name)
        except:
            error["text"]="User is already exists in the database"
            print(NameError)
    


    def add_emploee(self,user):
            for i in self.master.winfo_children():
                i.destroy()
            self.frameaddemployee = ttk.Frame(self.master)
            self.frameaddemployee.pack(pady=100)
            nameTextField = textfield(self,"Name",30,20,12,"")
            age=textfield(self,"Age",30,20,10,"")
            job=textfield(self,"Job",30,20,10,"")
            email=textfield(self,"Email",30,20,10,"")
            gender=textfield(self,"Gender",30,20,10,"")
            mobile=textfield(self,"Mobile",30,20,10,"")
            address=textfield(self,"Address",30,20,20,"")
            error=tk.Message(text="",width=200)
            error.pack()
            self.framebutton = ttk.Frame(self.master, width=300, height=300)
            self.framebutton.pack()
            self.register_btn = ttk.Button(self.framebutton, text="Add", command=lambda : self.insertEmployee(error,  nameTextField.get_value(),age.get_value(),job.get_value(),email.get_value(),gender.get_value(),mobile.get_value(),address.get_value()) ,width=12)
            self.register_btn.pack(side="left",padx=15)
            self.register_btn2 = ttk.Button(self.framebutton, text="Back", command=lambda : self.register(user),width=12)
            self.register_btn2.pack()
            
    def edit_database(self,name, age, job, email, gender, mobile, address,paid,id):
        
        cursor.execute("UPDATE employee SET name=?,age=?,job=?,email=?,gender=?,mobile=?,address=?,paid=? WHERE id=?" ,(name,age,job,email,gender,mobile,address,paid,id))
        db.commit()
        self.register()

    def Edit_employee(self,y,user):
            for i in self.master.winfo_children():
                i.destroy()
            self.frameaddemployee = ttk.Frame(self.master)
            self.frameaddemployee.pack(pady=100)
            print("y,",y)
            nameTextField=textfield(self,"Name",30,20,10,y[1])
            ageTextField=textfield(self,"Age",30,20,10,y[2])
            jobTextField=textfield(self,"Job",30,20,10,y[3])
            emailTextField=textfield(self,"Email",30,20,10,y[4])
            genderTextField=textfield(self,"Gender",30,20,10,y[5])
            mobileTextField=textfield(self,"Mobile",30,20,10,y[6])
            addressTextField=textfield(self,"Address",30,20,10,y[7])
            paidTextField=textfield(self,"Paid",30,20,10,y[8])
            self.framebutton = ttk.Frame(self.master, width=300, height=300)
            self.framebutton.pack(pady=15)
            self.register_btn = ttk.Button(self.framebutton, text="Edit", command=lambda :self.edit_database(nameTextField.get_value(),ageTextField.get_value(),jobTextField.get_value(),emailTextField.get_value(),genderTextField.get_value(),mobileTextField.get_value(),addressTextField.get_value(),paidTextField.get_value(),y[0]),width=12)
            self.register_btn.pack(side="left",padx=15)
            self.register_btn2 = ttk.Button(self.framebutton, text="Back", command=lambda : self.register(user),width=12)
            self.register_btn2.pack()

            


root = tk.Tk()
app(root)









root.mainloop()