from cgitb import text
from distutils.cmd import Command
from distutils.log import error
from doctest import master
from email.mime import image
import re



from pickle import TRUE
from re import X
from shutil import move

import tkinter as tk
from ttkwidgets import CheckboxTreeview
from tkinter import BOTH, CENTER, LEFT, Button, Canvas, Entry, Label, PhotoImage, Tk, Toplevel, ttk
from turtle import bgcolor, left
from emoji import emojize
from PIL import Image, ImageTk as itk
from tkinter import BOTH, CENTER, LEFT, Button, Entry, Label, ttk
from turtle import bgcolor, left, width
import emoji
from PIL import ImageTk, Image


import customtkinter
import sv_ttk

import sqlite3
from tokenize import String
with sqlite3.connect("HRMS.db") as db:
    cursor = db.cursor()

# cursor.execute(""" 
# DROP TABLE users
# """)


cursor.execute(""" CREATE TABLE IF NOT EXISTS employee (id integer PRIMARY KEY AUTOINCREMENT 
, name text NOT NULL ,age int NOT NULL,
job text NOT NULL,email text NOT NULL UNIQUE,gender text NOT NULL
,mobile text NOT NULL UNIQUE,address text NOT NULL
,paid bool NOT NULL default false) """)

cursor.execute(""" CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY AUTOINCREMENT 
, name text NOT NULL ,username text NOT NULL UNIQUE,password text NOT NULL
,role text NOT NULL ) """)


class TextField:
    entery = ""

    def __init__(self, parent, title, entwidth, fontsize, pady, padylbl, text, sidelbl, sideentry, isPassword=False):
        self.textFieldWrapper = ttk.Frame(parent, width=300, height=300)
        self.textFieldWrapper.pack(pady=pady)
        self.textFieldLabel = ttk.Label(self.textFieldWrapper, text=title, font=(
            'calibri', fontsize), foreground="#782c2d")
        self.textFieldLabel.pack(side=sidelbl, pady=padylbl)
        self.entery = ttk.Entry(self.textFieldWrapper, text="",
                              width=entwidth, show='*' if isPassword else '')
        self.entery.insert(0, text)
        self.entery.pack(side=sideentry, padx=10)

    def get_value(self):
        return self.entery.get()


class App:
    user = ""

    def __init__(self, master):
        self.master = master
        theme = "light"
        sv_ttk.set_theme(theme)
        self.login()

    ############# Pages #############

    def login(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.wrapperFrame = tk.Frame(width=300, height=150)
        self.wrapperFrame.place(in_=self.master, anchor="c", relx=.5, rely=.5)

        self.imageFrame = ttk.Frame(self.wrapperFrame, width=300, height=150)
        self.imageFrame.pack(side="top")

        logoImageFile = Image.open("./logo.png")
        logoImage = ImageTk.PhotoImage(logoImageFile)
        logoImageLabel = tk.Label(image=logoImage)

        logoImageLabel.image = logoImage
        logoImageLabel.pack(in_=self.imageFrame)

        self.formFrame = tk.Frame(self.wrapperFrame, width=100, height=100)
        self.formFrame.pack(side="bottom")

        usernameTextField = TextField(
            self.formFrame, "Username", 30, 20, 12, 0, "", tk.LEFT, tk.LEFT)
        passwordTextField = TextField(
            self.formFrame, "Password", 30, 20, 12, 0, "", tk.LEFT, tk.LEFT, True)

        errorMessage = tk.Message(self.formFrame, text="",
                                  width=200, foreground="red")
        errorMessage.pack()

        signInIcon = itk.PhotoImage(Image.open(
            "sign-in.png").resize((20, 20), Image.ANTIALIAS))

        style = ttk.Style(root)
        style.configure("TButton", font=('wasy10', 15))

        self.loginButtonFrame = ttk.Frame(
            self.formFrame, width=300, height=300)
        self.loginButtonFrame.pack()
        self.loginButton = customtkinter.CTkButton(self.loginButtonFrame, image=signInIcon, text="Sign in", text_font=8, command=lambda: self.auth(
            errorMessage, usernameTextField.get_value(), passwordTextField.get_value()), compound="right", fg_color="#fcba03", text_color="#fff", hover_color="#fcba03", width=50, height=35)
        self.loginButton.pack()

    def dashboard(self, user):

        # Destroy Previous Pages
        for i in self.master.winfo_children():
            i.destroy()

        # # Icons
        # editIcon = itk.PhotoImage(Image.open(
        #     "pencil.png").resize((20, 20), Image.ANTIALIAS))
        # deleteIcon = itk.PhotoImage(Image.open(
        #     "remove.png").resize((20, 20), Image.ANTIALIAS))
        signOutIcon = itk.PhotoImage(Image.open(
            "logout.png").resize((15, 15), Image.ANTIALIAS))
        # addEmployeeIcon = itk.PhotoImage(Image.open(
        #     "add-user.png").resize((20, 20), Image.ANTIALIAS))

        ########### Start Navbar ###########

        ##### Welcome Message #####
        self.navbarFrame = ttk.Frame(self.master)
        self.navbarFrame.pack(side="top", fill="x", padx=20, pady=10)
        self.welcomeMessage = tk.Label(
            self.navbarFrame, text=f'Welcome {user[0][1]} ', font=('Mistral', 33))
        self.wavingEmoji = tk.Label(
            self.navbarFrame, text="\U0001f44b", font=('Mistral', 33))
        self.welcomeMessage.pack(side="left")
        self.wavingEmoji.pack(side="left")

        ##### Buttons #####
        self.signOutButton = customtkinter.CTkButton(self.navbarFrame, image=signOutIcon, text="Sign Out", command=self.login,
                                                     compound="right", fg_color="#f02e2e", text_color="#fff", hover_color="#f02e2e")
        self.signOutButton.pack(side="right", padx=10)

        # self.addEmployeeButton = customtkinter.CTkButton(self.navbarFrame, image=addEmployeeIcon, text="Add Employee", command=lambda: self.addPopup(
        #     user), compound="right", fg_color="#fcba03", text_color="#fff", hover_color="#fcba03", width=10)
        # self.addEmployeeButton.pack(side="right", padx=10)

        ########### End Navbar ###########

        ########### Start Employess Table ###########

        # self.dataWrapperFrame = ttk.Frame(self.master, padding=10)
        # self.dataWrapperFrame.pack(side="top", fill="x", padx=20, pady=10)

        # errorMessage = tk.Message(text="", width=300, foreground="red")
        # errorMessage.pack()

        # self.actionsTreeView = ttk.Frame(self.dataWrapperFrame)
        # self.actionsTreeView.pack(side="right", anchor='center')
        # self.editButton = customtkinter.CTkButton(self.actionsTreeView, image=editIcon, text="", width=25, height=25,
        #                                           command=lambda: self.editEmployeeAction(errorMessage, user), compound="right", fg_color="#fafafa", hover_color="#fafafa")
        # self.editButton.pack(side='top', pady=10)

        # self.deleteButton = customtkinter.CTkButton(self.actionsTreeView, image=deleteIcon, text="", width=25, height=25,
        #                                             command=lambda: self.deleteEmployeeAction(errorMessage, user), compound="right", fg_color="#fafafa", hover_color="#fafafa")
        # self.deleteButton.pack(side='top')

        # cloumnsTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        # self.employeesTable = ttk.Treeview(
        #     self.dataWrapperFrame, columns=cloumnsTuple)
        # self.employeesTable.pack(fill="both", padx=20, pady=20)

        # self.employeesTable.heading("1", text="ID")
        # self.employeesTable.column("1", width="40", anchor='center')
        # self.employeesTable.heading("2", text="Name")
        # self.employeesTable.column("2", width="140", anchor='center')
        # self.employeesTable.heading("3", text="Age")
        # self.employeesTable.column("3", width="50", anchor='center')
        # self.employeesTable.heading("4", text="Job")
        # self.employeesTable.column("4", width="150", anchor='center')
        # self.employeesTable.heading("5", text="Email")
        # self.employeesTable.column("5", width="180", anchor='center')
        # self.employeesTable.heading("6", text="Gender")
        # self.employeesTable.column("6", width="90", anchor='center')
        # self.employeesTable.heading("7", text="Mobile")
        # self.employeesTable.column("7", width="120", anchor='center')
        # self.employeesTable.heading("8", text="Address")
        # self.employeesTable.column("8", width="180", anchor='center')
        # self.employeesTable.heading("9", text="Paid")
        # self.employeesTable.column("9", width="50", anchor='center')

        # self.employeesTable['show'] = 'headings'

        # cursor.execute("SELECT * from employee ORDER BY id ASC")
        # employees = cursor.fetchall()

        # for employee in employees:
        #     self.employeesTable.insert('', employee[0], values=employee)

    ############# Actions #############

    def deleteEmployeeAction(self, errorMessage, user):
        # Get selected employee data
        selectedData = self.getdata()

        if selectedData == "":
            errorMessage["text"] = "Please select an employee first"

        else:
            self.confirmPopup(master, "Delete", f"Are you sure you want to delete Employee #{selectedData[0]}",
                              lambda: self.deleteQuery(user, selectedData), lambda: self.dashboard(user))

    def editEmployeeAction(self, errorMessage, user):
        # Get selected employee data
        selectedData = self.getdata()
        # Throw error if there is no selected employee
        if selectedData == "":
            errorMessage["text"] = "Please select an employee first"
        # open edit pop if else
        else:
            self.editPopup(selectedData, user)

    ############# Validation #############

    def validateEmployee(self, user, nameError, ageError, jobError, emailError, genderError, mobileError, addressError, name, age, job, email, gender, mobile, address,id,query, databaseError, paidError={},paid ='0', ):
        nameError['text'] = ""
        ageError['text'] = ""
        jobError['text'] = ""
        emailError['text'] = ""
        genderError['text'] = ""
        mobileError['text'] = ""
        addressError['text'] = ""
        paidError['text'] = ""

        self.validFlag = True
        self.emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.mobileRegex = r'\b[05]+[0-9]{9,}\b'
 
        if(name == ''):
            nameError['text'] = "Invalid Name"
            self.validFlag = False
        if(not(str.isdigit(age))):
            ageError['text'] = "Invalid Age"
            self.validFlag = False
        elif(int(age) < 18 or int(age) > 65):
            ageError['text'] = "Invalid Age"
            self.validFlag = False
        if(job == ''):
            jobError['text'] = "Invalid Job"
            self.validFlag = False
        if(not(re.fullmatch(self.emailRegex, email))):
            emailError['text'] = "Invalid Email"
            self.validFlag = False
        if(gender != 'male' and gender != 'female'):
            genderError['text'] = "Invalid Gender"
            self.validFlag = False
        if(not(re.fullmatch(self.mobileRegex, mobile))):
            mobileError['text'] = "Invalid Mobile"
            self.validFlag = False
        if(address == ''):
            addressError['text'] = "Invalid Adress"
            self.validFlag = False
        if(paid != '0' and paid != '1'):
            paidError['text'] = "Invalid Paid"
            self.validFlag = False

        if(self.validFlag):
            if(query == 'add'):
                self.addQuery(user, name, age, job, email, gender, mobile, address, databaseError )
            if(query == 'edit'):
                self.confirmPopup(self.master, "Edit", f"Are you sure you want to Edit Empliyee #{id}", lambda: self.editQuery(user, name, age, job, email, gender, mobile, address, paid, id, databaseError ) , lambda: self.dashboard(user))
               
    ############# Queries #############

    def addQuery(self, user, name, age, job, email, gender, mobile, address, databaseError):
        try:
            cursor.execute("INSERT INTO employee (name,age,job,email,gender,mobile,address) VALUES (?,?,?,?,?,?,?)",
                       (name, age, job, email, gender, mobile, address))
            db.commit()
            for i in self.master.winfo_children():
                i.destroy()
        
            self.dashboard(user)
        except:
            databaseError['text']= 'Redundant Email or Mobile'

        
   
    def deleteQuery(self, user, selectedData):

        # Delete Query
        cursor.execute("DELETE FROM employee WHERE id="+str(selectedData[0]))
        db.commit()

        # Destroy Windows
        for i in self.master.winfo_children():
            i.destroy()

        # Redirct to Dashboard Page
        self.dashboard(user)

    def editQuery(self, user, name, age, job, email, gender, mobile, address, paid, id, databaseError):
        try:
            # Edit Query
            cursor.execute("UPDATE employee SET name=?,age=?,job=?,email=?,gender=?,mobile=?,address=?,paid=? WHERE id=?",
                        (name, age, job, email, gender, mobile, address, paid, id))
            db.commit()

            # Destroy Windows 
            for i in self.master.winfo_children():
                i.destroy()
            
            # Redirect to dashboard
            self.dashboard(user)
        except:
            databaseError['text']= 'Redundant Email or Mobile'


    ############# Popups #############

    def editPopup(self, selectedData, user):

        ### Icons
        saveIcon = itk.PhotoImage(Image.open(
            "floppy-disk.png").resize((30, 30), Image.ANTIALIAS))
        backIcon = itk.PhotoImage(Image.open(
            "back.png").resize((30, 30), Image.ANTIALIAS))

        ### Edit Popup Window
        editTopLevel = Toplevel()
        editTopLevel.title("Edit Employee")
        editTopLevel.geometry('%dx%d+%d+%d' % (250, 800, 600, 30))
        editTopLevel.resizable(0, 0)

        ### Textfields
        nameTextField = TextField(
            editTopLevel, "Name", 25, 15, 5, 5, selectedData[1], tk.TOP, tk.TOP)
        nameError = tk.Message(editTopLevel, text="",
                                  width=200, foreground="red")
        nameError.pack()
        ageTextField = TextField(
            editTopLevel, "Age", 25, 15, 5, 5, selectedData[2], tk.TOP, tk.TOP)
        ageError = tk.Message(editTopLevel, text="",
                                  width=200, foreground="red")
        ageError.pack()
        jobTextField = TextField(
            editTopLevel, "Job", 25, 15, 5, 5, selectedData[3], tk.TOP, tk.TOP)
        jobError = tk.Message(editTopLevel, text="",
                                  width=200, foreground="red")
        jobError.pack()
        emailTextField = TextField(
            editTopLevel, "Email", 25, 15, 5, 5, selectedData[4], tk.TOP, tk.TOP)
        emailError = tk.Message(editTopLevel, text="",
                                  width=200, foreground="red")
        emailError.pack()
        genderTextField = TextField(
            editTopLevel, "Gender", 25, 15, 5, 5, selectedData[5], tk.TOP, tk.TOP)
        genderError = tk.Message(editTopLevel, text="",
                                  width=200, foreground="red")
        genderError.pack()
        mobileTextField = TextField(
            editTopLevel, "Mobile", 25, 15, 5, 5, selectedData[6], tk.TOP, tk.TOP)
        mobileError = tk.Message(editTopLevel, text="",
                                  width=200, foreground="red")
        mobileError.pack()
        addressTextField = TextField(
            editTopLevel, "Address", 25, 15, 5, 5, selectedData[7], tk.TOP, tk.TOP)
        addressError = tk.Message(editTopLevel, text="",
                                  width=200, foreground="red")
        addressError.pack()
        paidTextField = TextField(
            editTopLevel, "Paid", 25, 15, 5, 5, selectedData[8], tk.TOP, tk.TOP)
        paidError = tk.Message(editTopLevel, text="",
                                  width=200, foreground="red")
        paidError.pack()

        databaseError = tk.Message(editTopLevel, text="",
                                  width=200, foreground="red")
        databaseError.pack()
        ### Buttons
        self.buttonWrapper = ttk.Frame(editTopLevel)
        self.buttonWrapper.pack(anchor='center', pady=10)
        self.editButton = customtkinter.CTkButton(self.buttonWrapper, image=saveIcon, text="", width=25, height=25,
                                                  command=lambda:self.validateEmployee(user, nameError, ageError, jobError, emailError, genderError, mobileError, addressError, nameTextField.get_value(), ageTextField.get_value(), jobTextField.get_value(), emailTextField.get_value(), genderTextField.get_value(), mobileTextField.get_value(), addressTextField.get_value(), databaseError=databaseError, id=selectedData[0], query='edit', paidError=paidError, paid=paidTextField.get_value()) , compound="right",fg_color="#fafafa", hover_color="#fafafa")

        self.editButton.pack(side='left', padx=15)
        self.backButton = customtkinter.CTkButton(self.buttonWrapper, image=backIcon, text="", width=25, height=25,
                                                  command=lambda: self.dashboard(user), compound="right",fg_color="#fafafa", hover_color="#fafafa")
        self.backButton.pack(side='right')

    def addPopup(self, user):

        

        ### Icons
        saveIcon = itk.PhotoImage(Image.open(
            "check.png").resize((30, 30), Image.ANTIALIAS))
        backIcon = itk.PhotoImage(Image.open(
            "back.png").resize((30, 30), Image.ANTIALIAS))

        addTopLevel = Toplevel()
        addTopLevel.title("Add Employee")
        addTopLevel.geometry('%dx%d+%d+%d' % (250, 700, 600, 70))
        addTopLevel.resizable(0, 0)

        

        nameTextField = TextField(addTopLevel, "Name", 25, 15, 5, 5, "", tk.TOP, tk.TOP)
        nameError = tk.Message(addTopLevel, text="",
                                  width=200, foreground="red")
        nameError.pack()
        ageTextField = TextField(addTopLevel, "Age", 25, 15, 5, 5, "", tk.TOP, tk.TOP)
        ageError = tk.Message(addTopLevel, text="",
                                  width=200, foreground="red")
        ageError.pack()                         
        jobTextField = TextField(addTopLevel, "Job", 25, 15, 5, 5, "", tk.TOP, tk.TOP)
        jobError = tk.Message(addTopLevel, text="",
                                  width=200, foreground="red")
        jobError.pack()                         

        emailTextField = TextField(addTopLevel, "Email", 25, 15, 5, 5, "", tk.TOP, tk.TOP)
        emailError = tk.Message(addTopLevel, text="",  
                                width=200, foreground="red")
        emailError.pack()                         

        genderTextField = TextField(addTopLevel, "Gender", 25, 15, 5, 5, "", tk.TOP, tk.TOP)
        genderError = tk.Message(addTopLevel, text="",
                                  width=200, foreground="red")
        genderError.pack()                         

        mobileTextField = TextField(addTopLevel, "Mobile", 25, 15, 5, 5, "", tk.TOP, tk.TOP)
        mobileError = tk.Message(addTopLevel, text="",
                                  width=200, foreground="red")
        mobileError.pack()                          
        addressTextField = TextField(addTopLevel, "Address", 25, 15,
                             5, 5, "", tk.TOP, tk.TOP)
        addressError = tk.Message(addTopLevel, text="",
                                  width=200, foreground="red")

        addressError.pack()

        databaseError = tk.Message(addTopLevel, text="",
                                  width=200, foreground="red")

        databaseError.pack()

        
        self.ButtonWrapper = ttk.Frame(addTopLevel)
        self.ButtonWrapper.pack(anchor='center', pady=10)
        self.saveButton = customtkinter.CTkButton(self.ButtonWrapper, image=saveIcon, text="", width=25, height=25,
                                                   command=lambda: self.validateEmployee(user, nameError, ageError, jobError, emailError, genderError, mobileError, addressError, nameTextField.get_value(), ageTextField.get_value(), jobTextField.get_value(), emailTextField.get_value(), genderTextField.get_value(), mobileTextField.get_value(), addressTextField.get_value(), databaseError=databaseError, id='', query='add'), compound="right", fg_color="#fafafa", hover_color="#fafafa")
        self.saveButton.pack(side='right', padx=15)

        self.backButton = customtkinter.CTkButton(self.ButtonWrapper, image=backIcon, text="", width=25, height=25,
                                                    command=lambda: self.dashboard(user), compound="right", fg_color="#fafafa", hover_color="#fafafa")
        self.backButton.pack(side='left')

    def confirmPopup(self, parent, title, messege, confirmCommand, cancelCommand):
        topLevel = Toplevel(parent)

        topLevel.geometry('%dx%d+%d+%d' % (400, 150, 550, 300))
        topLevel.title(title)
        topLevel.resizable(0, 0)

        self.wrapperFrame = ttk.Frame(topLevel, width=300, height=300)
        self.wrapperFrame.pack(side="bottom", anchor='ne', pady=10)
        Label(topLevel, text=messege, font=('calibri 13')).pack(
            side="left", anchor="c", padx=35)

        self.confirmButton = customtkinter.CTkButton(self.wrapperFrame, command=confirmCommand,
                                                     text="Confirm", text_font=6, fg_color="red" if title == 'Delete' else '#305af2', hover_color="red" if title == 'Delete' else '#305af2', text_color="#fff", width=20)
        self.confirmButton.pack(side='left', padx=5)
        self.cancelButton = customtkinter.CTkButton(self.wrapperFrame, command=cancelCommand,
                                                    text="Cancel", text_font=6, fg_color="#E2E5DE", hover_color="#E2E5DE", text_color='black', width=15)
        self.cancelButton.pack(side='right', padx=5)
   
    ############# Helper Functions #############

    def getdata(self):
        x = self.employeesTable.selection()
        y = self.employeesTable.item(x)['values']
        return y
 
    def auth(self, errorMessage, username, password):
        cursor.execute(
            "SELECT * from users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchall()
        if user:
            self.dashboard(user)
        else:
            errorMessage["text"] = "Invalid Username or Password"


root = tk.Tk()
root.title('HR Management System')
root.geometry("1200x800")
App(root)

root.mainloop()