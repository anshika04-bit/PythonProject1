from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import ImageTk
import pymysql as sql
from datetime import datetime

# ---------------- Login Page ---------------- #
def login_page():
    login = Tk()
    login.title("Login")
    login.geometry("500x300")
    login.config(bg="lightblue")

    Label(login, text="Username", font=("Arial", 14, "bold"), bg="lightblue").place(x=50, y=80)
    user_entry = Entry(login, font=("Arial", 14))
    user_entry.place(x=180, y=80)

    Label(login, text="Password", font=("Arial", 14, "bold"), bg="lightblue").place(x=50, y=130)
    pass_entry = Entry(login, show="*", font=("Arial", 14))
    pass_entry.place(x=180, y=130)

    def check_login():
        u = user_entry.get()
        p = pass_entry.get()
        # यहां आप database से check कर सकते हो
        if u == "anshika" and p == "123":
            messagebox.showinfo("Success", "Login Successful")
            login.destroy()
            registration_page()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    Button(login, text="Login", command=check_login, font=("Arial", 14, "bold")).place(x=200, y=200)
    login.mainloop()

# ---------------- Registration Page ---------------- #
def registration_page():
    top = Tk()
    top.title("Registration Page")
    top.geometry("1200x700")
    top.config(bg="cyan")

    # Insert Function
    def insert():

            k = e_fname.get()
            k2 = e_lname.get()
            k3 = int(e_contact.get())
            k4 = int(e_age.get())
            dob = cal.get_date()
            k6 = e_pass.get()
            k7 = gender_var.get()
            k8 = city_box.get()

            db = sql.connect(host="localhost", user="root", password="****", db="project")
            cur = db.cursor()
            query = """insert into registeration 
                    (first_name, last_name, contact, age, dob, password, gender, city) 
                    values (%s,%s,%s,%s,%s,%s,%s,%s)"""
            values = (k, k2, k3, k4, dob, k6, k7, k8)
            cur.execute(query, values)
            db.commit()
            db.close()

            messagebox.showinfo("Success", "Record Inserted Successfully")
    except Exception as e:
            messagebox.showerror("Error", f"Insertion Failed: {e}")

    # Open Records Page
    def open_records():
        back = Toplevel(top)
        back.title("All Student Records")
        back.geometry("1000x600")
        back.config(bg="lightyellow")

        tv = ttk.Treeview(back)
        tv["columns"] = ("Name", "Lastname", "Contact", "Age", "DOB", "Password", "Gender", "City")
        tv.column("#0", width=0, stretch=NO)
        for col in tv["columns"]:
            tv.column(col, anchor=CENTER, width=100)
            tv.heading(col, text=col, anchor=CENTER)
        tv.place(x=50, y=50, width=900, height=400)

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

        def show_records():
            for row in tv.get_children():
                tv.delete(row)
            try:
                db = sql.connect(host="localhost", user="root", password="****", db="project")
                cur = db.cursor()
                cur.execute("select * from registeration")
                rows = cur.fetchall()
                for r in rows:
                    tv.insert("", "end", values=r)
                db.close()
            except Exception as e:
                messagebox.showerror("Error", f"Database error: {e}")

        Button(back, text="Show Records", command=show_records, font=("Arial", 14, "bold")).place(x=400, y=500)

    # --------- UI Design -------- #
    Label(top, text="Student Registration", bg="green", fg="white", font=("Arial", 25, "bold")).place(x=450, y=30)

    Label(top, text="First Name", bg="cyan", font=("Arial", 18, "bold")).place(x=100, y=100)
    e_fname = Entry(top, font=("Arial", 18))
    e_fname.place(x=300, y=100)

    Label(top, text="Last Name", bg="cyan", font=("Arial", 18, "bold")).place(x=100, y=150)
    e_lname = Entry(top, font=("Arial", 18))
    e_lname.place(x=300, y=150)

    Label(top, text="Contact", bg="cyan", font=("Arial", 18, "bold")).place(x=100, y=200)
    e_contact = Entry(top, font=("Arial", 18))
    e_contact.place(x=300, y=200)

    Label(top, text="Age", bg="cyan", font=("Arial", 18, "bold")).place(x=100, y=250)
    e_age = Entry(top, font=("Arial", 18))
    e_age.place(x=300, y=250)

    Label(top, text="DOB", bg="cyan", font=("Arial", 18, "bold")).place(x=100, y=300)
    cal = DateEntry(top, width=18, font=("Arial", 16))
    cal.place(x=300, y=300)

    Label(top, text="Password", bg="cyan", font=("Arial", 18, "bold")).place(x=100, y=350)
    e_pass = Entry(top, show="*", font=("Arial", 18))
    e_pass.place(x=300, y=350)

    Label(top, text="Gender", bg="cyan", font=("Arial", 18, "bold")).place(x=100, y=400)
    gender_var = StringVar()
    Radiobutton(top, text="Male", variable=gender_var, value="Male", font=("Arial", 14)).place(x=300, y=400)
    Radiobutton(top, text="Female", variable=gender_var, value="Female", font=("Arial", 14)).place(x=400, y=400)
    Radiobutton(top, text="Other", variable=gender_var, value="Other", font=("Arial", 14)).place(x=520, y=400)

    Label(top, text="City", bg="cyan", font=("Arial", 18, "bold")).place(x=100, y=450)
    city_box = ttk.Combobox(top, values=["Select City", "Meerut", "Delhi", "Noida", "Jaipur"], font=("Arial", 16))
    city_box.current(0)
    city_box.place(x=300, y=450)

    Button(top, text="Submit", command=insert, font=("Arial", 18, "bold")).place(x=250, y=550)
    Button(top, text="Show Records", command=open_records, font=("Arial", 18, "bold")).place(x=400, y=550)
    Button(top, text="Exit", command=top.destroy, font=("Arial", 18, "bold")).place(x=600, y=550)

    top.mainloop()

# ---------------- Run App ---------------- #
login_page()
