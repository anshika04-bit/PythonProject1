from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from datetime import datetime
import pymysql as sql
def get_db():
    return sql.connect(host='localhost', user='root', password='236588@Er', db='project2')

#main window
top = Tk()
top.title("Registration System")
top.geometry("1366x768")
top.configure(bg="purple")

def Login():
    top.destroy()


def Exit():
    top.destroy()

def show():
    if e7.cget('show')=="*":
        e7.config(show="")
    else:
        e7.config(show="*")

def show2():
    for row in tv.get_children():
        tv.delete(row)


# Correct way to load and display image
img = ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\high-angle-view-laptop-stationeries-blue-background (1).jpg")
img_label = Label(top, image=img)
img_label.place(x=0, y=0)

import pymysql as sql
db = sql.connect(host='localhost', user='root', password='236588@Er', db='project2')

cur = db.cursor()

s="select * from registeration"
cur.execute(s)
result=cur.fetchall()
for col in result:
        name=col[0]
        lastname=col[1]
        contact=col[2]
        age=col[3]
        Dob=col[4]
        password=col[5]
        gender=col[6]
        city=col[7]



def delete():
    k = e1.get()
    db = sql.connect(host='localhost', user='root', password='236588@Er', db='project2')

    cur = db.cursor()
    q = "delete from registeration where first_name =%s"

    Result = cur.execute(q, (k,))
    db.commit()
    db.close()


    if(Result>0):
        messagebox.showinfo("Result","Your record deleted successfully")
    else:
        messagebox.showerror("Result",'Record not found')

    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e7.delete(0, "end")


def update():
    k = e1.get()  # first_name
    k2 = e2.get()  # lastname
    k3 = int(e3.get())  # contact
    k4 = int(e4.get())  # age
    k6 = e5.get()  # password
    k7 = var.get()  # gender
    k8 = c.get()  # city

    db = sql.connect(host='localhost', user='root', password='236588@Er', db='project2')
    cur = db.cursor()

    s = """UPDATE registeration 
           SET last_name=%s, contact=%s, age=%s, password=%s, gender=%s, city=%s 
           WHERE first_name=%s"""

    cur.execute(s, (k2, k3, k4, k6, k7, k8, k))
    db.commit()
    db.close()

    messagebox.showinfo("Success", "Record Updated Successfully")
tv = ttk.Treeview(top)
tv['columns'] = ('Name', 'Lastname', 'Contact', 'AGE', 'DOB', 'Password', 'Gender', 'City')

tv.column('#0', width=0, stretch=NO)
for col in tv['columns']:
    tv.column(col, anchor=CENTER, width=120)
    tv.heading(col, text=col, anchor=CENTER)

tv.place(x=520, y=150)
def search():
   show2()
   db = sql.connect(host='localhost', user='root', password='236588@er', db='project2')
   cur = db.cursor()

   q = "select * from  registeration where first_name=%s"
   cur.execute(q,(e1.get(),))
   result = cur.fetchall()
   db.close()
for col in result:
    tv.insert("", "end", values=(col))
    db.close()
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
    k= e1.get()
    k2= e2.get()
    k3=int(e3.get())
    k4=int(e4.get())
    #dob

    q=cal.get()
    date=datetime.strptime(q,"'%m/%d/%y'")
  #password
    k6=e5.get()
    #gender
    k7=var.get()
    #city
    k8=c.get()
    db = sql.connect(host="localhost", user="root", password="236588@Er", db="project2")
    cur = db.cursor()

    q = "INSERT INTO registeration(first_name,last_name,contact,age,dob,password,gender,city) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(q, (k, k2, k3, k4, date, k6, k7, k8))
    try:
        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='236588@Er', db='project2')

        cur = db.cursor()
        query = "insert into registeration (first_name,Last_name,contact,age,dob,password,gender,city) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (k, k2, k3, k4, date, k6, k7, k8)
        cur.execute(query, values)
        db.commit()

        db.close()
        messagebox.showinfo("Success","Record Inserted Successfully")
        print("record inserted successfully")
    except Exception as e:
        print("error", f"error:{e}")

    print("data to insert", k, k2, k3, k4, q, k6, k7, k8)

var = StringVar()
k = ['select', 'python', 'java', 'php', 'ruby', 'html', 'fullstack']

# Title
L = Label(top, text="Registration", fg="white", bg="purple", font=("Arial", 30, "bold"))
L.place(x=500, y=20)

# ===================== FIXED LABEL / ENTRY POSITIONS =====================

# Name
L2 = Label(top, text="Name", fg="white", bg="purple", font=("Arial", 20, "bold"))
L2.place(x=50, y=120)
e1 = Entry(top, font=("Arial", 18))
e1.place(x=250, y=120)

# Lastname
L3 = Label(top, text='Lastname', fg="white", bg="purple", font=("Arial", 20, "bold"))
L3.place(x=50, y=170)
e2 = Entry(top, font=("Arial", 18))
e2.place(x=250, y=170)

# Contact
L4 = Label(top, text='Contact', fg="white", bg="purple", font=("Arial", 20, "bold"))
L4.place(x=50, y=220)
e3 = Entry(top, font=("Arial", 18))
e3.place(x=250, y=220)

# Age
L5 = Label(top, text="Age", fg="white", bg="purple", font=("Arial", 20, "bold"))
L5.place(x=50, y=270)
e4 = Entry(top, font=("Arial", 18))
e4.place(x=250, y=270)

# Email
L6 = Label(top, text="Email", fg="white", bg="purple", font=("Arial", 20, "bold"))
L6.place(x=50, y=320)
e6 = Entry(top, font=("Arial", 18))
e6.place(x=250, y=320)

# City
L7 = Label(top, text="City", fg="white", bg="purple", font=("Arial", 20, "bold"))
L7.place(x=50, y=370)
e8 = Entry(top, font=("Arial", 18))
e8.place(x=250, y=370)

# DOB
L8 = Label(top, text="DOB", fg="white", bg="purple", font=("Arial", 20, "bold"))
L8.place(x=50, y=420)
cal = DateEntry(top, width=18, background="white", font=("Arial", 15))
cal.place(x=250, y=420)

# Gender
L9 = Label(top, text='Gender', fg="white", bg="purple", font=("Arial", 20, "bold"))
L9.place(x=50, y=470)

var = StringVar()
Radiobutton(top, text='Male', variable=var, value="Male", font=("Arial", 15), bg="white").place(x=250, y=470)
Radiobutton(top, text='Female', variable=var, value="Female", font=("Arial", 15), bg="white").place(x=350, y=470)
Radiobutton(top, text='Other', variable=var, value="Other", font=("Arial", 15), bg="white").place(x=470, y=470)

# Password
L10 = Label(top, text="Password", fg="white", bg="purple", font=("Arial", 20, "bold"))
L10.place(x=50, y=520)
e5 = Entry(top, font=("Arial", 18), show="*")
e5.place(x=250, y=520)

# Course
L11 = Label(top, text="Course", fg="white", bg="purple", font=("Arial", 20, "bold"))
L11.place(x=50, y=570)

course_list = ['Select', 'Python', 'Java', 'PHP', 'Ruby', 'HTML', 'Fullstack']
cb = ttk.Combobox(top, values=course_list, font=("Arial", 18))
cb.place(x=250, y=570)
cb.current(0)

# City Dropdown
city_list = ['Select City', 'Meerut', 'Jaipur', 'Delhi', 'Noida', 'Kanpur']
c = ttk.Combobox(top, values=city_list, font=("Arial", 18))
c.place(x=250, y=620)
c.current(0)

# Password Show Button
e7 = Entry(top, show="*")
e7.place(x=600, y=520)
Checkbutton(top, command=lambda: e7.config(show="" if e7.cget("show")=="" else "")).place(x=760, y=520)


# ===================== TREEVIEW FIX =====================
tv = ttk.Treeview(top, columns=('Name', 'Lastname', 'Contact', 'AGE', 'DOB', 'Password', 'Gender', 'City'),
                  show='headings')

for col in tv["columns"]:
    tv.heading(col, text=col)
    tv.column(col, width=120, anchor=CENTER)

tv.place(x=650, y=120, height=380)


# ===================== BUTTONS FIX =====================
b1 = Button(top, text="Submit", font=("Arial", 18), bg="white")
b1.place(x=650, y=520)

b2 = Button(top, text='Delete', font=("Arial", 18))
b2.place(x=780, y=520)

b3 = Button(top, text='Show', font=("Arial", 18))
b3.place(x=900, y=520)

b4 = Button(top, text='Search', font=("Arial", 18))
b4.place(x=650, y=570)

b5 = Button(top, text='Update', font=("Arial", 18))
b5.place(x=780, y=570)

b6 = Button(top, text='Exit', font=("Arial", 18), command=top.destroy)
b6.place(x=900, y=570)

b7 = Button(top, text='Login', font=("Arial", 18))
b7.place(x=1020, y=570)

top.mainloop()