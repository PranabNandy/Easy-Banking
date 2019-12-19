from tkinter import *
from check import *
import tkinter.messagebox
class Mainroot():
    def __init__(self):    
        self.root=Tk()
        self.root.title("The State Bank of India")
        self.root.geometry("600x400+300+165")
        self.root.configure(bg="cyan")
        l1=Label(self.root,text="Enter the A/C No  ",bd=1,width=20,
                 font="Times 20 bold",height=3,bg="cyan")
        l1.grid(row=2,column=0)
        self.e1=Entry(self.root,bd=5,font="Times 18 bold",bg="yellow")
        self.e1.grid(row=2,column=1)
        self.e1.focus()
        b1=Button(self.root,text=" OK ",font="Times 18 bold",bd=15,width=15,height=1,
                  justify="right",relief='ridge',bg="green",activebackground="blue",command= lambda: self.check1())
        b1.grid(row=3,column=1)
        l1=Label(self.root,text="Don't have any A/C",bd=1,width=20,
                 font="Verdana 17 ",height=1,bg="cyan")
        l1.grid(row=3,column=0)
        b2=Button(self.root,text="Register here",font="Times 18 bold",bd=15,width=15,height=1,
                  justify="right",relief='ridge',bg="green",activebackground="blue",command=self.register)
        b2.grid(row=4,column=0)
        b1=Button(self.root,text="Exit",font="Times 18 bold",bd=15,width=15,height=3,
                  justify="right",relief='ridge',bg="Red",activebackground="Orange",command=self.exit_1)
        b1.grid(row=5,column=1)
        self.root.resizable(width=False,height=False)
        self.root.mainloop()
    def register(self):
        self.root.destroy()
        Register()
    def exit_1(self):
        exit()
    def check1(self):
        x1=(self.e1.get())
        if(x1):
            x=eval(self.e1.get())
            self.root.destroy()
            c=Check_1(x)
        else:
             tkinter.messagebox.showinfo("Error","Please Enter a A/C No")
        
