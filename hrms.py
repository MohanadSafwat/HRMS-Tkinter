from cgitb import text
from distutils.log import error
from doctest import master
from email.mime import image
from msilib.schema import Font
from pickle import TRUE
from re import X
import tkinter as tk
from ttkwidgets import CheckboxTreeview
from tkinter import  BOTH, CENTER, LEFT, Button, Entry, Label, PhotoImage, ttk
from turtle import bgcolor, left
from emoji import emojize
from PIL import Image, ImageTk as itk


import customtkinter
import sv_ttk

import sqlite3
from tokenize import String
with sqlite3.connect("HRMS.db") as db:
    cursor=db.cursor()


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

        signinicon = itk.PhotoImage(Image.open("sign-in.png").resize((20,20),Image.ANTIALIAS))

        style = ttk.Style(root)
        style.configure("TButton", font=('wasy10', 15))

        self.framesign = ttk.Frame(self.master, width=300, height=300)
        self.framesign.pack()
        self.signin_button = customtkinter.CTkButton(self.framesign,image=signinicon, text="Sign in",text_font=8,command=lambda : self.auth(error,usernameTextField.get_value(),passwordTextField.get_value())
        ,compound="right",fg_color="#FFFFFF",hover_color="#F5F5F5",width=50,height=50)
        self.signin_button.pack()

   
        
        sv_ttk.set_theme("light")

    def getdata(self):
        x=self.tv.selection()
        y=self.tv.item(x)['values']
        print("getatra   ",y)
        return y
    
    def register(self,user):
        for i in self.master.winfo_children():
            i.destroy()
        print("user",user)

        welcome_message="Welcome " + user[0][1] + "..... 👋"
        self.frame2 = ttk.Frame(self.master)
        self.text2 = tk.Label(self.frame2, text=welcome_message,font = ('calibri', 33))
        self.text2.pack(side="left" )

        editicon = itk.PhotoImage(Image.open("pencil.png").resize((20,20),Image.ANTIALIAS))
        deleteicon = itk.PhotoImage(Image.open("remove.png").resize((20,20),Image.ANTIALIAS))
        signouticon = itk.PhotoImage(Image.open("logout.png").resize((15,15),Image.ANTIALIAS))
        addemployeeicon = itk.PhotoImage(Image.open("add-user.png").resize((20,20),Image.ANTIALIAS))

        self.signoutbutton = customtkinter.CTkButton(self.frame2,image=signouticon, text="Sign Out",command=self.login,
        compound="right",fg_color="#FFFFFF",hover_color="#F5F5F5")
        self.signoutbutton.pack(side="right", padx=10)


        self.add_employee_button = customtkinter.CTkButton(self.frame2,image=addemployeeicon, text="Add Employee",command=lambda : self.add_emploee(user)
        ,compound="right",fg_color="#FFFFFF",hover_color="#F5F5F5",width=10)
        self.add_employee_button.pack(side="right", padx=10)

        self.frame1 = ttk.Frame(self.master, padding=10)

        Column_id=1,2,3,4,5,6,7,8,9

        error=tk.Message(text="",width=300)

        self.edittreeview = ttk.Frame(self.frame1)
        self.edittreeview.pack(side="right",anchor='center')
        self.editbutton=customtkinter.CTkButton(self.edittreeview,image=editicon,text="",width=25,height=25,
        command=lambda : self.Editing(error,user),compound="right",fg_color="#FFFFFF",hover_color="#F5F5F5")
        self.editbutton.pack(side='top',pady=10)       

        self.deletebutton=customtkinter.CTkButton(self.edittreeview,image=deleteicon,text="",width=25,height=25,
         command=lambda : self.delete_empoyee(error,user),compound="right",fg_color="#FFFFFF",hover_color="#F5F5F5")
        self.deletebutton.pack(side='top') 
      

        self.tv = ttk.Treeview(self.frame1, columns=(Column_id))
         

        self.tv.pack(fill="both",padx=20, pady=20)
        self.tv.heading("1", text="ID")
        self.tv.column("1", width="40",anchor='center')
        self.tv.heading("2", text="Name")
        self.tv.column("2", width="140",anchor='center')
        self.tv.heading("3", text="Age")
        self.tv.column("3", width="50",anchor='center')
        self.tv.heading("4", text="Job")
        self.tv.column("4", width="150",anchor='center')
        self.tv.heading("5", text="Email")
        self.tv.column("5", width="180",anchor='center')
        self.tv.heading("6", text="Gender")
        self.tv.column("6", width="90",anchor='center')
        self.tv.heading("7", text="Mobile")
        self.tv.column("7", width="120",anchor='center')
        self.tv.heading("8", text="Address")
        self.tv.column("8", width="180",anchor='center')
        self.tv.heading("9", text="Paid")
        self.tv.column("9", width="50",anchor='center')

        self.tv['show']= 'headings'

        cursor.execute("SELECT * from employee ORDER BY id ASC")
        employees=cursor.fetchall()
        print("employees", employees)
        for employee in employees:
            self.tv.insert('', employee[0],values=employee)


        self.frame2.pack(side="top", fill="x", padx=20, pady=10)

        self.frame1.pack(side="top", fill="x", padx=20, pady=10)

     
        sv_ttk.set_theme("light")

    storeddata=["","","","","","",""]
    
    def delete_empoyee(self,error,user):
        selecteddata=self.getdata()
        print("selecteddata", selecteddata)
        error.pack()

        if selecteddata == "":
            error["text"]="Please select an employee to Delete"
        else :
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

    def Editing(self,error,user):
        y=self.getdata()
        print("sasa ",y)
        error.pack()

        if y == "":
            error["text"]="Please select an employee or add one"
        else :
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