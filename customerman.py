from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
import cx_Oracle
class Customer:
    def __init__(self,wincust):
        self.wincust=wincust
        
        wincust.title("Customer Details")
        wincust.geometry("1350x750+0+0")

        self.bg_ic_tick=ImageTk.PhotoImage(file="back7lines.png")
        tit=Label(self.wincust,image=self.bg_ic_tick).pack()
        
        
        title=Label(wincust,text="Customer Database Management Section",bd=10,relief=GROOVE,font=("times new roman",25,"bold"),bg="dodgerblue2",fg="orange")
        title.place(x=0,y=0,relwidth=1)
        
        
        
        self.custid_var=StringVar()
        self.custname_var=StringVar()
        self.custphone_var=StringVar()
        self.custemail_var=StringVar()
        self.custgender_var=StringVar()
        self.custloc_var=StringVar()
        
        self.search_byy_var=StringVar()
        self.search_txxt_var=StringVar()
        
        
        F1=Frame(wincust,bd=4,relief=RIDGE,bg="dodgerblue2")
        F1.place(x=10,y=80,width=450,height=600)
            
        m_title=Label(F1,text="Manage Customers",font=("times new roman",20,"bold"),bg="dodgerblue2",fg="orange2")
        m_title.grid(row=0,column=0,pady=10)
            
        lbl_cid=Label(F1,text="Customer ID *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cid.grid(row=1,column=0,pady=5,padx=5,sticky="w")
            
        txt_cid=Entry(F1,font=("times new roman",12,"bold"),textvariable=self.custid_var,relief=GROOVE,bd=5)
        txt_cid.grid(row=1,column=1,pady=5,padx=5,sticky="w")
        
        lbl_cname=Label(F1,text="Name *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cname.grid(row=2,column=0,pady=5,padx=5,sticky="w")
            
        txt_cname=Entry(F1,textvariable=self.custname_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_cname.grid(row=2,column=1,pady=5,padx=5,sticky="w")
            
        lbl_cphone=Label(F1,text="Phone No. *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cphone.grid(row=3,column=0,pady=5,padx=5,sticky="w")
            
        txt_cphone=Entry(F1,textvariable=self.custphone_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_cphone.grid(row=3,column=1,pady=5,padx=5,sticky="w")
        
        lbl_cemail=Label(F1,text="Email",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cemail.grid(row=4,column=0,pady=5,padx=5,sticky="w")
            
        txt_cemail=Entry(F1,textvariable=self.custemail_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_cemail.grid(row=4,column=1,pady=5,padx=5,sticky="w")
        
        lbl_cgen=Label(F1,text="Gender *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cgen.grid(row=5,column=0,pady=5,padx=5,sticky="w")
            
        combo_type=ttk.Combobox(F1,width=18,textvariable= self.custgender_var ,font=("times new roman",12,"bold"),state="readonly")
        combo_type["value"]=('MALE','FEMALE','OTHER')
        combo_type.grid(row=5,column=1,padx=5,pady=5)
            
        lbl_cloc=Label(F1,text="Location *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_cloc.grid(row=6,column=0,pady=5,padx=5,sticky="w")
            
        txt_cloc=Entry(F1,textvariable=self.custloc_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_cloc.grid(row=6,column=1,pady=5,padx=5,sticky="w")
            

        F3=Frame(F1,bd=4,relief=RIDGE,bg="crimson",padx=10)
        F3.place(x=14,y=460,width=420)
            
            
        Addbtn=Button(F3,text="Insert",bg="yellow2",font="calibri 10 bold",width=10,command=self.add_admsn).grid(row=0,column=0,padx=10,pady=5)
        Uptbtn=Button(F3,text="Update",bg="yellow2",font="calibri 10 bold",width=10,command=self.update_det).grid(row=0,column=1,padx=10,pady=5)
        Delebtn=Button(F3,text="Delete",bg="yellow2",font="calibri 10 bold",width=10,command=self.delete_dat).grid(row=0,column=2,padx=10,pady=5)
        Cletn=Button(F3,text="Clear",bg="yellow2",font="calibri 10 bold",width=10,command=self.clear_da).grid(row=0,column=3,padx=10,pady=5)
        

        F2=Frame(wincust,bd=4,relief=RIDGE,bg="dodgerblue2")
        F2.place(x=500,y=80,width=830,height=600)
            
        lbl_sear=Label(F2,text="Search By",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_sear.grid(row=0,column=0,pady=10,padx=20,sticky="w")
            
        combo_sear=ttk.Combobox(F2,width=15,font=("times new roman",12,"bold"),textvariable=self.search_byy_var,state="readonly")
        combo_sear["value"]=("CUSTOMERID","CUSTOMERNAME")
        combo_sear.grid(row=0,column=1,padx=10,pady=10)
            
        txt_sear=Entry(F2,width=15,font=("times new roman",10,"bold"),relief=GROOVE,bd=5,textvariable=self.search_txxt_var)
        txt_sear.grid(row=0,column=2,pady=10,padx=20,sticky="w")
          
        searbtn=Button(F2,text="Search",font=("times new roman",10,"bold"),width=15,command=self.search_da).grid(row=0,column=3,padx=10,pady=5)
        showalltn=Button(F2,text="ShowAll",bg="orange",font="times 10 bold",fg="crimson",width=15,command=self.fetch_data3).grid(row=0,column=4,padx=10,pady=5)
        
        
        
        F4=Frame(F2,bd=4,relief=RIDGE,bg="dodgerblue2")
        F4.place(x=10,y=65,width=760,height=400)   
        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
            
        self.Customer_Table=ttk.Treeview(F4,columns=("CUSTOMER ID","NAME","PHONE NO.","EMAIL","GENDER","LOCATION"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        style = ttk.Style()
        style.configure("Treeview.Heading", font="rockwell 10 bold")
        style.theme_use("vista")     

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Customer_Table.xview)

            #table
        scroll_y.config(command=self.Customer_Table.yview)
        self.Customer_Table.heading("CUSTOMER ID",text="CUSTOMER ID")
        self.Customer_Table.heading("NAME",text="NAME")
        self.Customer_Table.heading("PHONE NO.",text="PHONE NO.")
        self.Customer_Table.heading("EMAIL",text="EMAIL")
        self.Customer_Table.heading("GENDER",text="GENDER")
        self.Customer_Table.heading("LOCATION",text="LOCATION")
        self.Customer_Table['show']="headings"
        self.Customer_Table.column("CUSTOMER ID",width=100)
        self.Customer_Table.column("NAME",width=100)
        self.Customer_Table.column("PHONE NO.",width=100)
        self.Customer_Table.column("EMAIL",width=100)
        self.Customer_Table.column("GENDER",width=100)
        self.Customer_Table.column("LOCATION",width=100)
        self.Customer_Table.bind("<ButtonRelease-1>",self.get_foco)
        
            
        self.Customer_Table.pack(fill=BOTH,expand=1)
        self.fetch_data3()
        
        Quibtn_mov=Button(F2,text="QUIT! & GO BACK",width=20,padx=6,pady=0,font="times 13 bold",fg="red",bg="darkgoldenrod2",relief=SUNKEN,bd=4,command= self.wincust.destroy)
        Quibtn_mov.place(x=300,y=550)

    def fetch_data3(self):
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            cur.execute("select * from Customer_Details")
            rows = cur.fetchall()
            if (rows)!=0:
                self.Customer_Table.delete(*self.Customer_Table.get_children())
                for row in rows:
                    self.Customer_Table.insert('',END,values=row)
                con.commit()
            con.close()

    def clear_da(self):
            I=self.custid_var.get()
            N=self.custname_var.get()
            P=self.custphone_var.get()
            E=self.custemail_var.get()
            G=self.custgender_var.get()
            L=self.custloc_var.get()

            if (I=='' or N=='' or P=='' or E=='' or G=='' or L==''):
                messagebox.showerror("Error","Can't Clear\nAll Fields Are Required!!!",parent=self.wincust)
            else:
                self.custid_var.set('')
                self.custname_var.set('')
                self.custphone_var.set('')
                self.custemail_var.set('')
                self.custgender_var.set('')
                self.custloc_var.set('')
                messagebox.showinfo("Success","Fields Cleared Successfully",parent=self.wincust)

    def get_foco(self,event):
            cursor_row=self.Customer_Table.focus()
            content_s=self.Customer_Table.item(cursor_row)
            row=content_s['values']
            self.custid_var.set(row[0])
            self.custname_var.set(row[1])
            self.custphone_var.set(row[2])
            self.custemail_var.set(row[3])
            self.custgender_var.set(row[4])
            self.custloc_var.set(row[5])

    def add_admsn(self):
        I=self.custid_var.get()
        N=self.custname_var.get()
        P=self.custphone_var.get()
        E=self.custemail_var.get()
        G=self.custgender_var.get()
        L=self.custloc_var.get()

        if (I=='' or N=='' or P=='' or E=='' or G=='' or L==''):
            messagebox.showerror("Error","All Fields Are Required!!!",parent=self.wincust)
        else:
            P=int(self.custphone_var.get())
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            cur.execute("INSERT INTO Customer_Details VALUES (:1,:2,:3,:4,:5,:6)",(I,N,P,E,G,L))                                                               
            con.commit()
            self.fetch_data3()
            messagebox.showinfo("Success","Record has been Added Successfull",parent=self.wincust)
            #self.clear_da()
            con.close()
            

    def update_det(self):
        I=self.custid_var.get()
        N=self.custname_var.get()
        P=self.custphone_var.get()
        E=self.custemail_var.get()
        G=self.custgender_var.get()
        L=self.custloc_var.get()

        if (I=='' or N=='' or P=='' or E=='' or G=='' or L==''):
            messagebox.showerror("Error","All Fields Are Required!!!",parent=self.wincust)
        else:

            P=int(P)
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            sql="UPDATE Customer_details SET CUSTOMERNAME=:2,CUSTOMERPHONE=:3,CUSTOMEREMAIL=:4,CUSTOMERGENDER=:5, CUSTOMERLOCATION=:6 where CUSTOMERID=:1"
            cur.execute(sql,(N,P,E,G,L,I))
            con.commit()
            self.fetch_data3()
            messagebox.showinfo("Success","Record Updated Successfully",parent=self.wincust)
            #self.clear_da()
            con.close()
        

    def delete_dat(self):
        I=self.custid_var.get()
        if I=="":
            messagebox.showerror("Error","Customer ID is Required to Delete !!",parent=self.wintheatre)
        else:
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            cur.execute("Delete From  Customer_Details where CustomerID='%s'"%I)
            con.commit()
            con.close()
            self.fetch_data3()
            messagebox.showinfo("Success","Record Deleted Successfully",parent=self.wincust)
            #self.clear_da()


    def search_da(self):
        con=cx_Oracle.connect("mpsingh/mp")
        cur=con.cursor()
        
        cur.execute("select * from Customer_Details where "+str(self.search_byy_var.get())+" LIKE '%"+str(self.search_txxt_var.get()+"%'"))
        rows = cur.fetchall()
        if (rows)!=0:
            self.Customer_Table.delete(*self.Customer_Table.get_children())
            for row in rows:
                self.Customer_Table.insert('',END,values=row)
            con.commit()
        con.close()
  
    
if __name__ == "main":
     wincust=Tk()    
     ob=Customer(wincust)
     wincust.mainloop()
