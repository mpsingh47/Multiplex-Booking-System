from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
import cx_Oracle
class Ticket:
    def __init__(self,wintick):
        self.wintick=wintick
        
        wintick.title("Ticket Details")
        wintick.geometry("1350x750+0+0")

        self.bg_ic_tick=ImageTk.PhotoImage(file="back7lines.png")
        tit=Label(self.wintick,image=self.bg_ic_tick).pack()
                
        title=Label(wintick,text="Ticket Database Management Section",bd=10,relief=GROOVE,font=("times new roman",25,"bold"),bg="dodgerblue2",fg="orange")
        title.place(x=0,y=0,relwidth=1)
        
        self.tickid_var=StringVar()
        self.tickcustid_var=StringVar()
        self.tickmovid_var=StringVar()
        self.tithrid_var=StringVar()
        self.tickdate_var=StringVar()
        self.tickperson_var=StringVar()
        self.tickextra_var=StringVar()
        
        self.search_byy_var=StringVar()
        self.search_txxt_var=StringVar()
        
        #LeftFrame
        F1=Frame(wintick,bd=4,relief=RIDGE,bg="dodgerblue2")
        F1.place(x=10,y=80,width=450,height=600)
            
        m_title=Label(F1,text="Manage Tickets",font=("times new roman",20,"bold"),bg="dodgerblue2",fg="orange2")
        m_title.grid(row=0,column=0,pady=10)
            
        lbl_cid=Label(F1,text="Ticket ID ",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cid.grid(row=1,column=0,pady=5,padx=5,sticky="w")
            
        txt_cid=Entry(F1,font=("times new roman",12,"bold"),textvariable=self.tickid_var,relief=GROOVE,bd=5)
        txt_cid.grid(row=1,column=1,pady=5,padx=5,sticky="w")
        
        lbl_cname=Label(F1,text="Customer ID *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cname.grid(row=2,column=0,pady=5,padx=5,sticky="w")
            
        txt_cname=Entry(F1,textvariable=self.tickcustid_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_cname.grid(row=2,column=1,pady=5,padx=5,sticky="w")
            
        lbl_cphone=Label(F1,text="Movie ID *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cphone.grid(row=3,column=0,pady=5,padx=5,sticky="w")
            
        txt_cphone=Entry(F1,textvariable=self.tickmovid_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_cphone.grid(row=3,column=1,pady=5,padx=5,sticky="w")
        
        lbl_cemail=Label(F1,text="Theatre ID *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cemail.grid(row=4,column=0,pady=5,padx=5,sticky="w")
            
        txt_cemail=Entry(F1,textvariable=self.tithrid_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_cemail.grid(row=4,column=1,pady=5,padx=5,sticky="w")
        
        lbl_cgen=Label(F1,text="Show Date *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cgen.grid(row=5,column=0,pady=5,padx=5,sticky="w")
            
        txt_cloc=Entry(F1,textvariable=self.tickdate_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_cloc.grid(row=5,column=1,pady=5,padx=5,sticky="w")
            
        lbl_cloc=Label(F1,text="No. Of Persons *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cloc.grid(row=6,column=0,pady=5,padx=5,sticky="w")
            
        combo_type=ttk.Combobox(F1,width=18,textvariable= self.tickperson_var ,font=("times new roman",12,"bold"),state="readonly")
        combo_type["value"]=('1','2','3','4')
        combo_type.grid(row=6,column=1,padx=5,pady=5)
            
        lbl_extra=Label(F1,text="Extra Meal *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_extra.grid(row=7,column=0,pady=5,padx=5,sticky="w")
            
        combo_extratype=ttk.Combobox(F1,width=18,textvariable= self.tickextra_var ,font=("times new roman",12,"bold"),state="readonly")
        combo_extratype["value"]=('YES','NO')
        combo_extratype.grid(row=7,column=1,padx=5,pady=5)

        F3=Frame(F1,bd=4,relief=RIDGE,bg="crimson",padx=10)
        F3.place(x=14,y=450,width=420)
            
            
        Addbtn=Button(F3,text="Insert",bg="mediumpurple1",font="calibri 10 bold",width=10,command=self.add_tick).grid(row=0,column=0,padx=10,pady=5)
        Uptbtn=Button(F3,text="Update",bg="mediumpurple1",font="calibri 10 bold",width=10,command=self.update_tick).grid(row=0,column=1,padx=10,pady=5)
        Delebtn=Button(F3,text="Delete",bg="mediumpurple1",font="calibri 10 bold",width=10,command=self.delete_tick).grid(row=0,column=2,padx=10,pady=5)
        Cletn=Button(F3,text="Clear",bg="mediumpurple1",font="calibri 10 bold",width=10,command=self.clear_da).grid(row=0,column=3,padx=10,pady=5)
        

        #RightFrame
        F2=Frame(wintick,bd=4,relief=RIDGE,bg="dodgerblue2")
        F2.place(x=500,y=80,width=830,height=600)
            
        lbl_sear=Label(F2,text="Search By",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_sear.grid(row=0,column=0,pady=10,padx=20,sticky="w")
            
        combo_sear=ttk.Combobox(F2,width=15,font=("times new roman",12,"bold"),textvariable=self.search_byy_var,state="readonly")
        combo_sear["value"]=("TICKETID","CUSTOMERID","MOVIEID","THEATREID")
        combo_sear.grid(row=0,column=1,padx=10,pady=10)
            
        txt_sear=Entry(F2,width=15,font=("times new roman",10,"bold"),relief=GROOVE,bd=5,textvariable=self.search_txxt_var)
        txt_sear.grid(row=0,column=2,pady=10,padx=20,sticky="w")
          
        sebtn=Button(F2,text="Search",font=("times new roman",10,"bold"),width=15,command=self.search_da).grid(row=0,column=3,padx=10,pady=5)
        shallbtn=Button(F2,text="SHOW ALL",bg="orange",font="times 10 bold",fg="crimson",width=15,command=self.fetch_data3).grid(row=0,column=4,padx=10,pady=5)
        
        F4=Frame(F2,bd=4,relief=RIDGE,bg="dodgerblue2")
        F4.place(x=10,y=65,width=760,height=400)   
        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
            
        self.Ticket_Table=ttk.Treeview(F4,columns=("TICKET ID","CUSTOMER ID","MOVIE ID","THEATRE ID","SHOW DATE","NO. OF PERSONS","EXTRA SNACKS"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        style = ttk.Style()
        style.configure("Treeview.Heading", font="rockwell 10 bold")
        style.theme_use("vista")     

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Ticket_Table.xview)

        #table
        scroll_y.config(command=self.Ticket_Table.yview)
        self.Ticket_Table.heading("TICKET ID",text="TICKET ID")
        self.Ticket_Table.heading("CUSTOMER ID",text="CUSTOMER ID")
        self.Ticket_Table.heading("MOVIE ID",text="MOVIE ID")
        self.Ticket_Table.heading("THEATRE ID",text="THEATRE ID")
        self.Ticket_Table.heading("SHOW DATE",text="SHOW DATE")
        self.Ticket_Table.heading("NO. OF PERSONS",text="NO. OF PERSONS")
        self.Ticket_Table.heading("EXTRA SNACKS",text="EXTRA SNACKS")
        self.Ticket_Table['show']="headings"
        self.Ticket_Table.column("TICKET ID",width=100)
        self.Ticket_Table.column("CUSTOMER ID",width=100)
        self.Ticket_Table.column("MOVIE ID",width=100)
        self.Ticket_Table.column("THEATRE ID",width=100)
        self.Ticket_Table.column("SHOW DATE",width=100)
        self.Ticket_Table.column("NO. OF PERSONS",width=100)
        self.Ticket_Table.column("EXTRA SNACKS",width=100)
        self.Ticket_Table.bind("<ButtonRelease-1>",self.get_foco)
            
        self.Ticket_Table.pack(fill=BOTH,expand=1)
        self.fetch_data3()

        Quibtn_mov=Button(F2,text="QUIT! & GO BACK",width=20,padx=6,pady=0,font="times 13 bold",fg="red",bg="darkgoldenrod2",relief=SUNKEN,bd=4,command= self.wintick.destroy)
        Quibtn_mov.place(x=300,y=550)

    def fetch_data3(self):
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            cur.execute("select * from TicketBooking_Details")
            rows = cur.fetchall()
            if (rows)!=0:
                self.Ticket_Table.delete(*self.Ticket_Table.get_children())
                for row in rows:
                    self.Ticket_Table.insert('',END,values=row)
                con.commit()
            con.close()

    def clear_da(self):
            I=self.tickid_var.get()
            C=self.tickcustid_var.get()
            M=self.tickmovid_var.get()
            T=self.tithrid_var.get()
            D=self.tickdate_var.get()
            P=self.tickperson_var.get()
            E=self.tickextra_var.get()

            if (I=='' or C=='' or M=='' or T=='' or D=='' or P=='' or E==''):
                messagebox.showerror("Error","Can't Clear\nAll Fields Are Required!!!",parent=self.wintick)
            else:
                self.tickid_var.set('')
                self.tickcustid_var.set('')
                self.tickmovid_var.set('')
                self.tithrid_var.set('')
                self.tickdate_var.set('')
                self.tickperson_var.set('')
                self.tickextra_var.set('')
                messagebox.showinfo("Success","Fields Cleared Successfully",parent=self.wintick)

    def get_foco(self,event):
            cursor_row=self.Ticket_Table.focus()
            content_s=self.Ticket_Table.item(cursor_row)
            #print(content_s)
            row=content_s['values']
            self.tickid_var.set(row[0])
            self.tickcustid_var.set(row[1])
            self.tickmovid_var.set(row[2])
            self.tithrid_var.set(row[3])
            self.tickdate_var.set(row[4])
            self.tickperson_var.set(row[5])
            self.tickextra_var.set(row[6])

    def add_tick(self):
        I=self.tickid_var.get()
        C=self.tickcustid_var.get()
        M=self.tickmovid_var.get()
        T=self.tithrid_var.get()
        D=self.tickdate_var.get()
        P=self.tickperson_var.get()
        E=self.tickextra_var.get()

        if (I=='' or C=='' or M=='' or T=='' or D=='' or P=='' or E==''):
            messagebox.showerror("Error","All Fields Are Required!!!",parent=self.wintick)
        else:
            try:
                P=int(P)
                con=cx_Oracle.connect("mpsingh/mp")
                cur=con.cursor()
                cur.execute("INSERT INTO TicketBooking_Details VALUES (:1,:2,:3,:4,:5,:6,:7)",(I,C,M,T,D,P,E))
                con.commit()
                self.fetch_data3()
                messagebox.showinfo("Success","Record has been Added Successfull",parent=self.wintick)
                #self.clear_da()
                con.close()
            except cx_Oracle.IntegrityError :
                messagebox.showerror("Error","Can't Insert Data\nAll foreign IDs(CUSTOMER ID, MOVIE ID, THEATRE ID)\nshould be present in their respective Tables",parent=self.wintick)

    def update_tick(self):
        I=self.tickid_var.get()
        C=self.tickcustid_var.get()
        M=self.tickmovid_var.get()
        T=self.tithrid_var.get()
        D=self.tickdate_var.get()
        P=self.tickperson_var.get()
        E=self.tickextra_var.get()

        if (I=='' or C=='' or M=='' or T=='' or D=='' or P=='' or E==''):
            messagebox.showerror("Error","All Fields Are Required!!!",parent=self.wintick)
        else:
            try:
                P=int(P)
                con=cx_Oracle.connect("mpsingh/mp")
                cur=con.cursor()
                sql="UPDATE TicketBooking_details SET CUSTOMERID=:2,MOVIEID=:3,THEATREID=:4,SHOWDATE=:5, PERSONSALLOWED=:6,EXTRAMEAL=:7 where TICKETID=:1"
                cur.execute(sql,(C,M,T,D,P,E,I))
                con.commit()
                self.fetch_data3()
                messagebox.showinfo("Success","Record Updated Successfully",parent=self.wintick)
                #self.clear_da()
                con.close()
            except cx_Oracle.IntegrityError :
                messagebox.showerror("Error","All IDs should be present in\ntheir respective Tables",parent=self.wintick)
        
    def delete_tick(self):
        I=self.tickid_var.get()
        if I=="":
            messagebox.showerror("Error","Ticket ID is Required to Delete !!",parent=self.wintick)
        else:
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            cur.execute("Delete From  TicketBooking_Details where TICKETID='%s'"%I)
            con.commit()
            con.close()
            self.fetch_data3()
            messagebox.showinfo("Success","Record Deleted Successfully",parent=self.wintick)
            #self.clear_da()

    def search_da(self):
        con=cx_Oracle.connect("mpsingh/mp")
        cur=con.cursor()
        
        cur.execute("select * from TicketBooking_Details where "+str(self.search_byy_var.get())+" LIKE '%"+str(self.search_txxt_var.get()+"%'"))
        rows = cur.fetchall()
        if (rows)!=0:
            self.Ticket_Table.delete(*self.Ticket_Table.get_children())
            for row in rows:
                self.Ticket_Table.insert('',END,values=row)
            con.commit()
        con.close()
  
    
if __name__ == "main":
    wintick=Tk()    
    ob=Ticket(wintick)
    wintick.mainloop()
