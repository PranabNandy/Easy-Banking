from create_database import *
from deposit import *
from withdrawl import *
from register import *
from tkinter import *

class Check_1:
    def deposit_1(self,id):
        self.root.destroy()
        Deposit(id)
    def withdrawl_1(self,id):
        self.root.destroy()
        Withdrawl(id)
    def register_1(self):
        self.root.destroy()
        Register()
    def __init__(self,id):
        self.root=Tk()
        self.root.title("The State Bank of India")
        self.root.geometry("600x400+300+165")
        self.root.resizable(width=False,height=False)
        self.root.configure(bg="cyan")
    
        create_db()
        db=sqlite3.connect("samp1.db")
        c=db.cursor()
    #c.execute("select * from Bank")
    #[print(row) for row in c.fetchall()]

        list1=[(id)]
        c.execute("select * from Bank3 where id=?",list1)
        result=c.fetchall()
        if(result):
            l1=Label(self.root,text="Welcome  "+str(result[0][1]),bd=1,width=18,padx=10,
                     font="Times 22 bold",height=3,bg="cyan")
            l1.grid(row=1,column=0)
            l2=Label(self.root,text="Your last updated bal :",bd=1,width=19,padx=5,
                     font="Times 18 ",height=3,bg="cyan",anchor='e')
            l2.grid(row=2,column=0)
            l2=Label(self.root,text="Rs "+str(result[0][3])+"  on  "+str(result[0][4]),bd=1,width=20,
                     font="Times 18 ",height=3,bg="cyan",anchor='w')
            l2.grid(row=2,column=1)
            b2=Button(self.root,text="Deposit",font="Times 20 bold",bd=10,width=15,height=1,
                      justify="right",relief='ridge',bg="green",activebackground="blue",command= lambda: self.deposit_1(id))
            b2.grid(row=3,column=0)
            b3=Button(self.root,text="Withdrawl",font="Times 20 bold",bd=10,width=15,height=1,
                      justify="right",relief='ridge',bg="green",activebackground="blue",command= lambda: self.withdrawl_1(id))
            b3.grid(row=3,column=1)
            self.root.mainloop()

        else:
            l1=Label(self.root,text="You have entered wrong A/C No ",bd=1,width=30,padx=10,
                     font="Times 24 bold",height=3,bg="cyan")
            l1.grid(row=1,column=0)
            l2=Label(self.root,text="Do you want to create a new Account",bd=1,width=30,
                     font="Times 18 ",height=2,bg="cyan")
            l2.grid(row=2,column=0)
            b2=Button(self.root,text="Register",font="Times 20 bold",bd=15,width=13,height=1,
                      justify="right",relief='ridge',bg="lightblue",activebackground="blue",command= lambda: self.register_1())
            b2.grid(row=3,column=0)
            self.root.mainloop()
    
            
