from tkinter import *
from create_database import *
import datetime
import tkinter.messagebox

class Register:
    def store(self):
        if((self.e1.get()) and (self.e2.get()) and (self.e3.get())and (self.e4.get())):
            a=str(self.e1.get())
            b=eval(self.e2.get())
            d=eval(self.e3.get())
            e=eval(self.e4.get())
            create_db()
            db=sqlite3.connect("samp1.db")
            c=db.cursor()
            today=datetime.date.today()
            z1=[(e)]
            c.execute("select * from Bank3 where id=?",z1)
            result=c.fetchall()
            s=str(e)+" A/C No already exist.Enter another A/c No."
            if(result):
                tkinter.messagebox.showinfo("Error",s)
                self.e4.delete(0,'end')
            else:
                list4=[(e,a,b,d,str(today))]
                c.executemany("insert into Bank3 values(?,?,?,?,?)",list4)
                db.commit()
                tkinter.messagebox.showinfo("Registered","Registation Successful")
                self.root.destroy()
        else:
            tkinter.messagebox.showinfo("Error","Please fill all the information")
    def __init__(self):
        self.id=id
        self.root=Tk()
        self.root.title("The State Bank of India")
        self.root.geometry("600x400+300+165")
        self.root.resizable(width=False,height=False)
        self.root.configure(bg="cyan")
        l1=Label(self.root,text="Customer Name",bd=1,width=18,padx=10,
                     font="Times 16",height=1,bg="cyan",anchor='e')
        l1.grid(row=0,column=0)
        l2=Label(self.root,text="Age",bd=1,width=18,
                     font="Times 16",height=1,bg="cyan",anchor='e')
        l2.grid(row=1,column=0)
        l4=Label(self.root,text="The Opening Balance",bd=1,width=18,
                     font="Times 16",height=1,bg="cyan",anchor='e')
        l4.grid(row=2,column=0)
        l5=Label(self.root,text="Customer A/C No",bd=1,width=18,
                     font="Times 16",height=1,bg="cyan",anchor='e')
        l5.grid(row=3,column=0)
        self.e1=Entry(self.root,bd=5,font="Times 16 bold",bg="yellow")
        self.e1.grid(row=0,column=1)
        self.e1.focus()
        self.e2=Entry(self.root,bd=5,font="Times 16 bold",bg="yellow")
        self.e2.grid(row=1,column=1)
        self.e3=Entry(self.root,bd=5,font="Times 16 bold",bg="yellow")
        self.e3.grid(row=2,column=1)
        self.e4=Entry(self.root,bd=5,font="Times 16 bold",bg="yellow")
        self.e4.grid(row=3,column=1)
        l5=Label(self.root,text="Customer A/C No must\n be unique",bd=1,width=18,
                     font="Times 16",height=3,bg="cyan")
        l5.grid(row=4,column=1)
        b1=Button(self.root,text="Register",font="Times 20 bold",bd=15,width=10,height=1,
                 relief='ridge',bg="green",activebackground="blue",command=self.store)
        b1.grid(row=5,column=0)
        
        self.root.mainloop()

    


	
