from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


top=Tk()
top.title('sti')
top.geometry("1440x900")
top.config(bg='blue')

img = ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\high-angle-view-laptop-stationeries-blue-background (1).jpg")
img_label = Label(top, image=img)
img_label.place(x=0, y=0)


Label(top,text='Anshika Technical Institute',bg='green',fg='white',font=('Cambria 20')).place(x=450,y=20)
Label(top,text='Welcome',bg='green',fg='white',font=('Cambria 20')).place(x=550,y=60)


#functions

def click1():
    top.destroy()
    import AddTeacher

def click2():
    top.destroy()
    import Addcourse

def click3():
    top.destroy()
    import StudentRegisteration

def Exit():
    top.destroy()


def showcourses():
    # Clear existing data
    for row in tv.get_children():
        tv.delete(row)

    # Configure treeview columns for courses
    tv['columns'] = ('course_name', 'Duration', 'Fee', 'Teacher', 'Time', 'Mode')
    tv.column('#0', width=0, stretch=NO)
    tv.column('course_name', anchor=CENTER, width=100)
    tv.column('Duration', anchor=CENTER, width=100)
    tv.column('Fee', anchor=CENTER, width=100)
    tv.column('Teacher', anchor=CENTER, width=100)
    tv.column('Time', anchor=CENTER, width=100)
    tv.column('Mode', anchor=CENTER, width=100)

    tv.heading('course_name', text='Course Name', anchor=CENTER)
    tv.heading('Duration', text='Duration', anchor=CENTER)
    tv.heading('Fee', text='Fee', anchor=CENTER)
    tv.heading('Teacher', text='Teacher', anchor=CENTER)
    tv.heading('Time', text='Time', anchor=CENTER)
    tv.heading('Mode', text='Mode', anchor=CENTER)

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='236588@Er', db='project2')
    cur = db.cursor()

    cur.execute("SELECT * FROM course")
    result = cur.fetchall()
    for col in result:
        tv.insert("", 'end', values=(col[0], col[1], col[2], col[3], col[4], col[5]))


def showteachers():
    # Clear existing data
    for row in tv.get_children():
        tv.delete(row)

    # Configure treeview columns for teachers
    tv['columns'] = ('First Name', 'Last Name', 'Contact', 'Age', 'DOB', 'Qualification', 'Experience', 'Gender')
    tv.column('#0', width=0, stretch=NO)
    for col in tv['columns']:
        tv.column(col, anchor=CENTER, width=130)
        tv.heading(col, text=col, anchor=CENTER)

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='236588@Er', db='project2')
    cur = db.cursor()

    cur.execute("SELECT * FROM teacher_details")
    result = cur.fetchall()
    for col in result:
        tv.insert("", 'end', values=(col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7]))

def search():
    query = search_entry.get().strip()

    for row in tv.get_children():
        tv.delete(row)

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='236588@Er', db='project2')
    cur = db.cursor()

    # Try searching in courses first
    cur.execute("SELECT * FROM course WHERE course_name LIKE %s", ('%' + query + '%',))
    course_result = cur.fetchall()

    if course_result:
        # Display courses
        tv['columns'] = ('course_name', 'Duration', 'Fee', 'Teacher', 'Time', 'Mode')
        for col in tv['columns']:
            tv.column(col, anchor=CENTER, width=100)
            tv.heading(col, text=col, anchor=CENTER)
        tv.column('#0', width=0, stretch=NO)

        for row in course_result:
            tv.insert("", 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5]))

    else:
        # If no course matched, try teacher by first name
        cur.execute("SELECT * FROM teacher_details WHERE name LIKE %s", ('%' + query + '%',))
        teacher_result = cur.fetchall()

        if teacher_result:
            tv['columns'] = ('Name', 'Last Name', 'Contact', 'Age', 'DOB', 'Qualification', 'Experience', 'Gender')
            for col in tv['columns']:
                tv.column(col, anchor=CENTER, width=130)
                tv.heading(col, text=col, anchor=CENTER)
            tv.column('#0', width=0, stretch=NO)

            for row in teacher_result:
                tv.insert("", 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        else:
            # Optional: Show "No result" in Treeview or popup
            tv['columns'] = ('Result',)
            tv.column('#0', width=0, stretch=NO)
            tv.column('Result', anchor=CENTER, width=600)
            tv.heading('Result', text='Search Result', anchor=CENTER)
            tv.insert("", 'end', values=("No matching course or teacher found.",))

    db.close()

Button(top,text='Add Teacher',font='Cambria 15',command=click1).place(x=100,y=100)
Button(top,text='Student Registeration',font='Cambria 15',command=click3).place(x=250,y=100)
Button(top,text='Add Courses',font=('Cambria 15'),command=click2).place(x=500,y=100)
Button(top,text='Show Courses',font=('Cambria 15'),command=showcourses).place(x=680,y=100)
Button(top,text='Show Teachers',font=('Cambria 15'),command=showteachers).place(x=850,y=100)
Button(top,text='Exit',font=('Cambria 15'),command=Exit).place(x=1030,y=100)
# Label(top,text='Search Course',font=('Cambria 15')).place(x=100,y=200)
# Entry (top,font=('Cambria 15')).place(x=250,y=200)
Button(top,text='Search',font=('Cambria 15')).place(x=500,y=200)

Label(top, text='Search', font=('Cambria 15')).place(x=100, y=200)
search_entry = Entry(top, font=('Cambria 15'))
search_entry.place(x=250, y=200)

Button(top, text='Search', font=('Cambria 15'), command=lambda: search()).place(x=500, y=200)

tv = ttk.Treeview(top)
tv['columns'] = ('course_name', 'Duration','Fee', 'Teacher', 'Time', 'Mode')
tv.column('#0', width=0, stretch=NO)
tv.column('course_name', anchor=CENTER, width=100)
tv.column('Duration', anchor=CENTER, width=100)
tv.column('Fee', anchor=CENTER, width=100)
tv.column('Teacher', anchor=CENTER, width=100)
tv.column('Time', anchor=CENTER, width=100)
tv.column('Mode', anchor=CENTER, width=100)

tv.heading('course_name', text='CourseName', anchor=CENTER)
tv.heading('Duration', text='Duration', anchor=CENTER)
tv.heading('Fee', text='Fee', anchor=CENTER)
tv.heading('Teacher', text='TeacherName', anchor=CENTER)
tv.heading('Time', text='Time', anchor=CENTER)
tv.heading('Mode', text='Mode', anchor=CENTER)

tv.place(x=50, y=300)

top.mainloop()