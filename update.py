from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

top=Tk()
top.title("sti ")
top.geometry("1440x900")
top.config(bg="blue")


img = ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\high-angle-view-laptop-stationeries-blue-background (1).jpg")
img_label = Label(top, image=img)
img_label.place(x=0, y=0)


def Login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='236588@Er', db='project2')

    cur = db.cursor()
    cur.execute("select * from registeration where first_name =%s and password =%s",(E2.get(),E3.get()))
    row=cur.fetchone()

    if row is None:
        messagebox.showerror("Error","Invalid User Name and Password")
    else:
        top.destroy()
        import STI


L=Label(top,text='Login',bg='green',fg='white',font=('Arial 30 bold'))
L.place(x=550,y=30)

L2=L=Label(top,text='Name',bg='blue',fg='white',font=('Arial 20 bold'))
L2.place(x=200,y=100)
E2=Entry(top,font='Arial 20 bold')
E2.place(x=400,y=100)


L3=Label(top,text='Password',bg='blue',fg='white',font=('Arial 20 bold'))
L3.place(x=200,y=150)
E3=Entry(top,font='Arial 20 bold',show='*')
E3.place(x=400,y=150)

b=Button(top,text='Login',font=('Arial 20 bold'),command=Login)
b.place(x=400,y=200)


top.mainloop()