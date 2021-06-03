from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
import cx_Oracle
import datetime

class Poster:
    def __init__(self,winposter):
        self.winposter=winposter
        
        winposter.title("Poster Details")
        winposter.geometry("1350x750+0+0")

        self.bg_ic_post=ImageTk.PhotoImage(file="back8poster.png")
        tit=Label(self.winposter,image=self.bg_ic_post).pack()
        
        
        title=Label(self.winposter,text="Movie  Poster  Preview  Section",bd=10,relief=GROOVE,font=("broadway",25,"bold"),bg="dodgerblue2",fg="hotpink1",pady=2)
        title.place(x=0,y=0,relwidth=1)
        self.postmovid_var=StringVar()

        F1=Frame(self.winposter,relief=GROOVE,bd=5,bg='pink1')
        F1.place(x=380,y=60,width=590,height=60)
        
        postlogout_btn=Button(F1,text="Log Out",font="times 13 bold",fg="hotpink1",bg="dodgerblue",relief=SUNKEN,bd=4,command=self.winposter.destroy,width=10).grid(row=0,column=1,padx=8,pady=5)

        lbl_mid=Label(F1,text="Enter Movie ID:",font="times 12 bold",bg="hotpink1",fg="royalblue",relief=GROOVE,width=15).grid(row=0,column=2,padx=8,pady=5)
        ent_mid=Entry(F1,textvariable=self.postmovid_var,font="times 12 bold",width=18).grid(row=0,column=3,padx=8,pady=5)

        view_btn=Button(F1,text="View",font="times 13 bold",fg="hotpink1",bg="dodgerblue",relief=SUNKEN,bd=4,command=self.postview_func,width=10).grid(row=0,column=4,padx=8,pady=5)

    def postview_func(self):
        try:
            M=self.postmovid_var.get()
            con=cx_Oracle.connect("mpsingh/mp")
            cur=con.cursor()
            
            cur.execute("select * from Movie_Details where MOVIEID LIKE '%s'"%M)
            rows = cur.fetchall()
            
            if len(rows)!=0:
                # print(rows)
                # for row in rows:
                #     print(row)
                self.showpost_func(rows)
            else:
                messagebox.showerror("Error",f"Movie with MOVIE ID: '{M}' Not Found !!!",parent=self.winposter)
            con.commit()
            con.close()
        except:
            import sys
            print(sys.exc_info())
    
    def showpost_func(self,ls):
        
        #print(ls)
        movid=ls[0][0]

        F2=Frame(self.winposter,bd=6,relief=RIDGE,bg="dodgerblue2")
        F2.place(x=250,y=190,width=270,height=370)

        if self.isposterexits(movid):

            self.postpic=ImageTk.PhotoImage(file=f"{movid}.png")
            post_lbl=Label(F2,image=self.postpic,bd=0)
            post_lbl.pack(expand=True,fill=BOTH)
            
            #post_lbl.destroy()
            #post_lbl=Label(self.winposter,image=self.postpic,bd=0)
            #post_lbl.place(x=250,y=180)
        else:
            self.postpic=ImageTk.PhotoImage(file="posternotavailable.png")
            post_lbl=Label(F2,image=self.postpic,bd=0)
            post_lbl.pack(expand=True,fill=BOTH)


        F3=Frame(self.winposter,bd=4,relief=RIDGE,bg="maroon1")
        F3.place(x=680,y=130,width=480,height=500)

        lblname=Label(F3,text="Poster Details",font=("times new roman",18,"bold"),bg="orange",fg="crimson").grid(row=0,pady=8,padx=5,columnspan=2)

        lblname=Label(F3,text="Movie Name:",font=("times new roman",16,"bold"),bg="orange",fg="crimson")
        lblname.grid(row=1,column=0,pady=8,padx=5,sticky="w")
        
        txtname=Label(F3,font=("times new roman",12,"bold"),text=ls[0][1],relief=GROOVE,bd=5,fg="crimson")
        txtname.grid(row=1,column=1,pady=8,padx=5,sticky="w")
        
        lbl_typ=Label(F3,text="Movie Type:",font=("times new roman",16,"bold"),bg="orange",fg="crimson")
        lbl_typ.grid(row=2,column=0,pady=8,padx=5,sticky="w")
        
        txt_typ=Label(F3,font=("times new roman",13,"bold"),text=ls[0][2],relief=GROOVE,bd=5,fg="crimson")
        txt_typ.grid(row=2,column=1,pady=8,padx=5,sticky="w")
        
        lbl_dat=Label(F3,text="Released Date:",font=("times new roman",16,"bold"),bg="orange",fg="crimson")
        lbl_dat.grid(row=3,column=0,pady=8,padx=5,sticky="w")
        
        d=ls[0][3].strftime("%d-%b-%Y")
        txt_dat=Label(F3,font=("times new roman",13,"bold"),text=d,relief=GROOVE,bd=5,fg="crimson")
        txt_dat.grid(row=3,column=1,padx=5,pady=8,sticky="w")

        lbl_hero=Label(F3,text="Heroes:",font=("times new roman",16,"bold"),bg="orange",fg="crimson")
        lbl_hero.grid(row=4,column=0,pady=8,padx=5,sticky="w")
        
        txt_hero=Label(F3,font=("times new roman",13,"bold"),text=ls[0][4],relief=GROOVE,bd=5,fg="crimson")
        txt_hero.grid(row=4,column=1,pady=8,padx=5,sticky="w")
        
        lbl_heroine=Label(F3,text="Heroines:",font=("times new roman",16,"bold"),bg="orange",fg="crimson")
        lbl_heroine.grid(row=5,column=0,pady=8,padx=5,sticky="w")
        
        txt_heroine=Label(F3,font=("times new roman",13,"bold"),text=ls[0][5],relief=GROOVE,bd=5,fg="crimson")
        txt_heroine.grid(row=5,column=1,pady=8,padx=5,sticky="w")    
        
        
        lbl_length=Label(F3,text="Length(in min)",font=("times new roman",16,"bold"),bg="orange",fg="crimson")
        lbl_length.grid(row=7,column=0,pady=8,padx=5,sticky="w")
        
        txt_length=Label(F3,font=("times new roman",13,"bold"),text=ls[0][6],relief=GROOVE,bd=5,fg="crimson")
        txt_length.grid(row=7,column=1,pady=8,padx=5,sticky="w")

        lbl_rating=Label(F3,text="Rating",font=("times new roman",16,"bold"),bg="orange",fg="crimson")
        lbl_rating.grid(row=8,column=0,pady=8,padx=5,sticky="w")
        
        txt_rating=Label(F3,font=("times new roman",13,"bold"),text=ls[0][7],relief=GROOVE,bd=5,fg="crimson")
        txt_rating.grid(row=8,column=1,pady=8,padx=5,sticky="w")

    def isposterexits(self,mid):
        import os
        mid=mid+".png"
        #print(mid)
        return (os.path.exists(mid))

if __name__ == "main":
    winposter=Tk()    
    ob=Poster(winposter)
    winposter.mainloop()
