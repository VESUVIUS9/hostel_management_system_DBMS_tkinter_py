from tkinter import *
import tkinter.messagebox as MessageBox
from mysql.connector import (connection)
from PIL import ImageTk, Image  
from tkinter import ttk

#before executing change path of picture

def fee_details():
    fee=Tk()
    mydb = connection.MySQLConnection(
                host = "localhost",
                user = "root",
                passwd = "hello",
                database = "hostel"
                )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Fees_bill1;")
    student1=cursor.fetchall()
    
    fee.title("SHOW")
    fee.configure(bg='#041d78')
   
    label = Label(fee, text="FEE DETAILS", font=("Arial",10)).grid(row=0, columnspan=3)
    
    cols = ('stud_id', 'room_no', 'paid_sem_fees','mess_bill','canteen_bill','bill')
    listBox = ttk.Treeview(fee, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)
        
   
    # for row in rows:
    #          insertdata=str(row[0])+ '  '+ row[1]+ ' '+row[2]+ ' '+ row[3]+ ' '+ row[4]+ '   '+ row[5]+ ' ' + str(row[6])
    #          listBox = ttk.Treeview(show1, columns=insertdata, show='headings')
    #          list.insert(list.size()+1,insertdata)
    i=0 
    for student in student1: 
        for j in range(len(student)):
            e = Entry(listBox, width=20, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    fee.mainloop()
    
    mydb.close()
    
def Hstudent_details():
    show1=Tk()
    mydb = connection.MySQLConnection(
                host = "localhost",
                user = "root",
                passwd = "hello",
                database = "hostel"
                )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM test;")
    student1=cursor.fetchall()
    
    show1.title("SHOW")
    show1.configure(bg='#041d78')
   
    label = Label(show1, text="Student Records", font=("Arial",10)).grid(row=0, columnspan=3)
    
    cols = ('stud_id', 'stud_name', 'stud_dept','stud_year','stud_room_no','stud_addr','stud_phone')
    listBox = ttk.Treeview(show1, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)
    i=0 
    for student in student1: 
        for j in range(len(student)):
            e = Entry(listBox, width=20, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    show1.mainloop()
    mydb.close()
    
    
   
    
def update_stu():
    update=Toplevel()
    update.geometry("800x450")
    update.title("UPDATION")
    bcg=ImageTk.PhotoImage(Image.open(r'C:\coding\project hostel management\1st edit.jpg','r'))
    my_canvas = Canvas(update, width=800, height=450)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0,0, image=bcg, anchor="nw")
    student= Label(update,text='ENTER STUDENT ID',font=('bold',10))
    student.place(x=40,y=50)
        
    sname= Label(update,text='ENTER STUDENT NAME',font=('bold',10))
    sname.place(x=40,y=100)
    dept= Label(update,text='ENTER DEPT NUMBER',font=('bold',10))
    dept.place(x=40,y=150)
    year= Label(update,text='ENTER STUDENT YEAR',font=('bold',10))
    year.place(x=40,y=200)
    room_no= Label(update,text='ENTER ROOM NUMBER',font=('bold',10))
    room_no.place(x=40,y=250)
    adress= Label(update,text='ENTER ADRESS',font=('bold',10))
    adress.place(x=40,y=300)
    phone= Label(update,text='ENTER PHONE NO',font=('bold',10))
    phone.place(x=40,y=350)
    e1_student= Entry(update, show=None, font=('Arial', 14))
    e1_sname = Entry(update, show=None, font=('Arial', 14))
    e1_dept = Entry(update, show=None, font=('Arial', 14))
    e1_year= Entry(update, show=None, font=('Arial', 14))
    e1_room_no= Entry(update, show=None, font=('Arial', 14))
    e1_adress= Entry(update, show=None, font=('Arial', 14))  
    e1_phone= Entry(update, show=None, font=('Arial', 14)) 
    e1_student.place(x=200,y=50)
    e1_sname.place(x=200,y=100)
    e1_dept.place(x=200,y=150)
    e1_year.place(x=200,y=200)
    e1_room_no.place(x=200,y=250)
    e1_adress.place(x=200,y=300)
    e1_phone.place(x=200,y=350)
    
    def a4():
            studentid=e1_student.get()
            sname=e1_sname.get()
            dept=e1_dept.get()
            year=e1_year.get()
            room_no=e1_room_no.get()
            adress=e1_adress.get()
            phone=e1_phone.get()
            if(studentid=="" or sname=="" or adress=="" or dept=="" or room_no=="" or phone==""):
                MessageBox.showinfo("Insert Status","All Fields are required")
            else:
                mydb = connection.MySQLConnection(
                host = "localhost",
                user = "root",
                passwd = "hello",
                database = "hostel"
                )
                cursor = mydb.cursor()
                cursor.execute("update student set stud_name='"+ sname+"',stud_addr='"+adress+"',stud_dept='" + dept+ "',stud_phone='"+phone+"',stud_room_no='"+room_no+"' where stud_id='"+ studentid+"'")
                cursor.execute("commit")
                MessageBox.showinfo("updating values are!","('"+ studentid +"','"+ sname +"','"+ adress +"','"+ dept +"','"+ phone+"','"+room_no+"')")
                cursor.execute("commit")
                
                e1_student.delete(0,'end')
                e1_sname.delete(0,'end')
                e1_adress.delete(0,'end')
                e1_phone.delete(0,'end')
                e1_dept.delete(0,'end')
                e1_room_no.delete(0,'end')
                      
                MessageBox.showinfo("Update Status","updated Successfully")
                mydb.close()
    update1= Button(update, text="UPDATE", font=("italic",15),bg="#10044d",fg="white",command=a4)
    update1.place(x=300,y=405)
    update.mainloop()
def insertion():
    insert=Toplevel()
    insert.geometry("800x500")
    insert.title("INSERTION")
    bcg=ImageTk.PhotoImage(Image.open(r'C:\coding\project hostel management\1st edit.jpg','r'))
    my_canvas = Canvas(insert, width=800, height=450)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0,0, image=bcg, anchor="nw")
    studentid= Label(insert,text='ENTER STUDENT ID',font=('bold',10))
    studentid.place(x=40,y=50)
        
    sname= Label(insert,text='ENTER STUDENT NAME',font=('bold',10))
    sname.place(x=40,y=100)
    dept= Label(insert,text='ENTER STUDENT DEPT',font=('bold',10))
    dept.place(x=40,y=150)
    year= Label(insert,text='ENTER STUDENT YEAR',font=('bold',10))
    year.place(x=40,y=200)
        
    room_no= Label(insert,text='ENTER STUDENT ROOM NO',font=('bold',10))
    room_no.place(x=40,y=250)
    address= Label(insert,text='ENTER STUDENT ADDRESS',font=('bold',10))
    address.place(x=40,y=300)
    phone= Label(insert,text='ENTER STUDENT PHONE NO',font=('bold',10))
    phone.place(x=40,y=350)
    # sem= Label(insert,text='ENTER ROOM NUMBER',font=('bold',10))
    # sem.place(x=40,y=400)-
        
    e1_studentid= Entry(insert, show=None, font=('Arial', 14))
    e1_sname = Entry(insert, show=None, font=('Arial', 14))
    e1_dept = Entry(insert, show=None, font=('Arial', 14))
    e1_year= Entry(insert, show=None, font=('Arial', 14))
    e1_roomno= Entry(insert, show=None, font=('Arial', 14))
    e1_address= Entry(insert, show=None, font=('Arial', 14))
    e1_phone= Entry(insert, show=None, font=('Arial', 14))
    # e1_roomno= Entry(insert, show=None, font=('Arial', 14))
        
    e1_studentid.place(x=250,y=50)
    e1_sname.place(x=250,y=100)
    e1_dept.place(x=250,y=200)
    e1_year.place(x=250,y=150)
    
    e1_roomno.place(x=250,y=250)
    e1_address.place(x=250,y=300)
    e1_phone.place(x=250,y=350)
    # e1_roomno.place(x=200,y=400)
    def a1():
            studentid=e1_studentid.get()
            sname=e1_sname.get()
            dept=e1_dept.get()
            year=e1_year.get()
            room_no=e1_roomno.get()
            address=e1_address.get()
            phone=e1_phone.get()
            # roomno=e1_roomno.get()
            if(studentid=="" or sname=="" or dept=="" or year=="" or room_no=="" or address=="" or phone==""):
                MessageBox.showinfo("Insert Status","All Fields are required")
            else:
                mydb = mysql.connector.connect(
                host='localhost',
                user = 'root',
                passwd = 'hello',
                database = 'hostel'
                )
                cursor = mydb.cursor()
                cursor.execute("insert into test values('"+ studentid +" ','"+ sname +"','"+ dept +"','"+ year +"','"+ room_no +"','"+ address +"','"+ phone +"')")
                cursor.execute("commit")
                MessageBox.showinfo("inserted values are!","('"+ studentid +" ','"+ sname +"','"+ dept +"','"+ year +"','"+ room_no +"','"+ address +"','"+ phone +"')")
                cursor.execute("commit")
                e1_studentid.delete(0,'end')
                e1_sname.delete(0,'end')
                e1_dept.delete(0,'end')
                e1_year.delete(0,'end')
                e1_roomno.delete(0,'end')
                e1_address.delete(0,'end')
                e1_phone.delete(0,'end')
                # e1_roomno.delete(0,'end')
                
                         
                MessageBox.showinfo("Insert Status","Inserted Successfully")
                mydb.close()
    insert1= Button(insert, text="INSERT", font=("italic",15),bg="#10044d",fg="white",command=a1)
    insert1.place(x=200,y=450)
    insert.mainloop()
def deletion():
    
    dele=Toplevel()
    dele.geometry("400x400")
    dele.title("DELETION")
    bcg=ImageTk.PhotoImage(Image.open(r'C:\coding\project hostel management\1st edit.jpg','r'))
    my_canvas = Canvas(dele, width=400, height=400)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0,0, image=bcg, anchor="nw")
    studentid= Label(dele,text='ENTER STUDENTID',font=('bold',20))
    studentid.place(x=50,y=70)
    e1_student= Entry(dele, show=None, font=('Arial', 15))
    e1_student.place(x=50,y=130)
    
    def a2():
        if(e1_student.get()==""):
            MessageBox.showinfo("delete status","ID is compolsary for delete")
        else:
           mydb = connection.MySQLConnection(
           host = "localhost",
           user = "root",
           passwd = "hello",
           database = "hostel"
                    )
           cursor = mydb.cursor()
           cursor.execute("delete from test where id='"+ e1_student.get()+"'")
           cursor.execute("commit")
            
            
           MessageBox.showinfo("Delete Status","Deleted Successfully")
           mydb.close()        
    dele1= Button(dele, text="DELETE", font=("italic",15),bg="#5cf5f7",fg="#10044d",command=a2)
    dele1.place(x=100,y=190)
    dele.mainloop()
def mess_info():
    mess=Tk()
    mydb = connection.MySQLConnection(
                host = "localhost",
                user = "root",
                passwd = "hello",
                database = "hostel"
                )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Mess_canteen1;")
    student1=cursor.fetchall()
    
    mess.title("SHOW")
    mess.configure(bg='#041d78')
   
    label = Label(mess, text="Menu", font=("Arial",10)).grid(row=0, columnspan=3)
    
    cols = ('item_no', 'menu', 'price','availibility','timimg')
    listBox = ttk.Treeview(mess, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)
        
   
    # for row in rows:
    #          insertdata=str(row[0])+ '  '+ row[1]+ ' '+row[2]+ ' '+ row[3]+ ' '+ row[4]+ '   '+ row[5]+ ' ' + str(row[6])
    #          listBox = ttk.Treeview(show1, columns=insertdata, show='headings')
    #          list.insert(list.size()+1,insertdata)
    i=0 
    for student in student1: 
        for j in range(len(student)):
            e = Entry(listBox, width=20, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    mess.mainloop()
    
    mydb.close()
def Hemployee_details():
    emp=Tk()
    mydb = connection.MySQLConnection(
                host = "localhost",
                user = "root",
                passwd = "hello",
                database = "hostel"
                )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Hemployee1;")
    student1=cursor.fetchall()
    
    emp.title("SHOW")
    emp.configure(bg='#041d78')
   
    label = Label(emp, text="Employee_details", font=("Arial",10)).grid(row=0, columnspan=3)
    
    cols = ('emp_id', 'emp_name', 'emp_designation','emp_dept','emp_addr','emp_phone','emp_salary','emp_date_of_join')
    listBox = ttk.Treeview(emp, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)
        
   
    # for row in rows:
    #          insertdata=str(row[0])+ '  '+ row[1]+ ' '+row[2]+ ' '+ row[3]+ ' '+ row[4]+ '   '+ row[5]+ ' ' + str(row[6])
    #          listBox = ttk.Treeview(show1, columns=insertdata, show='headings')
    #          list.insert(list.size()+1,insertdata)
    i=0 
    for student in student1: 
        for j in range(len(student)):
            e = Entry(listBox, width=20, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    emp.mainloop()
    
    mydb.close()
def Hvisitors():
    emp=Tk()
    mydb = connection.MySQLConnection(
                host = "localhost",
                user = "root",
                passwd = "hello",
                database = "hostel"
                )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Hvisitors;")
    student1=cursor.fetchall()
    
    emp.title("SHOW")
    emp.configure(bg='#041d78')
   
    label = Label(emp, text="visitors_details", font=("Arial",10)).grid(row=0, columnspan=3)
    
    cols = ('visitor_id', 'visitor_name', 'visit_purpose','visit_to','visitor_addr','visitor_phone','visit_date')
    listBox = ttk.Treeview(emp, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)
        
   
    # for row in rows:
    #          insertdata=str(row[0])+ '  '+ row[1]+ ' '+row[2]+ ' '+ row[3]+ ' '+ row[4]+ '   '+ row[5]+ ' ' + str(row[6])
    #          listBox = ttk.Treeview(show1, columns=insertdata, show='headings')
    #          list.insert(list.size()+1,insertdata)
    i=0 
    for student in student1: 
        for j in range(len(student)):
            e = Entry(listBox, width=20, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    emp.mainloop()
    
    mydb.close()
def option():
    option=Toplevel()
    option.geometry("1000x600")
    option.title("HOSTEL PAGE")
    bcg=ImageTk.PhotoImage(Image.open(r'C:\coding\project hostel management\1st edit.jpg','r'))
    my_canvas = Canvas(option, width=1000, height=600)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0,0, image=bcg, anchor="nw")
    insert= Button(option, text="INSERT NEW STUDENT", font=("italic",20),bg="#10044d",fg="white",command=insertion)
    insert.place(x=10,y=75)
    delete= Button(option, text="DELETE STUDENT", font=("italic",20),bg="#10044d",fg="white",command=deletion)
    delete.place(x=10,y=200)
    update= Button(option, text="UPDATE STUDENT", font=("italic",20),bg="#10044d",fg="white",command=update_stu)
    update.place(x=10,y=350)
    total= Button(option, text="FEE DETAILS", font=("italic",20),bg="#10044d",fg="white",command=fee_details)
    total.place(x=750,y=75)
    Hstudent= Button(option, text="HOSTEL STUDENT DETAILS", font=("italic",20),bg="#10044d",fg="white",command=Hstudent_details)
    Hstudent.place(x=600,y=200)
    mess_canteen= Button(option, text="MESS CANTEEN INFO", font=("italic",20),bg="#10044d",fg="white",command=mess_info)
    mess_canteen.place(x=600,y=350)
    Hemployee= Button(option, text="HOSTEL EMPLOYEE INFO", font=("italic",20),bg="#10044d",fg="white",command=Hemployee_details)
    Hemployee.place(x=10,y=500)
    Hemployee= Button(option, text="HOSTEL VISITORS INFO", font=("italic",20),bg="#10044d",fg="white",command=Hvisitors)
    Hemployee.place(x=600,y=500)
    option.mainloop()

def ADMINlogin():
    
    hostel = Toplevel()
    hostel.geometry("525x328")
    hostel.title("ADMIN Login page")
    
    bcg=ImageTk.PhotoImage(Image.open(r'C:\coding\project hostel management\1st edit.jpg','r'))
    my_canvas = Canvas(hostel, width=525, height=328)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0,0, image=bcg, anchor="nw")
    ide=Label(hostel,text='ADMIN LOGIN PAGE',bg="#041d78",fg="#83e6e6",font=('bold',20))
    
    ide.place(x=200,y=20)
    
    name= Label(hostel,text='USER NAME',font=('bold',15))
    name.place(x=70,y=80)
    
    
    name = Label(hostel,text='PASSWORD',font=('bold',15))
    name.place(x=70,y=130)
    e1 = Entry(hostel, show=None, font=('Arial', 17))  
    e2 = Entry(hostel, show='*', font=('Arial', 17))   
    e1.place(x=230,y=80)
    e2.place(x=230,y=130)
    
    def submit():
        name=e1.get()
        password=e2.get()
        if name=='ak' or password=='123':
            option()

        
        # if(name=="" or password==""):
        #     MessageBox.showerror("Insert Status","All Fields are required")
        # else:
            
        #     mydb = connection.MySQLConnection(
        #     host = "localhost",
        #     user = "root",
        #     passwd = "Anusha@123",
        #     database = "hostel"
        #     )
        #     mycursor = mydb.cursor()
        #     sql = "SELECT * FROM hostellogin WHERE  name = '%s' AND  password = '%s'" % (e1.get(),e2.get())
        #     mycursor.execute(sql)
        #     if mycursor.fetchone():
        #         MessageBox.showinfo("LOGIN Status","successful") 
        #         option()
        #         hostel.quit()
                
        #     else:
        #         MessageBox.showerror("LOGIN Status","Invalid password or username")
                        
        
            
    
    submits= Button(hostel, text='SUBMIT', font=("italic",20),bg="#05f6fa",fg="blue",command=submit)
    submits.place(x=200,y=200)
    hostel.mainloop()

def room_details():
    emp=Tk()
    mydb = connection.MySQLConnection(
                host = "localhost",
                user = "root",
                passwd = "hello",
                database = "hostel"
                )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Hroom1;")
    student1=cursor.fetchall()
    
    emp.title("SHOW")
    emp.configure(bg='#041d78')
   
    label = Label(emp, text="room_details", font=("Arial",10)).grid(row=0, columnspan=3)
    
    cols = ('room_no', 'allocated_to', 'roommate','no_of_chairs','no_of_beds','coolere_available',)
    listBox = ttk.Treeview(emp, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)
        
   
    # for row in rows:
    #          insertdata=str(row[0])+ '  '+ row[1]+ ' '+row[2]+ ' '+ row[3]+ ' '+ row[4]+ '   '+ row[5]+ ' ' + str(row[6])
    #          listBox = ttk.Treeview(show1, columns=insertdata, show='headings')
    #          list.insert(list.size()+1,insertdata)
    i=0 
    for student in student1: 
        for j in range(len(student)):
            e = Entry(listBox, width=20, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    emp.mainloop()
    
    mydb.close()
    
def login():
    option=Toplevel()
    option.geometry("1000x600")
    option.title("STUDENT PAGE")
    bcg=ImageTk.PhotoImage(Image.open(r'C:\coding\project hostel management\1st edit.jpg','r'))
    my_canvas = Canvas(option, width=1000, height=600)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0,0, image=bcg, anchor="nw")
    insert= Button(option, text="SHOW STUDENT DETAILS", font=("italic",20),bg="#10044d",fg="white",command=Hstudent_details)
    insert.place(x=10,y=75)
    delete= Button(option, text="SHOW MESS DETAILS", font=("italic",20),bg="#10044d",fg="white",command=mess_info)
    delete.place(x=10,y=200)
    update= Button(option, text="SHOW FEES DETAILS", font=("italic",20),bg="#10044d",fg="white",command=fee_details)
    update.place(x=10,y=350)
    total= Button(option, text="SHOW ROOM DETAILS", font=("italic",20),bg="#10044d",fg="white",command=room_details)
    total.place(x=400,y=75)
    
    option.mainloop()
def logout():
    logout = Toplevel()
    logout.geometry("600x300")
    logout.title("student Login page")
    bcg=ImageTk.PhotoImage(Image.open('1st edit.jpg'))
    my_canvas = Canvas(logout, width=600, height=300)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0,0, image=bcg, anchor="nw")
    sname= Label(logout,text='ENTER YOUR NAME',font=('bold',10))
    sname.place(x=20,y=30)
    hostelid= Label(logout,text='ENTER YOUR HOSTELID',font=('bold',10))
    hostelid.place(x=20,y=60)
    place= Label(logout,text='ENTER PLACE',font=('bold',10))
    place.place(x=20,y=100)
    sem= Label(logout,text='ENTER SEM',font=('bold',10))
    sem.place(x=20,y=130)
    date= Label(logout,text='ENTER DATE',font=('bold',10))
    date.place(x=20,y=160)
    time= Label(logout,text='ENTER TIME',font=('bold',10))
    time.place(x=20,y=190)
    e1_sname = Entry(logout, show=None, font=('Arial', 14))
    e1_hostelid= Entry(logout, show=None, font=('Arial', 14))
    e1_place= Entry(logout, show=None, font=('Arial', 14))
    e1_sem= Entry(logout, show=None, font=('Arial', 14))
    e1_date= Entry(logout, show=None, font=('Arial', 14))
    e1_time= Entry(logout, show=None, font=('Arial', 14))
    
    e1_hostelid.place(x=200,y=30)
    e1_sname.place(x=200,y=70)
    e1_place.place(x=200,y=100)
    e1_sem.place(x=200,y=130)
    e1_date.place(x=200,y=160)
    e1_time.place(x=200,y=190)
    def logoutsubmit():
        hostelids=e1_hostelid.get()
        sname=e1_sname.get()
        place=e1_place.get()
        sem=e1_sem.get()
        date=e1_date.get()
        time=e1_time.get()
         
        if(hostelid=="" or sname=="" or place=="" or sem=="" or date=="" or time==""):
            MessageBox.showinfo("Insert Status","All Fields are required")
        else:
            con= connection.MySQLConnection(host="localhost",user="root",password="Anusha@123",database="hostel")
            cursor = con.cursor()
            cursor.execute("insert into logout (hostelids,sname,place,sem,date,time)  values('"+ hostelids+"','"+ sname +"','"+ place +"','"+ sem +"','"+ date +"','"+ time +"')")
            cursor.execute("commit")
            MessageBox.showinfo("Insert Status","Inserted Successfully")
            
            e1_hostelid.delete(0,'end')
            e1_sname.delete(0,'end')
            e1_place.delete(0,'end')
            e1_sem.delete(0,'end')
            e1_date.delete(0,'end')
            e1_time.delete(0,'end')
            con.close()
    logoutsubmit= Button(logout, text="SUBMIT", font=("italic",15),bg="#0afff7",command=logoutsubmit)
    logoutsubmit.place(x=130,y=250)
    
    logout.mainloop()
def LOG():
    log=Toplevel()
    log.geometry("600x500")
    log.title("LOG PAGE")
    #log.configure(bg='blue')
    back=ImageTk.PhotoImage(Image.open(r'C:\coding\project hostel management\1st edit.jpg','r'))
    my_canvas1 = Canvas(log, width=600, height=500)
    my_canvas1.pack()
    my_canvas1.create_image(0,0, image=back, anchor="nw")
    
    ide=Label(log,text='HOSTEL',bg="#041d78",fg="#83e6e6",font=('bold',30))
    
    ide.place(x=250,y=40)
    
    butLI= Button(log, text="LOGIN", font=("italic",20),bg="#07f7cb",command=lambda:[login()])
    butLI.place(x=190,y=200)
    # butLO= Button(log, text="LOGOUT", font=("italic",20),bg="#07f7cb",command=logout)
    # butLO.place(x=190,y=300)
    log.mainloop()
    
def root():
    root= Tk()
   
    
    root.geometry("700x466")
    root.title("HOSTEL DATABASE")
    img =ImageTk.PhotoImage(Image.open(r'C:\coding\project hostel management\1st edit.jpg','r'))
    canvas = Canvas(root, width = 700, height = 466)
    canvas.pack()
    
    canvas.create_image(20, 20, anchor=NW, image=img)
   
    ide=Label(root,text='LOGIN PAGE',bg="#041d78",fg="#83e6e6",font=('bold',30))
    
    ide.place(x=180,y=30)
    but1= Button(root, text="ADMIN LOGIN", font=("italic",20),bg="#83e6e6",command=lambda:[ADMINlogin()])
    
    but1.place(x=190,y=170)
    but2= Button(root, text="STUDENT LOGIN", font=("italic",20),bg="#83e6e6",command=lambda:[LOG(),root.quit])
    but2.place(x=190,y=250)
    root.mainloop()
root()
exit(0)