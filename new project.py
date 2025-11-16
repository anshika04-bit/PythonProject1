from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from datetime import datetime
import pymysql as sql

def get_db():
    return sql.connect(host='localhost', user='root', password='236588@Er', db='project2')

# main window
top = Tk()
top.title("Registration System")
top.geometry("1366x768")

# BACKGROUND IMAGE FIX
img = Image.open(r"C:\Users\HP\Downloads\high-angle-view-laptop-stationeries-blue-background (1).jpg")
img = img.resize((1366, 768))
bg = ImageTk.PhotoImage(img)

bg_label = Label(top, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()

# Title
L = Label(top, text="Registration", fg="white", bg="purple", font=("Arial", 30, "bold"))
L.place(x=500, y=20)

# ===================== FIXED LABEL / ENTRY POSITIONS =====================

# Name
L2 = Label(top, text="Name", fg="white", bg="purple", font=("Arial", 20, "bold"))
L2.place(x=50, y=120)
e1 = Entry(top, font=("Arial", 14))
e1.place(x=250, y=120)

# Lastname
L3 = Label(top, text='Lastname', fg="white", bg="purple", font=("Arial", 20, "bold"))
L3.place(x=50, y=170)
e2 = Entry(top, font=("Arial", 14))
e2.place(x=250, y=170)

# Contact
L4 = Label(top, text='Contact', fg="white", bg="purple", font=("Arial", 20, "bold"))
L4.place(x=50, y=220)
e3 = Entry(top, font=("Arial", 14))
e3.place(x=250, y=220)

# Age
L5 = Label(top, text="Age", fg="white", bg="purple", font=("Arial", 20, "bold"))
L5.place(x=50, y=270)
e4 = Entry(top, font=("Arial", 14))
e4.place(x=250, y=270)

# Email
L6 = Label(top, text="Email", fg="white", bg="purple", font=("Arial", 20, "bold"))
L6.place(x=50, y=320)
e6 = Entry(top, font=("Arial", 14))
e6.place(x=250, y=320)

# City
L7 = Label(top, text="City", fg="white", bg="purple", font=("Arial", 20, "bold"))
L7.place(x=50, y=370)
e8 = Entry(top, font=("Arial", 14))
e8.place(x=250, y=370)

# DOB
L8 = Label(top, text="DOB", fg="white", bg="purple", font=("Arial", 20, "bold"))
L8.place(x=50, y=420)
cal = DateEntry(top, width=14, background="white", font=("Arial", 15))
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
e5 = Entry(top, font=("Arial", 14), show="*")
e5.place(x=250, y=520)

# Course
L11 = Label(top, text="Course", fg="white", bg="purple", font=("Arial", 20, "bold"))
L11.place(x=50, y=570)

course_list = ['Select', 'Python', 'Java', 'PHP', 'Ruby', 'HTML', 'Fullstack']
cb = ttk.Combobox(top, values=course_list, font=("Arial", 14))
cb.place(x=250, y=570)
cb.current(0)

# City Dropdown
city_list = ['Select City', 'Meerut', 'Jaipur', 'Delhi', 'Noida', 'Kanpur']
c = ttk.Combobox(top, values=city_list, font=("Arial", 14))
c.place(x=250, y=620)
c.current(0)

# Password Show Button
e7 = Entry(top, show="*")
e7.place(x=600, y=520)
Checkbutton(top, command=lambda: e7.config(show="" if e7.cget("show")=="" else "")).place(x=760, y=520)



tv = ttk.Treeview(top, columns=('Name', 'Lastname', 'Contact', 'AGE', 'DOB', 'Password', 'Gender', 'City'),
                  show='headings')

for col in tv["columns"]:
    tv.heading(col, text=col)
    tv.column(col, width=120, anchor=CENTER)

tv.place(x=650, y=120, height=380)



b1 = Button(top, text="Submit", font=("Arial", 14), bg="white")
b1.place(x=650, y=520)

b2 = Button(top, text='Delete', font=("Arial", 14))
b2.place(x=780, y=520)

b3 = Button(top, text='Show', font=("Arial", 14))
b3.place(x=900, y=520)

b4 = Button(top, text='Search', font=("Arial", 14))
b4.place(x=650, y=570)

b5 = Button(top, text='Update', font=("Arial", 14))
b5.place(x=780, y=570)

b6 = Button(top, text='Exit', font=("Arial", 14), command=top.destroy)
b6.place(x=900, y=570)

b7 = Button(top, text='Login', font=("Arial", 14))
b7.place(x=1020, y=570)

top.mainloop()