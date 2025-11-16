from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from datetime import datetime

top = Tk()
top.title("sti")
top.geometry("1440x900")


def Login():
    top.destroy()
    import lala


def Exit():
    top.destroy()


def show():
    if e7.cget('show') == "*":
        e7.config(show='')
    else:
        e7.config(show="*")


def show2():
    for row in tv.get_children():
        tv.delete(row)

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='***', db='project')

    cur = db.cursor()

    s = "select * from registeration"
    cur.execute(s)
    result = cur.fetchall()
    for col in result:
        name = col[0]
        lastname = col[1]
        contact = col[2]
        age = col[3]
        Dob = col[4]
        password = col[5]
        gender = col[6]
        city = col[7]
        tv.insert("", 'end', values=(name, lastname, contact, age, Dob, password, gender, city))


def delete():
    k = e1.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='****', db='project')

    cur = db.cursor()
    s = "delete from registeration where first_name =%s"

    Result = cur.execute(s, (k,))
    db.commit()
    db.close()

    if (Result > 0):
        messagebox.showinfo("Result", "Your record deleted successfully")
    else:
        messagebox.showerror("Result", 'Record not found')

    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e7.delete(0, "end")


def update():
    k = e1.get()  # NAME
    k2 = e2.get()  # Lastname
    k3 = int(e3.get())  # contact
    k4 = int(e4.get())  # age
    k6 = e7.get()
    k7 = var.get()
    k8 = c.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='***', db='project')
    cur = db.cursor()

    s = """Update registeration set last_name=%s,contact=%s,age=%s,password=%s,gender=%s,city=%s where first_name=%s"""
    cur.execute(s, (k2, k3, k4, k6, k7, k8, k))
    db.commit()
    messagebox.showinfo("Success", "Record Updated Successfully")
    db.close()


def search():
    for row in tv.get_children():
        tv.delete(row)

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='****', db='project')

    cur = db.cursor()

    s = "select * from registeration where first_name=%s"
    cur.execute(s, (e1.get(),))
    result = cur.fetchall()
    for col in result:
        name = col[0]
        lastname = col[1]
        contact = col[2]
        age = col[3]
        Dob = col[4]
        password = col[5]
        gender = col[6]
        city = col[7]
        tv.insert("", 'end', values=(name, lastname, contact, age, Dob, password, gender, city))


def insert():
    k = e1.get()
    k2 = e2.get()
    k3 = int(e3.get())
    k4 = int(e4.get())
    format = '%m/%d/%y'
    s = cal.get()
    date = datetime.strptime(s, format)
    n = date.strftime('%y,%m,%d')
    k6 = e7.get()
    k7 = var.get()
    k8 = c.get()

    try:
        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='***', db='project')

        cur = db.cursor()
        query = "insert into registeration (first_name,Last_name,contact,age,dob,password,gender,city) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (k, k2, k3, k4, date, k6, k7, k8)
        cur.execute(query, values)
        db.commit()

        db.close()
        print("record inserted successfully")
    except Exception as e:
        print("error", e)

    print("data to insert", k, k2, k3, k4, n, k6, k7, k8)


var = StringVar()

img = ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\high-angle-view-laptop-stationeries-blue-background (1).jpg")
img_label = Label(top, image=img)
img_label.place(x=0, y=0)

L = Label(top, text='Registeration', bg='green', fg='white', font=('Arial 30 bold'))
L.place(x=600, y=30)

L2 = Label(top, text='Name', bg='Green', fg='white', font=('Arial 20 bold'))
L2.place(x=50, y=150)
e1 = Entry(top, font=('arial 20 bold'))
e1.place(x=200, y=150)

L3 = Label(top, text='Lastname', bg='green', fg='white', font=('Arial 20 bold'))
L3.place(x=50, y=200)
e2 = Entry(top, font=('Arial 20 bold'))
e2.place(x=200, y=200)

L4 = Label(top, text='contact', bg='green', fg='white', font=('Arial 20 bold'))
L4.place(x=50, y=250)
e3 = Entry(top, font=('Arial 20 bold'))
e3.place(x=200, y=250)

L5 = Label(top, text='Age', bg='green', fg='white', font=('Arial 20 bold'))
L5.place(x=50, y=300)
e4 = Entry(top, font=('Arial 20 bold'))
e4.place(x=200, y=300)

L6 = Label(top, text='DOB', bg='green', fg='white', font=('Arial 20 bold'))
L6.place(x=50, y=350)
cal = DateEntry(top, width=18, bg='Green', fg='white', font=('Arial 20 bold'), year=2020)
cal.place(x=200, y=350)

L7 = Label(top, text='Password', bg='green', fg='white', font=('Arial 20 bold'))
L7.place(x=50, y=400)
e7 = Entry(top, show="*", font=('Arial', 20, 'bold'))
e7.place(x=200, y=400)

ch = Checkbutton(top, command=show)
ch.place(x=510, y=400)

L8 = Label(top, text='Gender', bg='green', fg='white', font=('Arial 20 bold'))
L8.place(x=50, y=450)
r = Radiobutton(top, text='Male', variable=var, value="Male", font=('arial', 15, "bold"))
r.place(x=200, y=450)
r2 = Radiobutton(top, text="Female", variable=var, value="Female", font=("arial", 15, "bold"))
r2.place(x=350, y=450)
r3 = Radiobutton(top, text="Other", variable=var, value="Other", font=('Arial', 15, 'bold'))
r3.place(x=500, y=450)

L9 = Label(top, text='City', bg='green', fg='white', font=('Arial 20 bold'))
L9.place(x=50, y=500)
k = ['select city', 'Meerut', 'Jaipur', 'Delhi', 'Noida', 'Kanpur']

c = ttk.Combobox(top, values=k, font=('Arial 20 bold'))
c.place(x=200, y=500)
c.current(0)

tv = ttk.Treeview(top)
tv['columns'] = ('Name', 'Lastname', 'Contact', 'AGE', 'DOB', 'Password', 'Gender', 'City')
tv.column('#0', width=0, stretch=NO)
tv.column('Name', anchor=CENTER, width=80)
tv.column('Lastname', anchor=CENTER, width=80)
tv.column('Contact', anchor=CENTER, width=80)
tv.column('AGE', anchor=CENTER, width=80)
tv.column('DOB', anchor=CENTER, width=80)
tv.column('Password', anchor=CENTER, width=80)
tv.column('Gender', anchor=CENTER, width=80)
tv.column('City', anchor=CENTER, width=80)
tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Lastname', text='Lastname', anchor=CENTER)
tv.heading('Contact', text='Contact', anchor=CENTER)
tv.heading('AGE', text='AGE', anchor=CENTER)
tv.heading('DOB', text='DOB', anchor=CENTER)
tv.heading('Password', text='Password', anchor=CENTER)
tv.heading('Gender', text='Gender', anchor=CENTER)
tv.heading('City', text='City', anchor=CENTER)
tv.place(x=520, y=150)

b = Button(top, text='Submit', command=insert, font=('arial 20 bold'))
b.place(x=250, y=550)

b2 = Button(top, text='delete', command=delete, font=('arial 20 bold'))
b2.place(x=400, y=550)

b3 = Button(top, text='show', font=('Arial 20 bold'), command=show2)
b3.place(x=550, y=550)

b4 = Button(top, text='search', font=('Arial 20 bold'), command=search)
b4.place(x=700, y=550)

b5 = Button(top, text='update', font=('Arial 20 bold'), command=update)
b5.place(x=850, y=550)

b6 = Button(top, text='Exit', font=('Arial 20 bold'), command=Exit)
b6.place(x=1000, y=550)

b7 = Button(top, text='Login', font=('Arial 20 bold'), command=Login)
b7.place(x=1100, y=550)

top.config(bg='cyan')

top.mainloop()