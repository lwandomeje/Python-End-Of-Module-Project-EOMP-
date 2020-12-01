from tkinter import *
import tkinter
from tkinter import messagebox
from datetime import *



show = Tk()
show.title("LOTTO App")
show.geometry("1100x880")
show.configure(background="gold")

c=Canvas(show,height=10,width=200)
filename=PhotoImage(file="//home//user//Downloads//lotto1.png")
bg_lbl= Label(show,image=filename)
bg_lbl.place(x=60,y=0)

date_time1= datetime.now()
txtdate1 = Label(show,width=20)
txtdate1.place(x=900,y=110)
txtdate1.config(text="DATE: " + date_time1.strftime("%d/%m/%y"))

def submit():
    try:
        age = int(txtage.get())
        name = txtname.get()
        if age >= 18:
         messagebox.showinfo("INFO","Its time to be a Millionair")
         f = open("myStat.txt","a+")
         f.write("name:" + name+"\n")
         f.write("age:" + str(age) + "\n")
         f.close()
         show.withdraw()
         import test
         test.mainloop()
        else:
            messagebox.showinfo("INFO","Sorry You Under Age TO PLay")
            txtage.delete(0,END)
            txtname.delete(0,END)

    except ValueError:
        messagebox.showinfo("INFO","Enter a number in Age")
        txtage.delete(0,END)
        txtname.delete(0,END)



date_time1= datetime.now()
txtdate1 = Label(show,width=20)
txtdate1.place(x=900,y=80)
txtdate1.config(text="TIME: " + date_time1.strftime("%H: %M: %S"))


lblname = Label(show, text= "Enter Your Name:", bg="silver")
lblname.place(x=10,y=480)
txtname=Entry(show , width=30)
txtname.place(x=280 , y=480)

lblage = Label(show, text= "Enter Your Age:", bg="silver")
lblage.place(x=10,y=580)
txtage=Entry(show , width=30)
txtage.place(x=280 , y=580)


#Buttons
search_btn = Button(show,text='Submit', width= 15,bg="green" ,command=submit )
search_btn.place(x=460,y=660)



show.mainloop()

