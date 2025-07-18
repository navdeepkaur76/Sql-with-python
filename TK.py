from tkinter import*
import pymysql
import pymysql.cursors
from tkinter import messagebox
conn=pymysql.connect(host='localhost',user='root',db='happy')
a=conn.cursor()
def show_entry_fields():
    data = (
        f"Emp no: {e1.get()}\n"
        f"First Name: {e2.get()}\n"
        f"Last Name: {e3.get()}\n"
        f"Age: {e4.get()}\n"
        f"Sex: {e5.get()}\n"
        f"Income: {e6.get()}"
    )
    show_output(data)
master=Tk()
Label(master,text="Emp no").grid(row=0)
Label(master,text="First Name").grid(row=1)
Label(master,text="Last Name").grid(row=2)
Label(master,text="Age").grid(row=3)
Label(master,text="Sex").grid(row=4)
Label(master,text="Income").grid(row=5)
e1=Entry(master)
e2=Entry(master)
e3=Entry(master)
e4=Entry(master)
e5=Entry(master)
e6=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
def clear_fields():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

def add_record():
    emp = e1.get()
    fn = e2.get()
    ln = e3.get()
    age = e4.get()
    sex = e5.get()
    income = e6.get()
    insert = "INSERT INTO SMILE (EMP_NO, FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (emp, fn, ln, age, sex, income)
    a.execute(insert, values)
    conn.commit()
def print_all():
    sql = "SELECT * FROM SMILE"
    try:
        a.execute(sql)
        results = a.fetchall()
        display_text = ""
        for row in results:
            display_text += (
                f"EMP NO = {row[0]}, First Name = {row[1]}, Last Name = {row[2]}, "
                f"Age = {row[3]}, Sex = {row[4]}, Income = {row[5]}\n"
            )
        show_output(display_text)
    except Exception as e:
        show_output(f"Error: unable to fetch data\n{e}")
def delete_record():
    emp_no = e1.get()
    if not emp_no:
        result_label.config(text="Please enter an Emp No to delete.", fg="red")
        return

    confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
    if not confirm:
        result_label.config(text="Deletion cancelled.", fg="red")
        return

    try:
        sql = "DELETE FROM SMILE WHERE emp_no = %s"
        a.execute(sql, (emp_no,))
        conn.commit()
        
    except pymysql.MySQLError as e:
        result_label.config(text=f"Error: {e}", fg="red")
def update_record():
    emp_no = e1.get()
    fname = e2.get()
    lname = e3.get()
    age = e4.get()
    sex = e5.get()
    income = e6.get()

    if not emp_no:
        result_label.config(text="Please enter Emp No to update.", fg="red")
        return

    sqlupd = """
        UPDATE SMILE 
        SET first_name = %s, last_name = %s, age = %s, sex = %s, income = %s 
        WHERE emp_no = %s
    """

    try:
        a.execute(sqlupd, (fname, lname, age, sex, income, emp_no))
        conn.commit()
        
    except pymysql.MySQLError as e:
        result_label.config(text=f"Error: {e}", fg="red")
def search_record():
    emp_no = e1.get()
    sql = "SELECT * FROM SMILE WHERE emp_no = %s"

    try:
        a.execute(sql, (emp_no,))
        result = a.fetchone()

        if result:
            
            e1.delete(0, END)
            e1.insert(0, result[0])

            e2.delete(0, END)
            e2.insert(0, result[1])

            e3.delete(0, END)
            e3.insert(0, result[2])

            e4.delete(0, END)
            e4.insert(0, str(result[3]))

            e5.delete(0, END)
            e5.insert(0, result[4])

            e6.delete(0, END)
            e6.insert(0, str(result[5]))

            
    except pymysql.MySQLError as e:
        result_label.config(text=f"Error: {e}", fg="red")
def show_output(text):
    output_box.delete("1.0", END)
    output_box.insert(END, text)
Button(master, text='Add Record', command=add_record).grid(row=6, column=0,
                                                           sticky=W, pady=(2, 0))
Button(master,text='Clear Field',command=clear_fields).grid(row=6,column=1,
                                                    sticky=W,pady=4)
Button(master,text='Data',command=print_all).grid(row=6,column=2,
                                                    sticky=W,pady=4)
Button(master,text='Quit',command=master.quit).grid(row=6,column=3,
                                                    sticky=W,pady=4)
Button(master,text='Show',command=show_entry_fields).grid(row=6,column=4,
                                                    sticky=W,pady=4)
Button(master,text='Delete',command=delete_record).grid(row=7,column=0,
                                                    sticky=W,pady=4)
Button(master,text='Update',command=update_record).grid(row=7,column=1,
                                                    sticky=W,pady=4)
Button(master,text='Search',command=search_record).grid(row=7,column=2,
                                                    sticky=W,pady=4)
output_box = Text(master, height=6, width=80, fg="darkgreen", wrap=WORD)
output_box.grid(row=9, column=0, columnspan=5, padx=5, pady=(2, 10))
result_label = Label(master, text="", fg="blue", justify=LEFT)
result_label.grid(row=8, column=0, columnspan=5, sticky=W, pady=2)
mainloop()


