# adapted from http://wiki.tcl.tk/%0920152
import tkinter as tk
from tkinter import ttk
from emoji import emojize


import sv_ttk

class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x800")
        root.title('HR Management System')
        root.geometry("1200x800")
        # Import the tcl file
        # root.tk.call('source', 'forest-dark.tcl')

        # Set the theme with the theme_use method
        # ttk.Style().theme_use('forest-dark')
        theme ="dark"
        sv_ttk.set_theme(theme)
        self.login()
    
    def login(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame1 = ttk.Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.reg_txt = ttk.Label(self.frame1, text='login')
        self.reg_txt.pack()
        self.register_btn = ttk.Button(self.frame1, text="Sign in", command=self.register)
        self.register_btn.pack()
        sv_ttk.set_theme("dark")

    
    def register(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = ttk.Frame(self.master)
        self.text2 = tk.Label(self.frame2, text="Welcome Raji 👋",font = ('calibri', 33))
        self.text2.pack(side="left" )

        # self.button = self.button(self.frame2, text='Add' , command=edit)
        # self.button.pack(side="right", padx=10)
        self.button = ttk.Button(self.frame2, text="Sign Out", command=self.login)
        self.button.pack(side="right", padx=10)



        self.button = ttk.Button(self.frame2, text="Add HR")
        self.button.pack(side="right")

        self.button = ttk.Button(self.frame2, text="Add Employee")
        self.button.pack(side="right", padx=10)


        self.accentbutton = ttk.Button(self.frame2, text="Accentbutton", style="Accent.TButton")


        self.accentbutton.pack(side="right", padx=10)

        self.frame1 = ttk.Frame(root, padding=10)




        # style = ttk.Style()
        # style.configure("mystyle.Treeview",font=('calibri',13),rowheight=50)
        # style.configure("mystyle.Treeview.Heading",font=('calibri',13))
        self.tv = ttk.Treeview(self.frame1, columns=(1,2,3,4,5,6,7,8))
        self.tv.pack(fill="both",padx=20, pady=20)

        self.tv.heading("1", text="ID")
        self.tv.column("1", width="40")
        self.tv.heading("2", text="Name")
        self.tv.column("2", width="140")
        self.tv.heading("3", text="Age")
        self.tv.column("3", width="50")
        self.tv.heading("4", text="Job")
        self.tv.column("4", width="120")
        self.tv.heading("5", text="Email")
        self.tv.column("5", width="150")
        self.tv.heading("6", text="Gender")
        self.tv.column("6", width="90")
        self.tv.heading("7", text="Mobile")
        self.tv.column("7", width="150")
        self.tv.heading("8", text="Address")
        self.tv.column("8", width="150")
        self.tv['show']= 'headings'

        self.tv.insert('', 1,values=('1', 'Mohanad', '22', "Software Engineer", "mohanadsafwat@icloud.com", "Male", "01022944586", "Gamal Abd El-Naser"))

        # self.tv.place(x=1,y=1)
        # text1 = tk.Text(self.frame1, borderwidth=0, highlightthickness=0, wrap="word",
        #                 width=40, height=4)
        # text1.pack(fill="both", expand=True
        # )
        # text1.bind("<FocusIn>", lambda event: self.frame1.state(["focus"]))
        # text1.bind("<FocusOut>", lambda event: self.frame1.state(["!focus"]))
        # text1.insert("end", "This widget has the focus")



        self.frame2.pack(side="top", fill="x", padx=20, pady=10)

        self.frame1.pack(side="top", fill="x", padx=20, pady=10)

     
        sv_ttk.set_theme("dark")



root = tk.Tk()
app(root)









root.mainloop()