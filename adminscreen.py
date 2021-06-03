from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
class class_admin:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Section")
        self.root.geometry("1350x750")
        
        self.bg_ic=ImageTk.PhotoImage(file="back3curtains.png")
        tit=Label(self.root,image=self.bg_ic).pack()

        
        title=Label(self.root,text="Multiplex Booking System",bd=10,relief=GROOVE,font=("magneto",30,"bold"),bg="firebrick2",fg="black")
        title.place(x=0,y=0,relwidth=1)

        weltitle=Label(self.root,text="Welcome ACET\nChoose What You Want To Do:-",font=("rockwell",25,"bold"),bg="white",fg="firebrick2",padx=200)
        weltitle.place(x=200,y=160)
        
                
        #tableBUtton
                
        F5=Frame(self.root,bd=7,relief=RIDGE,bg="orange2")
        F5.place(x=440,y=270)
         
        MovBtn=Button(F5,text="Manage Movies",fg='red',font="times 15 bold",width=15,command=self.movfun).grid(row=0,column=0,padx=20,pady=15)
        Thrbtn=Button(F5,text="Manage Theatre",width=15,fg='red',font="times 15 bold",command=self.thrfun).grid(row=0,column=1,padx=20,pady=15)
        Admbtn=Button(F5,text="Manage Customers",width=15,fg='red',font="times 15 bold",command=self.custfun).grid(row=2,column=0,padx=20,pady=15)
        Sectn=Button(F5,text="Manage Tickets",width=15,fg='red',font="times 15 bold",command=self.tickfun).grid(row=2,column=1,padx=20,pady=15)
        Thrbtn=Button(F5,text="Movies Poster",width=15,fg='red',font="times 15 bold",command=self.postfun).grid(row=3,column=0,padx=20,pady=15)
        quitbtn=Button(F5,text="Quit & Go Back",width=15,fg='red',font="times 15 bold",command=self.root.destroy).grid(row=3,column=1,padx=20,pady=15)

    def movfun(self):
        from movieman import Movie
        root0=Toplevel()
        obj=Movie(root0)
        root0.mainloop()

    def thrfun(self):
        from theatreman import Theatre
        root1=Toplevel()
        ob1=Theatre(root1)
        root1.mainloop()

    def custfun(self):
        from customerman import Customer
        root2=Toplevel()
        ob2=Customer(root2)
        root2.mainloop()

    def tickfun(self):
        from ticketman import Ticket
        root3=Toplevel()
        ob3=Ticket(root3)
        root3.mainloop()
    
    def postfun(self):
        from posterman import Poster
        root4=Toplevel()
        ob4=Poster(root4)
        root4.mainloop()

if __name__ =="main":    
    root=Tk()
    ob=class_admin(root)
    root.mainloop()