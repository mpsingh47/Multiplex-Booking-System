from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login():
    def __init__(self,root):
        self.root=root
        self.root.title("Login Screen")
        self.root.geometry("1350x750+0+0")
        
        
        self.bg_icon=ImageTk.PhotoImage(file="back6.png")
        self.user_icon=PhotoImage(file="main.png")
        self.pass_icon=PhotoImage(file="pass.png")
        self.logo_icon=ImageTk.PhotoImage(file="useradmin.jpg")
        self.uname=StringVar()
        self.pass_=StringVar()
        self.uname_c=StringVar()
        self.pass_c=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        
        title=Label(self.root,text="*** Multiplex  Booking  System ***",font=("rockwell",40,"bold"),bg="royalblue1",fg="black",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
         
        
        Login_win_a=Frame(self.root,bg="slate blue",relief=SUNKEN,bd=10,padx=7)
        Login_win_a.place(x=100,y=100)

        logolbl=Label(Login_win_a,image=self.logo_icon,bd=0)
        logolbl.grid(row=0,columnspan=3,pady=20)
        #logolbl=Label(Login_win_a,text="Admin Login",font=("times new roman",20,"bold italic"),relief=RAISED,bg= 'chocolate2',fg='light cyan',bd=7)
        #logolbl.grid(row=0,columnspan=3,pady=15,ipadx=50)

        lbluser=Label(Login_win_a,text=" Username: ",fg="purple1",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_win_a,bd=5,textvariable=self.uname,relief=GROOVE,bg='gray69',font=("",15)).grid(row=1,column=1,padx=20)
        
        lblpass=Label(Login_win_a,text=" Password: ",fg="purple1",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_win_a,bg='gray64',bd=5,textvariable=self.pass_,show='*',relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
         
        btn_log=Button(Login_win_a,text="Login",width=15,command=self.alogin,font=("cambria",15,"bold"),bg="olivedrab1",fg="firebrick3").grid(row=3,column=1,pady=2)

     
        btnexit = Button (self.root , text ='E\nX\nI\nT', font=("times new roman",15,"bold"),bg='firebrick2' ,bd =6, command = self.ext,padx=5).place(x=690,y=540)
        #btnexit.grid(row=6,column=2,padx=8,pady=8,sticky='nsew')

    def alogin(self):
        def is_valid_password(password):
            import hashlib
            password_hash = hashlib.sha256(password.encode("utf=8")).hexdigest()
            #return password_hash == "0300dc429eeb82775c426d87a5fd72c1bba7a35f56a4804df8b3c35c38df6813"
            return password_hash == "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
            return password_hash=='1234'
        if self.uname.get()=="" or self.pass_.get()=="" :
            messagebox.showerror("Error","All fields are required!!")
        elif self.uname.get()=="ACET" and is_valid_password(self.pass_.get()):
            #messagebox.showinfo("Successfull",f"Welcome {self.uname.get()}")  
            self.pass_.set("")
            self.admscr()
        else:
            messagebox.showerror("Error","Invalid Username or Password")
            #print('invalid')

    def ext(self):
        self.root.destroy()

    def admscr(self):
        from adminscreen import class_admin
        root4=Toplevel()
        ob4=class_admin(root4)
        root4.mainloop()

        
root=Tk()
obj=Login(root)
root.mainloop()
