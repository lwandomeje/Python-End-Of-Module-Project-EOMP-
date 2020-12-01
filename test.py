from tkinter import *
import random
from datetime import *
from tkinter import Image
from tkinter import messagebox

show = Tk()
show.title("LOTTO App")
show.geometry("1100x880")
show.configure(background="gold")

c=Canvas(show,height=10,width=200)
filename=PhotoImage(file="//home//user//Downloads//lotto1.png")
bg_lbl= Label(show,image=filename)
bg_lbl.place(x=60,y=0)
c.pack()


date_time1= datetime.now()
txtdate1 = Label(show,width=20)
txtdate1.place(x=900,y=0)
txtdate1.config(text="DATE: " + date_time1.strftime("%d/%m/%y"))

date_time1= datetime.now()
txttime1 = Label(show,width=20)
txttime1.place(x=900,y=30)
txttime1.config(text="TIME: " + date_time1.strftime("%H: %M: %S"))



def lotto():
    number2= list(range(1,49))
    number3 = random.sample(number2,k=6)
    num7.insert("1.0",number3[0])
    num8.insert("1.0",number3[1])
    num9.insert("1.0",number3[2])
    num10.insert("1.0",number3[3])
    num11.insert("1.0",number3[4])
    num12.insert("1.0",number3[5])
    return number3


def Mynumbers():
    enter1 = int(num1.get("1.0",END))
    enter2 = int(num2.get("1.0",END))
    enter3 = int(num3.get("1.0",END))
    enter4 = int(num4.get("1.0",END))
    enter5 = int(num5.get("1.0",END))
    enter6 = int(num6.get("1.0",END))
    numbers1=[enter1,enter2,enter3,enter4,enter5,enter6]
    if enter1 > 49 :
        messagebox.showinfo("INFO","Enter Numbers Between 1 and 49")
    if enter2 > 49 :
        messagebox.showinfo("INFO","Enter Numbers Between 1 and 49")
    if enter3 > 49 :
        messagebox.showinfo("INFO","Enter Numbers Between 1 and 49")
    if enter4 > 49 :
        messagebox.showinfo("INFO","Enter Numbers Between 1 and 49")
    if enter5 > 49  :
        messagebox.showinfo("INFO","Enter Numbers Between 1 and 49")
    if enter6 > 49 :
        messagebox.showinfo("INFO","Enter Numbers Between 1 and 49")
    return numbers1


def com():
    try:
        num7.delete("1.0", END)
        num8.delete("1.0", END)
        num9.delete("1.0", END)
        num10.delete("1.0", END)
        num11.delete("1.0", END)
        num12.delete("1.0", END)

        numbers1 = Mynumbers()
        number3 = lotto()
        result = [y for y in numbers1 if y in number3]



        if len(numbers1) != len(set(numbers1)):
            messagebox.showinfo("INFO","YOU CAN NOT REPEAT NUMBERS")
            show.withdraw()
            import peomp
            peomp.mainloop()

        else:
            txtguessednum.configure(text=result)


            if len(result) == 6:
                txtwinings.configure(text="YOUR PRIZE R10,000 000.00")
                f = open("/home/user/PycharmProjects/pythonProject/myStat.txt","a+")
                f.write(txtwinings.cget("text")+"\n"+"You got:" +str(result) + "\n" +txtdate1.cget("text") +"\n" +txttime1.cget("text"))
            elif len(result) == 5:
                txtwinings.configure(text="YOUR PRIZE R8,584.00")
                f = open("/home/user/PycharmProjects/pythonProject/myStat.txt","a+")
                f.write(txtwinings.cget("text")+"\n"+"You got:"+str(result) + "\n" +txtdate1.cget("text") +"\n" +txttime1.cget("text"))
            elif len(result) == 4:
                txtwinings.configure(text="YOUR PRIZE R2,384.00")
                f = open("/home/user/PycharmProjects/pythonProject/myStat.txt","a+")
                f.write(txtwinings.cget("text")+"\n" + "YOU got:" +str(result) +"\n" +txtdate1.cget("text") +"\n" +txttime1.cget("text"))
            elif len(result) == 3:
                txtwinings.configure(text="YOUR PRIZE R100.50")
                f = open("/home/user/PycharmProjects/pythonProject/myStat.txt","a+")
                f.write(txtwinings.cget("text")+"\n"+"You got:" + str(result) + "\n" +txtdate1.cget("text") +"\n" +txttime1.cget("text"))
            elif len(result) == 2:
                txtwinings.configure(text="YOUR PRIZE R20.00")
                f = open("/home/user/PycharmProjects/pythonProject/myStat.txt","a+")
                f.write(txtwinings.cget("text")+"\n" +"you got:" +str(result) + "\n" +txtdate1.cget("text") +"\n" +txttime1.cget("text"))
            elif len(result) == 1:
                txtwinings.configure(text="YOUR PRIZE R0")
                f = open("/home/user/PycharmProjects/pythonProject/myStat.txt","a+")
                f.write(txtwinings.cget("text")+"\n" +"You got:" +str(result) + "\n" +txtdate1.cget("text") +"\n" +txttime1.cget("text") )
            elif len(result) == 0:
                txtwinings.configure(text="YOUR PRIZE R0")
                f = open("/home/user/PycharmProjects/pythonProject/myStat.txt","a+")
                f.write(txtwinings.cget("text")+"\n" +"You got:"+ str(result)+"\n" +txtdate1.cget("text") +"\n" +txttime1.cget("text"))

    except ValueError:
        messagebox.showinfo("INFO","Please Enter a number")




lbl = Label(show, text= "Enter your numbers:", bg="silver")
lbl.place(x=100,y=490)

num1 = Text(show,width=9,height=5,bg="limegreen" )
num1.place(x=300,y=430)

num2 = Text(show,width=9,height=5,bg="gold")
num2 .place(x=400,y=430)

num3  = Text(show,width=9,height=5,bg="tomato")
num3 .place(x=500,y=430)

num4 = Text(show,width=9,height=5,bg="violet")
num4.place(x=600,y=430)

num5 = Text(show,width=9,height=5,bg="steelblue")
num5.place(x=700,y=430)

num6 = Text(show,width=9,height=5,bg="tan")
num6.place(x=800,y=430)

txtguessednum = Label(show,width=30)
txtguessednum.place(x=10,y=730)
txtwinings = Label(show,width=30)
txtwinings.place(x=370,y=730)


lbl = Label(show, text= "Today's wining lotto numbers :", bg="silver")
lbl.place(x=80,y=630)

num7= Text(show,width=9,height=5,bg="limegreen")
num7.place(x=300,y=590)

num8 = Text(show,width=9,height=5,bg="gold")
num8 .place(x=400,y=590)

num9 = Text(show,width=9,height=5,bg="violet")
num9.place(x=600,y=590)

num10=Text(show,width=9,height=5,bg="steelblue")
num10.place(x=700,y=590)

num11=Text(show,width=9,height=5,bg="tan")
num11.place(x=800, y=590)

num12= Text(show,width=9,height=5,bg="tomato")
num12.place(x=500,y=590)

#Buttons
search_btn = Button(show,text='Play', width= 15,bg="green", command=com )
search_btn.place(x=460,y=550)

show.mainloop()

