import sqlite3
import datetime
from gui import *
from tkinter import *
import tkinter.messagebox
class Deposit:
    def gui_1(self):
        if(self.e1.get()):
            db=sqlite3.connect("samp1.db")
            c=db.cursor()
            z=eval(self.e1.get())
            id=self.id
            list1=[(id)]
            c.execute("select * from Bank3 where id=?",list1)    
            result_1=c.fetchall()
            a=result_1[0][3]+z
            today=datetime.date.today()
            list4=[(a,str(today),id)]
            c.executemany("update Bank3 set bal=?,date1=? where id=?",list4)
            db.commit()
            tkinter.messagebox.showinfo("Deposit","You have successfully deposited")
            self.root.destroy()
        else:
            tkinter.messagebox.showinfo("Error","Please Enter the amount")
   
    def __init__(self,id):
        self.id=id
        self.root=Tk()
        self.root.title("The State Bank of India")
        self.root.geometry("600x400+300+165")
        self.root.resizable(width=False,height=False)
        self.root.configure(bg="cyan")
        l1=Label(self.root,text="Enter the Amount  :  ",bd=1,width=18,padx=10,
                     font="Times 20 bold",height=3,bg="cyan")
        l1.grid(row=1,column=0)
        self.e1=Entry(self.root,bd=5,font="Times 18 bold",bg="yellow")
        self.e1.focus()
        self.e1.grid(row=1,column=1)
        
        b1=Button(self.root,text="Deposit",font="Times 18 bold",bd=15,width=15,height=1,
                  justify="right",relief='ridge',bg="green",activebackground="blue",command= lambda: self.gui_1())
        b1.grid(row=2,column=1)
        
        self.root.mainloop()

