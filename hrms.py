from cgitb import text
from distutils.cmd import Command
from distutils.log import error
from doctest import master
from email.mime import image
from msilib.schema import Font
from pickle import TRUE
from re import X

import tkinter as tk
from ttkwidgets import CheckboxTreeview
from tkinter import  BOTH, CENTER, LEFT, Button, Canvas, Entry, Label, PhotoImage, Tk, Toplevel, ttk
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
    
    def __init__(self,app,title,entwidth,fontsize,pady,padylbl,text,sidelbl,sideentry) :
        self.fram1 = ttk.Frame(app, width=300, height=300)
        self.fram1.pack(pady=pady)
        self.lbl1 = ttk.Label(self.fram1, text=title,font=('calibri',fontsize))
        self.lbl1.pack(side=sidelbl,pady=padylbl)
        self.ent1=ttk.Entry(self.fram1,text="",width=entwidth)
        self.ent1.insert(0, text)
        self.ent1.pack(side=sideentry,padx=10)
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

        usernameTextField=textfield(self.master,"Username",30,20,12,0,"",tk.LEFT,tk.LEFT)
        passwordTextField=textfield(self.master,"Password",30,20,12,0,"",tk.LEFT,tk.LEFT)
        
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
    def disable_event():
        pass
    def open_popup(self,window,title,messege,yesfunction,cancelfunction):
        top= Toplevel(window)
        # top.geometry("400x150")
        top.geometry('%dx%d+%d+%d' % (400, 150, 550, 300))

        top.title(title)
        top.protocol("WM_DELETE_WINDOW", self.disable_event)        
        top.resizable(0,0)

        self.framepopup = ttk.Frame(top, width=300, height=300)
        self.framepopup.pack(side="bottom",anchor='ne',pady=10)
        Label(top, text= messege, font=('calibri 13')).pack(side="left",anchor="c",padx=35)

        self.yes = customtkinter.CTkButton(self.framepopup,command= yesfunction, text="Yes",text_font=6,fg_color="#E2E5DE",hover_color="#E2E5DE",width=20)
        self.yes.pack(side='left',padx=5)
        self.cancel = customtkinter.CTkButton(self.framepopup,command=cancelfunction, text="cancel",text_font=6,fg_color="#E2E5DE",hover_color="#E2E5DE",width=15)
        self.cancel.pack(side='right',padx=5)
#    def insertEmployee(self,edit,name, age, job, email, gender, mobile, address):
        # try: 
           
        #     error["text"]="User is ADDED sucessfully"
        #     print('name', name)
        # except:
        #     error["text"]="User is already exists in the database"
        #     print(NameError)
    def adding_query(self,user,error,edit,name,age,job,email,gender,mobile,address):
        # try:
            cursor.execute("INSERT INTO employee (name,age,job,email,gender,mobile,address) VALUES (?,?,?,?,?,?,?)",(name,age,job,email,gender,mobile,address))
            db.commit()        
            for i in self.master.winfo_children():
                i.destroy()
            self.register(user)
        # except:
        #     error["text"]="User is already exists in the database"
        #     print(NameError)
    def edit_database(self,user,name, age, job, email, gender, mobile, address,paid,id):
        
        cursor.execute("UPDATE employee SET name=?,age=?,job=?,email=?,gender=?,mobile=?,address=?,paid=? WHERE id=?" ,(name,age,job,email,gender,mobile,address,paid,id))
        db.commit()
        for i in self.master.winfo_children():
            i.destroy()
        self.register(user)

  
    
    def popup_Edit_window(self,y,user):
        edit= Toplevel()
        edit.title("Edit Employee")
        edit.geometry('%dx%d+%d+%d' % (250, 700, 600, 70))
        edit.resizable(0,0)
        saveicon = itk.PhotoImage(Image.open("floppy-disk.png").resize((30,30),Image.ANTIALIAS))
        # edit.overrideredirect(1)
        print("y,",y)
        nameTextField=textfield(edit,"Name",25,15,5,5,y[1],tk.TOP,tk.TOP)
        ageTextField=textfield(edit,"Age",25,15,5,5,y[2],tk.TOP,tk.TOP)
        jobTextField=textfield(edit,"Job",25,15,5,5,y[3],tk.TOP,tk.TOP)
        emailTextField=textfield(edit,"Email",25,15,5,5,y[4],tk.TOP,tk.TOP)
        genderTextField=textfield(edit,"Gender",25,15,5,5,y[5],tk.TOP,tk.TOP)
        mobileTextField=textfield(edit,"Mobile",25,15,5,5,y[6],tk.TOP,tk.TOP)
        addressTextField=textfield(edit,"Address",25,15,5,5,y[7],tk.TOP,tk.TOP)
        paidTextField=textfield(edit,"Paid",25,15,5,5,y[8],tk.TOP,tk.TOP)
        self.sasa = ttk.Frame(edit)
        self.sasa.pack(anchor='center',pady=10)
        self.savebutton1=customtkinter.CTkButton(self.sasa,image=saveicon,text="",width=25,height=25,
        command=lambda :self.open_popup(edit.master,"Save","Are you sure you want to save",lambda :self.edit_database(user,nameTextField.get_value(),ageTextField.get_value(),jobTextField.get_value(),emailTextField.get_value(),genderTextField.get_value(),mobileTextField.get_value(),addressTextField.get_value(),paidTextField.get_value(),y[0]),lambda : self.register(user)),compound="right",fg_color="#FFFFFF",hover_color="#F5F5F5")
        
        self.savebutton1.pack(side='left',padx=15)  
# command=lambda :self.edit_database(user,nameTextField.get_value(),ageTextField.get_value(),jobTextField.get_value(),emailTextField.get_value(),genderTextField.get_value(),mobileTextField.get_value(),addressTextField.get_value(),paidTextField.get_value(),y[0])
    def popup_Add_window(self,user):
        delete= Toplevel()
        delete.title("Add Employee")
        delete.geometry('%dx%d+%d+%d' % (250, 650, 550, 70))
        error=tk.Message(text="",width=150)
        error.pack()

        saveicon = itk.PhotoImage(Image.open("check.png").resize((30,30),Image.ANTIALIAS))
        cancelicon = itk.PhotoImage(Image.open("back.png").resize((30,30),Image.ANTIALIAS))
        # edit.protocol("WM_DELETE_WINDOW", self.disable_event)        # top.overrideredirect(1)
        delete.resizable(0,0)
        name1=textfield(delete,"Name",25,15,5,5,"",tk.TOP,tk.TOP)
        age1=textfield(delete,"Age",25,15,5,5,"",tk.TOP,tk.TOP)        
        job1=textfield(delete,"Job",25,15,5,5,"",tk.TOP,tk.TOP)
        email1=textfield(delete,"Email",25,15,5,5,"",tk.TOP,tk.TOP)
        gender1=textfield(delete,"Gender",25,15,5,5,"",tk.TOP,tk.TOP)
        mobile1=textfield(delete,"Mobile",25,15,5,5,"",tk.TOP,tk.TOP)
        address1=textfield(delete,"Address",25,15,5,5,"",tk.TOP,tk.TOP)
        # paid1=textfield(edit,"Paid",25,15,5,5,"",tk.TOP,tk.TOP)
        error=tk.Message(text="",width=200)
        error.pack()
        self.sasa = ttk.Frame(delete)
        self.sasa.pack(anchor='center',pady=10)
        self.savebutton1=customtkinter.CTkButton(self.sasa,image=saveicon,text="",width=25,height=25,
        command=lambda : self.adding_query(user,delete,error,name1.get_value(),age1.get_value(),job1.get_value(),email1.get_value(),gender1.get_value(),mobile1.get_value(),address1.get_value()),compound="right",fg_color="#FFFFFF",hover_color="#F5F5F5")
        self.savebutton1.pack(side='left',padx=15)       

        self.deletebutton=customtkinter.CTkButton(self.sasa,image=cancelicon,text="",width=25,height=25,
       command=lambda : self.register(user),compound="right",fg_color="#FFFFFF",hover_color="#F5F5F5")
        self.deletebutton.pack(side='left') 



    def register(self,user):
        for i in self.master.winfo_children():
            i.destroy()
        print("user",user)

        welcome_message="Welcome " + user[0][1] + "..... 👋"
        self.frame2 = ttk.Frame(self.master)
        self.text2 = tk.Label(self.frame2, text=welcome_message,font = ('Mistral', 33))
        self.text2.pack(side="left" )

        editicon = itk.PhotoImage(Image.open("pencil.png").resize((20,20),Image.ANTIALIAS))
        deleteicon = itk.PhotoImage(Image.open("remove.png").resize((20,20),Image.ANTIALIAS))
        signouticon = itk.PhotoImage(Image.open("logout.png").resize((15,15),Image.ANTIALIAS))
        addemployeeicon = itk.PhotoImage(Image.open("add-user.png").resize((20,20),Image.ANTIALIAS))

        self.signoutbutton = customtkinter.CTkButton(self.frame2,image=signouticon, text="Sign Out",command=self.login,
        compound="right",fg_color="#FFFFFF",hover_color="#F5F5F5")
        self.signoutbutton.pack(side="right", padx=10)

        self.add_employee_button = customtkinter.CTkButton(self.frame2,image=addemployeeicon, text="Add Employee",command=lambda : self.popup_Add_window(user) 
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
    
    def deleting_query(self,user,selecteddata):
        cursor.execute("DELETE FROM employee WHERE id="+str(selecteddata[0]))
        db.commit()
        for i in self.master.winfo_children():
            i.destroy()
        self.register(user)

    def delete_empoyee(self,error,user):
        selecteddata=self.getdata()
        print("selecteddata", selecteddata)
        error.pack()

        if selecteddata == "":
            error["text"]="Please select an employee to Delete"

        else :
            self.open_popup(master,"Delete","Are you sure you want to delete this employee",lambda : self.deleting_query(user,selecteddata),lambda : self.register(user))

        

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
            self.popup_Edit_window(y,user)

 

root = tk.Tk()
app(root)

root.mainloop()


  # def Edit_employee(self,y,user):
    #         for i in self.master.winfo_children():
    #             i.destroy()
    #         self.frameaddemployee = ttk.Frame(self.master)
    #         self.frameaddemployee.pack(pady=100)
    #         print("y,",y)
    #         nameTextField=textfield(self.master,"Name",30,20,10,0,y[1],tk.LEFT,tk.LEFT)
    #         ageTextField=textfield(self.master,"Age",30,20,10,0,y[2],tk.LEFT,tk.LEFT)
    #         jobTextField=textfield(self.master,"Job",30,20,10,0,y[3],tk.LEFT,tk.LEFT)
    #         emailTextField=textfield(self.master,"Email",30,20,10,0,y[4],tk.LEFT,tk.LEFT)
    #         genderTextField=textfield(self.master,"Gender",30,20,10,0,y[5],tk.LEFT,tk.LEFT)
    #         mobileTextField=textfield(self.master,"Mobile",30,20,10,0,y[6],tk.LEFT,tk.LEFT)
    #         addressTextField=textfield(self.master,"Address",30,20,10,0,y[7],tk.LEFT,tk.LEFT)
    #         paidTextField=textfield(self.master,"Paid",30,20,10,0,y[8],tk.LEFT,tk.LEFT)
    #         self.framebutton = ttk.Frame(self.master, width=300, height=300)
    #         self.framebutton.pack(pady=15)
    #         self.register_btn = ttk.Button(self.framebutton, text="Edit", command=lambda :self.edit_database(nameTextField.get_value(),ageTextField.get_value(),jobTextField.get_value(),emailTextField.get_value(),genderTextField.get_value(),mobileTextField.get_value(),addressTextField.get_value(),paidTextField.get_value(),y[0]),width=12)
    #         self.register_btn.pack(side="left",padx=15)
    #         self.register_btn2 = ttk.Button(self.framebutton, text="Back", command=lambda : self.register(user),width=12)
    #         self.register_btn2.pack()



    
    # def add_emploee(self,user):
    #         for i in self.master.winfo_children():
    #             i.destroy()
    #         self.frameaddemployee = ttk.Frame(self.master)
    #         self.frameaddemployee.pack(pady=100)
    #         nameTextField = textfield(self.master,"Name",30,20,12,0,"",tk.LEFT,tk.LEFT)
    #         age=textfield(self.master,"Age",30,20,10,0,"",tk.LEFT,tk.LEFT)
    #         job=textfield(self.master,"Job",30,20,10,0,"",tk.LEFT,tk.LEFT)
    #         email=textfield(self.master,"Email",30,20,10,0,"",tk.LEFT,tk.LEFT)
    #         gender=textfield(self.master,"Gender",30,20,10,0,"",tk.LEFT,tk.LEFT)
    #         mobile=textfield(self.master,"Mobile",30,20,10,0,"",tk.LEFT,tk.LEFT)
    #         address=textfield(self.master,"Address",30,20,20,0,"",tk.LEFT,tk.LEFT)
    #         error=tk.Message(text="",width=200)
    #         error.pack()
    #         self.framebutton = ttk.Frame(self.master, width=300, height=300)
    #         self.framebutton.pack()
    #         self.register_btn = ttk.Button(self.framebutton, text="Add", command=lambda : self.insertEmployee(error,  nameTextField.get_value(),age.get_value(),job.get_value(),email.get_value(),gender.get_value(),mobile.get_value(),address.get_value()) ,width=12)
    #         self.register_btn.pack(side="left",padx=15)
    #         self.register_btn2 = ttk.Button(self.framebutton, text="Back", command=lambda : self.register(user),width=12)
    #         self.register_btn2.pack()