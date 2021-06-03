from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle

class Movie:
    def __init__(self,winmovie):
        self.winmovie=winmovie
        self.winmovie.title("Movies Details")
        self.winmovie.geometry("1350x750+0+0")
        #self.winmovie.config(bg="chocolate1")
        self.bg_ic_mov=ImageTk.PhotoImage(file="back7lines.png")
        tit=Label(self.winmovie,image=self.bg_ic_mov).pack()
        
        title=Label(self.winmovie,text="Movies Database Management Section",bd=10,relief=GROOVE,font=("times new roman",25,"bold"),bg="dodgerblue2",fg="orange")
        title.place(x=0,y=0,relwidth=1)
      
        #variables
        self.movieid_var=StringVar()
        self.moviename_var=StringVar()
        self.movietype_var=StringVar()
        self.movierdate=StringVar()
        self.movieactor_var=StringVar()
        self.movieactress_var=StringVar()
        self.movielength_var=StringVar()
        self.movierating_var=StringVar()

        self.search_by_var=StringVar()
        self.search_txt_var=StringVar()
        
        #LeftSideFrame      
        F1=Frame(self.winmovie,bd=4,relief=RIDGE,bg="dodgerblue3")
        F1.place(x=10,y=90,width=450,height=600)
        
        m_title=Label(F1,text="Manage Movies     ",font=("cambria",20,"bold"),fg="orange2",bg='dodgerblue3')
        m_title.grid(row=0,column=0,pady=10)
        
        lbl_id=Label(F1,text="Movie ID *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_id.grid(row=1,column=0,pady=5,padx=5,sticky="w")
        
        txt_id=Entry(F1,font=("times new roman",12,"bold"),textvariable=self.movieid_var,relief=GROOVE,bd=5)
        txt_id.grid(row=1,column=1,pady=5,padx=5,sticky="w")
        
        lbl_name=Label(F1,text="Name *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_name.grid(row=2,column=0,pady=5,padx=5,sticky="w")
        
        txt_name=Entry(F1,textvariable=self.moviename_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_name.grid(row=2,column=1,pady=5,padx=5,sticky="w")
        
        lbl_type=Label(F1,text="Type *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_type.grid(row=3,column=0,pady=5,padx=5,sticky="w")
        
        combo_type=ttk.Combobox(F1,width=18,textvariable=self.movietype_var,font=("times new roman",12,"bold"),state="readonly")
        combo_type["value"]=('ROMANTIC','ACTION', 'COMEDY', 'HORROR', 'SCIENCE FICTION','OTHER')
        combo_type.grid(row=3,column=1,padx=5,pady=5)

        lbl_rdate=Label(F1,text="Release Date *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_rdate.grid(row=4,column=0,pady=5,padx=5,sticky="w")
        
        txt_rdate=Entry(F1,textvariable=self.movierdate,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_rdate.grid(row=4,column=1,pady=5,padx=5,sticky="w")
        
        lbl_actor=Label(F1,text="Hero *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_actor.grid(row=5,column=0,pady=5,padx=5,sticky="w")
        
        txt_actor=Entry(F1,textvariable=self.movieactor_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_actor.grid(row=5,column=1,pady=5,padx=5,sticky="w")    
        
        
        lbl_actress=Label(F1,text="Heroine *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_actress.grid(row=6,column=0,pady=5,padx=5,sticky="w")
        
        txt_actress=Entry(F1,textvariable=self.movieactress_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_actress.grid(row=6,column=1,pady=5,padx=5,sticky="w")
        
        lbl_length=Label(F1,text="Length(in min)",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_length.grid(row=7,column=0,pady=5,padx=5,sticky="w")
        
        txt_length=Entry(F1,textvariable=self.movielength_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_length.grid(row=7,column=1,pady=5,padx=5,sticky="w")

        lbl_rating=Label(F1,text="Rating",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_rating.grid(row=8,column=0,pady=5,padx=5,sticky="w")
        
        txt_rating=Entry(F1,textvariable=self.movierating_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_rating.grid(row=8,column=1,pady=5,padx=5,sticky="w")
        
        
        
        #BUttonFrame
        F3=Frame(F1,bd=4,relief=RIDGE,bg="crimson",padx=10)
        F3.place(x=14,y=460,width=420)
        
        
        Addbtn=Button(F3,text="Insert",width=10,font="calibri 10 bold",fg="crimson",command=self.add_students).grid(row=0,column=0,padx=10,pady=5)
        Uptbtn=Button(F3,text="Update",width=10,font="calibri 10 bold",fg="crimson",command=self.update_detail).grid(row=0,column=1,padx=10,pady=5)
        Delebtn=Button(F3,text="Delete",width=10,font="calibri 10 bold",fg="crimson",command=self.delete_data).grid(row=0,column=2,padx=10,pady=5)
        Clebtn=Button(F3,text="Clear",font="calibri 10 bold",fg="crimson",command= self.clear,width=10).grid(row=0,column=3,padx=10,pady=5)

        #RightSideFrame      
        F2=Frame(self.winmovie,bd=4,relief=RIDGE,bg="dodgerblue3")
        F2.place(x=500,y=90,width=830,height=600)
        
        lbl_sear=Label(F2,text="Search By",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_sear.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        combo_sear=ttk.Combobox(F2,width=15,textvariable=self.search_by_var,font=("times new roman",12,"bold"),state="readonly")
        combo_sear["value"]=("MOVIEID","MOVIENAME","MOVIETYPE")
        combo_sear.grid(row=0,column=1,padx=10,pady=10)
        
        txt_sear=Entry(F2,width=15,textvariable=self.search_txt_var,font=("times new roman",10,"bold"),relief=GROOVE,bd=5)
        txt_sear.grid(row=0,column=2,pady=10,padx=20,sticky="w")
      
        searbtn=Button(F2,text="Search",width=14,font="calibri 10 bold",command=self.search_data).grid(row=0,column=3,padx=10,pady=5)
        showallbtn=Button(F2,text="SHOW ALL",width=14,bg="orange",font="times 10 bold",fg="crimson",command=self.fetch_data).grid(row=0,column=4,padx=10,pady=5)
        
        
        #TreeviewFrame
        F4=Frame(F2,bd=4,relief=RIDGE,bg="dodgerblue2")
        F4.place(x=10,y=55,width=760,height=400)   
        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
        
        self.Movie_Table=ttk.Treeview(F4,columns=("ID","NAME","TYPE","RELEASE DATE","HEROES","HEROINES","LENGTH","RATING"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Movie_Table.xview)

        
        style = ttk.Style()
        style.configure("Treeview.Heading", font="rockwell 10 bold")
        style.theme_use("vista")
        #print(style.theme_names(('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')))
        #table
        scroll_y.config(command=self.Movie_Table.yview)
        self.Movie_Table.heading("ID",text="ID")
        self.Movie_Table.heading("NAME",text="NAME")
        self.Movie_Table.heading("TYPE",text="TYPE")
        self.Movie_Table.heading("RELEASE DATE",text="RELEASE DATE")
        self.Movie_Table.heading("HEROES",text="HEROES")
        self.Movie_Table.heading("HEROINES",text="HEROINES")
        self.Movie_Table.heading("LENGTH",text="LENGTH")
        self.Movie_Table.heading("RATING",text="RATING")
        self.Movie_Table['show']="headings"
        self.Movie_Table.column("ID",width=80)
        self.Movie_Table.column("NAME",width=150)
        self.Movie_Table.column("TYPE",width=120)
        self.Movie_Table.column("RELEASE DATE",width=120)
        self.Movie_Table.column("HEROES",width=150)
        self.Movie_Table.column("HEROINES",width=150)
        self.Movie_Table.column("LENGTH",width=80)
        self.Movie_Table.column("RATING",width=80)
        self.Movie_Table.bind("<ButtonRelease-1>",self.get_pointer)
        
        
        self.Movie_Table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        
        Quibtn_mov=Button(F2,text="QUIT! & GO BACK",width=20,padx=6,pady=0,font="times 13 bold",fg="red",bg="darkgoldenrod2",relief=SUNKEN,bd=4,command= self.winmovie.destroy)
        Quibtn_mov.place(x=300,y=550)
        
        
    def add_students(self):
        if self.movieid_var.get()=="" or self.moviename_var.get()=="" or self.movieactor_var.get()=="" or self.movietype_var.get()=="" or self.movierdate.get()=="" or self.movieactress_var.get()=="" :#or self.movierating_var.get()=="" or self.movielength_var.get()=="" :
            messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.winmovie)
        else:
            I=self.movieid_var.get()
            N=self.moviename_var.get()
            T=self.movietype_var.get()
            D=self.movierdate.get()
            H= self.movieactor_var.get()
            A=self.movieactress_var.get()
            L=eval(self.movielength_var.get())
            R=eval(self.movierating_var.get())
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            cur.execute("INSERT INTO Movie_Details VALUES (:1,:2,:3,:4,:5,:6,:7,:8)", (I,N,T,D,H,A,L,R))
            con.commit()
            self.fetch_data()
            messagebox.showinfo("Success","Record has been Inserted Successfully",parent=self.winmovie)
            #self.clear()
            con.close()

    def fetch_data(self):
        con=cx_Oracle.connect("mpsingh/mp")
        cur=con.cursor()
        cur.execute("select * from Movie_Details")
        rows = cur.fetchall()
        if (rows)!=0:
            self.Movie_Table.delete(*self.Movie_Table.get_children())
            for row in rows:
                self.Movie_Table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        if self.movieid_var.get()=="" or self.moviename_var.get()=="" or self.movieactor_var.get()=="" or self.movietype_var.get()=="" or self.movierdate.get()=="" or self.movieactress_var.get()=="" :  #or self.movierating_var.get()=="" or self.movielength_var.get()=="" :
            messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.winmovie)
        else:
            self.movieid_var.set('')
            self.moviename_var.set('')
            self.movietype_var.set('')
            self.movierdate.set('')
            self.movieactor_var.set('')
            self.movieactress_var.set('')
            self.movielength_var.set('')
            self.movierating_var.set('')
            messagebox.showinfo("Success","Fields Cleared Successfully",parent =self.winmovie)


    def get_pointer(self,event):
        cursor_row=self.Movie_Table.focus()
        contents=self.Movie_Table.item(cursor_row)
        row=contents['values']
        self.movieid_var.set(row[0])
        self.moviename_var.set(row[1])
        self.movietype_var.set(row[2])
        self.movierdate.set(row[3])
        self.movieactor_var.set(row[4])
        self.movieactress_var.set(row[5])
        self.movielength_var.set(row[6])
        self.movierating_var.set(row[7])

    def update_detail(self):
        if self.movieid_var.get()=="" or self.moviename_var.get()=="" or self.movieactor_var.get()=="" or self.movietype_var.get()=="" or self.movierdate.get()=="" or self.movieactress_var.get()=="" :#or self.movierating_var.get()=="" or self.movielength_var.get()=="" :
            messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.winmovie)
        else:
            I=self.movieid_var.get()
            N=self.moviename_var.get()
            T=self.movietype_var.get()
            D=self.movierdate.get()
            H= self.movieactor_var.get()
            A=self.movieactress_var.get()
            L=eval(self.movielength_var.get())
            R=eval(self.movierating_var.get())
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            sql="UPDATE MOVIE_DETAILS SET MOVIENAME=:2,MOVIETYPE=:3,MOVIERELEASINGDATE=:4,MOVIEACTOR=:5,MOVIEACTRESS=:6,MOVIELENGTH=:7,MOVIERATING=:8 where MOVIEID=:1"
            cur.execute(sql,(N,T,D,H,A,L,R,I))
            con.commit()
            self.fetch_data()
            messagebox.showinfo("Success","Record Updated Successfully",parent=self.winmovie)
            #self.clear()
            con.close()


    def delete_data(self):

        I=self.movieid_var.get()
        if I=="":
            messagebox.showerror("Error","Movie ID is Required to Delete the record!!",parent=self.winmovie)
        else:
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            cur.execute("Delete From Movie_Details where Movieid ='%s'"%self.movieid_var.get())
            #rows = cur.fetchall()
            con.commit()
            con.close()
            self.fetch_data()
            messagebox.showinfo("Success","Record Deleted Successfully",parent=self.winmovie)
            #self.clear()

    def search_data(self):
        con=cx_Oracle.connect("mpsingh/mp")
        cur=con.cursor()
        
        cur.execute("select * from Movie_Details where "+str(self.search_by_var.get())+" LIKE '%"+str(self.search_txt_var.get()+"%'"))
        rows = cur.fetchall()
        if (rows)!=0:
            self.Movie_Table.delete(*self.Movie_Table.get_children())
            for row in rows:
                self.Movie_Table.insert('',END,values=row)
            con.commit()
        con.close()

    #parents
            
if __name__ =="main":    
    winmovie=Tk()
    ob=Movie(winmovie)
    winmovie.mainloop()
