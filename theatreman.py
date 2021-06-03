from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
import cx_Oracle
class Theatre:
    def __init__(self,wintheatre):
            
        self.wintheatre=wintheatre
        self.wintheatre.title("Theatre Details")
        self.wintheatre.geometry("1350x750+0+0")
    
        self.bg_ic_thr=ImageTk.PhotoImage(file="back7lines.png")
        tit=Label(self.wintheatre,image=self.bg_ic_thr).pack()

        title=Label(self.wintheatre,text="Theatre Database Management Section",bd=10,relief=GROOVE,font=("times new roman",25,"bold"),bg="dodgerblue2",fg="orange")
        title.place(x=0,y=0,relwidth=1)

        self.Theatreid_var=StringVar()
        self.Thrname_var=StringVar()
        self.Thrtype_var=StringVar()
        self.Thrloc_var=StringVar()
        self.ThrMovid_var=StringVar()
        self.Thrshowprice_var=StringVar()
        self.Thrgst_var=StringVar()

        self.search_buy_var=StringVar()
        self.search_text_var=StringVar()        
    
        
        E1=Frame(wintheatre,bd=4,relief=RIDGE,bg="dodgerblue2")
        E1.place(x=10,y=80,width=450,height=600)
            
        m1_title=Label(E1,text="Manage Theatres",font=("times new roman",20,"bold"),fg="orange2",bg='dodgerblue2')
        m1_title.grid(row=0,column=0,pady=10)
            
        lbl_thid=Label(E1,text="Theatre ID *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_thid.grid(row=1,column=0,pady=5,padx=5,sticky="w")
            
        txt_thid=Entry(E1,font=("times new roman",12,"bold"),textvariable=self.Theatreid_var,relief=GROOVE,bd=5)
        txt_thid.grid(row=1,column=1,pady=5,padx=5,sticky="w")
        
        lbl_thname=Label(E1,text="Theatre Name *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_thname.grid(row=2,column=0,pady=5,padx=5,sticky="w")
            
        txt_thname=Entry(E1,textvariable=self.Thrname_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_thname.grid(row=2,column=1,pady=5,padx=5,sticky="w")
            
        lbl_thtype=Label(E1,text="Theatre Type *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_thtype.grid(row=3,column=0,pady=5,padx=5,sticky="w")
            
        combo_type=ttk.Combobox(E1,width=18,textvariable=self.Thrtype_var,font=("times new roman",12,"bold"),state="readonly")
        combo_type["value"]=('AC','NON-AC')
        combo_type.grid(row=3,column=1,padx=5,pady=5)
            
        lbl_thloc=Label(E1,text="Location *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_thloc.grid(row=4,column=0,pady=5,padx=5,sticky="w")
            
        txt_thloc=Entry(E1,textvariable=self.Thrloc_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_thloc.grid(row=4,column=1,pady=5,padx=5,sticky="w")

        lbl_thmovid=Label(E1,text="Latest MovieID *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_thmovid.grid(row=5,column=0,pady=5,padx=5,sticky="w")
            
        txt_thmovid=Entry(E1,textvariable=self.ThrMovid_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_thmovid.grid(row=5,column=1,pady=5,padx=5,sticky="w") 
        
            
        lbl_thprice=Label(E1,text="Show Price *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_thprice.grid(row=6,column=0,pady=5,padx=5,sticky="w")
            
        txt_thprice=Entry(E1,textvariable=self.Thrshowprice_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_thprice.grid(row=6,column=1,pady=5,padx=5,sticky="w")
                
        lbl_thgst=Label(E1,text="Theatre GST *",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_thgst.grid(row=7,column=0,pady=5,padx=5,sticky="w")
            
        txt_thgst=Entry(E1,textvariable=self.Thrgst_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_thgst.grid(row=7,column=1,pady=5,padx=5,sticky="w")

        
        E3=Frame(E1,bd=4,relief=RIDGE,bg="crimson",padx=10)
        E3.place(x=14,y=460,width=420)
            
            
        Addbtn1=Button(E3,text="Insert",width=10,bg="salmon1",font="calibri 10 bold",command=self.add_parents).grid(row=0,column=0,padx=10,pady=5)
        Uptbtn1=Button(E3,text="Update",width=10,bg="salmon1",font="calibri 10 bold",command=self.update_detai).grid(row=0,column=1,padx=10,pady=5)
        Delebtn1=Button(E3,text="Delete",width=10,bg="salmon1",font="calibri 10 bold",command=self.delete_dat).grid(row=0,column=2,padx=10,pady=5)
        Clebtn1=Button(E3,text="Clear",width=10,bg="salmon1",font="calibri 10 bold",command=self.clear_data).grid(row=0,column=3,padx=10,pady=5)

        E2=Frame(wintheatre,bd=4,relief=RIDGE,bg="dodgerblue2")
        E2.place(x=500,y=80,width=830,height=600)
            
        lbl_searc=Label(E2,text="Search By",font=("times new roman",18,"bold"),bg="orange",fg="crimson")
        lbl_searc.grid(row=0,column=0,pady=10,padx=20,sticky="w")
            
        combo_searc=ttk.Combobox(E2,width=15,textvariable=self.search_buy_var,font=("times new roman",12,"bold"),state="readonly")
        combo_searc["value"]=("THEATREID","THEATRETYPE")
        combo_searc.grid(row=0,column=1,padx=10,pady=10)
            
        txt_searc=Entry(E2,width=15,font=("times new roman",10,"bold"),textvariable=self.search_text_var,relief=GROOVE,bd=5)
        txt_searc.grid(row=0,column=2,pady=10,padx=20,sticky="w")
            
        searcbtn=Button(E2,text="Search",width=14,font="calibri 10 bold",command=self.search_dat).grid(row=0,column=3,padx=10,pady=5)
        showallbtn=Button(E2,text="SHOW ALL",width=14,bg="orange",font="times 10 bold",fg="crimson",command=self.fetch_data2).grid(row=0,column=4,padx=10,pady=5)
        
        
        
        E4=Frame(E2,bd=4,relief=RIDGE,bg="dodgerblue2")
        E4.place(x=10,y=65,width=760,height=400)   
        scroll_x=Scrollbar(E4,orient=HORIZONTAL)
        scroll_y=Scrollbar(E4,orient=VERTICAL)
            
        self.Theatre_Table=ttk.Treeview(E4,columns=("THEATRE ID","NAME","TYPE","LOCATION","LATEST MOVIE","SHOW PRICE","GST"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        style = ttk.Style()
        style.configure("Treeview.Heading", font="rockwell 10 bold")
        style.theme_use("vista")            
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Theatre_Table.xview)

            #table
        scroll_y.config(command=self.Theatre_Table.yview)
        self.Theatre_Table.heading("THEATRE ID",text="THEATRE ID")
        self.Theatre_Table.heading("NAME",text="NAME")
        self.Theatre_Table.heading("TYPE",text="TYPE")
        self.Theatre_Table.heading("LOCATION",text="LOCATION")
        self.Theatre_Table.heading("LATEST MOVIE",text="LATEST MOVIE")
        self.Theatre_Table.heading("SHOW PRICE",text="SHOW PRICE")
        self.Theatre_Table.heading("GST",text="GST")
        self.Theatre_Table['show']="headings"
        self.Theatre_Table.column("THEATRE ID",width=100)
        self.Theatre_Table.column("NAME",width=100)
        self.Theatre_Table.column("TYPE",width=100)
        self.Theatre_Table.column("LOCATION",width=100)
        self.Theatre_Table.column("LATEST MOVIE",width=100)
        self.Theatre_Table.column("SHOW PRICE",width=100)
        self.Theatre_Table.column("GST",width=100)
        self.Theatre_Table.bind("<ButtonRelease-1>",self.get_focus)
            
            
        self.Theatre_Table.pack(fill=BOTH,expand=1)
        self.fetch_data2()
        
        Quibtn_thr=Button(E2,text="QUIT! & GO BACK",width=20,padx=6,pady=0,font="times 13 bold",fg="red",bg="darkgoldenrod2",relief=SUNKEN,bd=4,command= self.wintheatre.destroy)
        Quibtn_thr.place(x=300,y=550)
            
    def add_parents(self):
            I=self.Theatreid_var.get()
            N=self.Thrname_var.get()
            T=self.Thrtype_var.get()
            L=self.Thrloc_var.get()
            M=self.ThrMovid_var.get()
            P=self.Thrshowprice_var.get()
            G=self.Thrgst_var.get()

            if (I=="" or N=="" or T=="" or L=="" or M==""  or P=="" or G=="") :
               messagebox.showerror("Error","All Fields Are Required!!!",parent=self.wintheatre)
            else:
                try:
                    P=float(self.Thrshowprice_var.get())
                    G=float(self.Thrgst_var.get())
                    con=cx_Oracle.connect("mpsingh/mp")
                    cur=con.cursor()
                    cur.execute("INSERT INTO theatre_details VALUES(:1,:2,:3,:4,:5,:6,:7)", (I,N,T,L,M,P,G))
                    con.commit()
                    self.fetch_data2()
                    messagebox.showinfo("Success","Record has been Added Successfull",parent=self.wintheatre)
                    #self.clear_data()
                    con.close()
                except cx_Oracle.IntegrityError as ie:
                    messagebox.showerror("Error"," Latest Movie Id \n should be present in\n table Movie_Details",parent=self.wintheatre)
                    

    def fetch_data2(self):
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            cur.execute("select * from Theatre_Details")
            rows = cur.fetchall()
            if (rows)!=0:
                self.Theatre_Table.delete(*self.Theatre_Table.get_children())
                for row in rows:
                    self.Theatre_Table.insert('',END,values=row)
                con.commit()
            con.close()


    def clear_data(self):
            I=self.Theatreid_var.get()
            N=self.Thrname_var.get()
            T=self.Thrtype_var.get()
            L=self.Thrloc_var.get()
            M=self.ThrMovid_var.get()
            P=self.Thrshowprice_var.get()
            G=self.Thrgst_var.get()
            if (I=="" or N=="" or T=="" or L=="" or M=="" or P=="" or G=="" ) :
                messagebox.showerror("Error","Can't Clear, \nAll Fields Are Required !!",parent=self.wintheatre)
            else:
                self.Theatreid_var.set('')
                self.Thrname_var.set('')
                self.Thrtype_var.set('')
                self.Thrloc_var.set('')
                self.ThrMovid_var.set('')
                self.Thrshowprice_var.set('')
                self.Thrgst_var.set('')
                messagebox.showinfo("Success","Fields Cleared Successfully",parent=self.wintheatre)



    def get_focus(self,events):
        cursor_row=self.Theatre_Table.focus()
        contents=self.Theatre_Table.item(cursor_row)
        row=contents['values']
        print(row[0],row[1],row[2],row[3],row[4],row[5])
        self.Theatreid_var.set(row[0])
        self.Thrname_var.set(row[1])
        self.Thrtype_var.set(row[2])
        self.Thrloc_var.set(row[3])
        self.ThrMovid_var.set(row[4])
        self.Thrshowprice_var.set(row[5])
        self.Thrgst_var.set(row[6])


    def update_detai(self):
        I=self.Theatreid_var.get()
        N=self.Thrname_var.get()
        T=self.Thrtype_var.get()
        L=self.Thrloc_var.get()
        M=self.ThrMovid_var.get()
        P=self.Thrshowprice_var.get()
        G=self.Thrgst_var.get()
        if (I=="" or N=="" or T=="" or L=="" or M==""  or P=="" or G=="") :
               messagebox.showerror("Error","All Fields Are Required!!!",parent=self.wintheatre)
        else:
            P=float(P)
            G=float(G)
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            sql="UPDATE theatre_Details SET THEATRENAME=:2,THEATRETYPE=:3,THEATRELOCATION=:4,LATESTSHOWMOVIEID=:5,THEATREPERSHOWPRICE=:6,THEATREPERSHOWGST=:7 where THEATREID=:1"
            cur.execute(sql,(N,T,L,M,P,G,I))
            con.commit()
            self.fetch_data2()
            messagebox.showinfo("Success","Record Updated Successfully",parent=self.wintheatre)
            #self.clear_data()
            con.close()

    def delete_dat(self):
        I=self.Theatreid_var.get()
        if I=="":
            messagebox.showerror("Error","Theatre ID is Required to Delete !!",parent=self.wintheatre)
        else:
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            cur.execute("Delete From  Theatre_Details where THEATREID='%s'"%I)
            con.commit()
            con.close()
            self.fetch_data2()
            messagebox.showinfo("Success","Record Deleted Successfully",parent=self.wintheatre)
            #self.clear_data()

    def search_dat(self):
        con=cx_Oracle.connect("mpsingh/mp")
        cur=con.cursor()
        
        #cur.execute("select * from Theatre_Details where "+str(self.search_buy_var.get())+" LIKE '%"+str(self.search_text_var.get()+"%'"))
        sql=f"select * from Theatre_Details where {str(self.search_buy_var.get())} = '{str(self.search_text_var.get())}'"
        cur.execute(sql)
        rows = cur.fetchall()
        if (rows)!=0:
            self.Theatre_Table.delete(*self.Theatre_Table.get_children())
            for row in rows:
                self.Theatre_Table.insert('',END,values=row)
            con.commit()
        con.close()


if __name__ == "main":
    winthr=Tk()
    ob=Theatre(winthr)
    winthr.mainloop()