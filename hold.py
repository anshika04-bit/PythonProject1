from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
from tkinter import messagebox
import pymysql as sql   # correct import
# Root window
top = Tk()
top.geometry("1200x700")
top.configure(bg="purple")
top.title("Login Form")
def showpassword():
    if e3.cget("show") == "*":
        e3.config(show="")
    else:
        e3.config(show="*")
def insert():
    username = e1.get()
    password = e3.get()
    if username.strip() == "" or password.strip() == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        messagebox.showinfo("Submitted", f"Username: {username}\nPassword: {password}")


# Load and display image
img = ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\high-angle-view-laptop-stationeries-blue-background (1).jpg")
img_label = Label(top, image=img)
img_label.place(x=0, y=0)
# Dropdown values
k = ['select', 'python', 'java', 'php', 'ruby', 'html', 'fullstack']
# Name
L2 = Label(top, text="Name", fg="white", bg="purple", font=("Arial", 20, "bold"))
L2.place(x=100, y=100)
e1 = Entry(top, font=("Arial", 20, "bold"))
e1.place(x=300, y=100)
# Password
L4 = Label(top, text="Password", fg="white", bg="purple", font=("Arial", 20, "bold"))
L4.place(x=100, y=220)
e3 = Entry(top, font=("Arial", 20, "bold"), show="*")
e3.place(x=300, y=220)
b4 = Checkbutton(top, text="Show Password", command=showpassword, bg="purple", fg="white", font=("Arial", 12, "bold"))
b4.place(x=300, y=270)
b4.place(x=100, y=320)
# Submit Button
b1 = Button(top, text="Submit", font=("Arial", 20, "bold"), bg="white", fg="black", command=insert)
b1.place(x=500, y=570)

top.mainloop()