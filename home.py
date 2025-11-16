from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import ttk, messagebox

top = Tk()
top.title('sti')
top.geometry("1440x900")
top.config(bg='blue')

img = ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\high-angle-view-laptop-stationeries-blue-background (1).jpg")
img_label = Label(top, image=img)
img_label.place(x=0, y=0)

var = StringVar()


def insert():
    k = e1.get()
    k2 = e2.get()
    k3 = int(e3.get())
    k4 = int(e4.get())
    format = '%m/%d/%y'
    s = e5.get()
    date = datetime.strptime(s, format)
    n = date.strftime('%y,%m,%d')
    k6 = e6.get()
    k7 = var.get()
    k8 = combo.get()

    try:
        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='Shivank@2000', db='project')

        cur = db.cursor()
        query = "insert into teacher_details (name,lastname,contact,age,dob,qualification,experience,gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (k, k2, k3, k4, date, k6, k7, k8)
        cur.execute(query, values)
        db.commit()

        db.close()
        print("record inserted successfully")
    except Exception as e:
        print("error", e)

    print("data to insert", k, k2, k3, k4, n, k6, k7, k8)

    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")
    e6.delete(0, "end")


def Exit():
    top.destroy()


def back():
    top.destroy()
    import STI


def update():
    k = e1.get()
    k2 = e2.get()
    k3 = int(e3.get())
    k4 = int(e4.get())
    format = '%m/%d/%y'
    s = e5.get()
    date = datetime.strptime(s, format)
    n = date.strftime('%y,%m,%d')
    k6 = e6.get()
    k7 = var.get()
    k8 = combo.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='236588@Er', db='project2')
    cur = db.cursor()

    s = """Update teacher_details set lastname=%s,contact=%s,age=%s,DOB=%s,qualification=%s,experience=%s,gender=%s where name=%s"""
    cur.execute(s, (k2, k3, k4, date, k6, k7, k8, k))
    db.commit()
    messagebox.showinfo("Success", "Record Updated Successfully")
    db.close()

    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")
    e6.delete(0, "end")


def delete():
    k = e1.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Shivank@2000', db='project')

    cur = db.cursor()
    s = "delete from teacher_details where name =%s"

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
    e5.delete(0, "end")
    e6.delete(0, "end")


Label(top, text='Anshika Technical Institute', bg='green', fg='white', font=('Cambria 20')).place(x=450, y=20)
Label(top, text='Teacher Registeration', bg='green', fg='white', font=('Cambria 20')).place(x=480, y=60)

Label(top, text='Name', font=('Cambria 15')).place(x=100, y=100)
e1 = Entry(top, font='cambria 15')
e1.place(x=250, y=100)

Label(top, text='Last Name', font='Cambria 15').place(x=100, y=150)
e2 = Entry(top, font='cambria 15')
e2.place(x=250, y=150)

Label(top, text='contact', font=('Cambria 15')).place(x=100, y=200)
e3 = Entry(top, font='cambria 15')
e3.place(x=250, y=200)

Label(top, text='Age', font=('Cambria 15')).place(x=100, y=250)
e4 = Entry(top, font='cambria 15')
e4.place(x=250, y=250)

Label(top, text='DOB', font='Cambria 15').place(x=100, y=300)
e5 = DateEntry(top, width=18, bg='Green', fg='white', font='Cambria 15', year=2020)
e5.place(x=250, y=300)
Label(top, text='Qualification', font='Cambria 15').place(x=100, y=350)
k = ['select Qualification', 'BTech', 'MTech', 'BCA', 'MCA', 'PhD']
combo = ttk.Combobox(top, values=k, font=('Cambria 15'))
combo.place(x=250, y=350)
combo.current(0)
Label(top, text='Experience', font='Cambria 15').place(x=100, y=400)
e6 = Entry(top, font='Cambria 15')
e6.place(x=250, y=400)

Label(top, text='Gender', bg='white', fg='black', font=('Cambria 15')).place(x=100, y=450)
r = Radiobutton(top, text='Male', variable=var, value="Male", font=('Cambria', 15))
r.place(x=250, y=450)
r2 = Radiobutton(top, text="Female", variable=var, value="Female", font=("cambria", 15))
r2.place(x=330, y=450)
r3 = Radiobutton(top, text="Other", variable=var, value="Other", font=('cambria', 15))
r3.place(x=430, y=450)

Button(top, text='Submit', font='Cambria 15', command=insert).place(x=100, y=550)
Button(top, text='Back', font='Cambria 15', command=back).place(x=250, y=550)
Button(top, text='Exit', font='Cambria 15', command=Exit).place(x=350, y=550)
Button(top, text='Update Teacher', font='Cambria 15', command=update).place(x=450, y=550)
Button(top, text='Delete Teacher', font='Cambria 15', command=delete).place(x=650, y=550)

top.mainloop()