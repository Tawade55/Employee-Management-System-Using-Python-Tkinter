from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from tkinter import ttk
from sqlite3 import *
from requests import*
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import requests

def f1():
	mw.withdraw()
	aw.deiconify()
def f2():
	aw.withdraw()
	mw.deiconify()
def f3():
	mw.withdraw()
	vw.deiconify()
	vw_emp_data.delete(1.0,END)
	try:
		con=connect("emp1.db")
		cursor=con.cursor()
		sql="select*from employee"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info + " id= " + str(d[0]) + " name= " + str(d[1]) + " salary= " + str(d[2]) + "\n"
		vw_emp_data.insert(INSERT,info)
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
def f4():
	vw.withdraw()
	mw.deiconify()
def f5():
	con=None
	try:
		con=connect("emp1.db")
		cursor=con.cursor()
		sql="insert into employee values('%s','%s','%s')"
		id=aw_ent_id.get()
		if not id.isdigit() and int(id)<=0:
			raise ValueError()
		elif int(id)<1:
			raise IndexError("Id should be minimum one")
		
			
			
			
		name=aw_ent_name.get()
		if not all(x.isalpha() or x.isspace() for x in name):
			raise NameError("Name must be combination of Alphabets only")
		
		name=aw_ent_name.get()
		if len(name)<2:
			raise TypeError("Length of name must be minimum 2 letters")
		
		name=aw_ent_name.get()
		if len(name)==0:
			raise TypeError("Length of name must be  greater than or equal to 2")
		salary=aw_ent_salary.get()
		if not salary.isdigit():
			raise AttributeError("Salary should be in numbers only")
		
		salary=float(aw_ent_salary.get())
		if not salary >=8000:
			raise  ReferenceError("Salary Should be minimum 8000")
		
		
		cursor.execute(sql%(id,name,salary))
		con.commit()
		showinfo("Success","Record created")
	
	except ValueError as e:
		showerror("Issue","Id should be integer only and not blank")
		con.rollback()	
	except IndexError as e:
		showerror("Issue","Id should be minimum one")
	
	except NameError as e:
		showerror("Issue","Name must be combination of Alphabets only")
		
	except TypeError as e:
		showerror("Issue","Length of name must be  greater than or equal to 2")
	except  AttributeError as e:
		showerror("Issue","Salary should be in numbers only")
	except  ReferenceError as e:
		showerror("Issue","Salary Should be minimum 8000")
	except  Exception as e:
		showerror("Issue","Id Already Exists")
	finally:
		if con is not None:
			con.close()
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_salary.delete(0,END)
		aw_ent_id.focus()


def f6():
	mw.withdraw()
	uw.deiconify()
	#uw_emp_data.delete(1.0,END)
	con=None
	try:
		con=connect("emp1.db")
		cursor=con.cursor()
		sql="update employee set name ='%s',salary='%s' where id='%s'"
		id=uw_ent_id.get()
		if not id.isdigit():


			raise ValueError("Issue","Id should be integer only")

		
			
			
			
		name=uw_ent_name.get()
		if not all(x.isalpha() or x.isspace() for x in name):
			raise NameError("Name must be combination of Alphabets only")
		
		name=uw_ent_name.get()
		if len(name)<2:
			raise TypeError("Length of name must be minimum 2 letters")
		
		name=uw_ent_name.get()
		if len(name)==0:
			raise TypeError("Length of name must be  greater than or equal to 2")
		salary=uw_ent_salary.get()
		if not salary.isdigit():
			raise AttributeError("Salary should be in numbers only")
		
		salary=float(uw_ent_salary.get())
		if not salary >=8000:
			raise  ReferenceError("Salary Should be minimum 8000")
		
		
		cursor.execute(sql%(name,salary,id))
		if cursor.rowcount == 1:
			showinfo("Success","Record updated")
			con.commit()
		else:
			showerror("Failure","record does not exist")
	
	except ValueError as e:
		showerror("Issue","Id should be integer only and not blank")
		con.rollback()	
	#except IndexError as e:
		#showerror("Issue","Id should be minimum one")
	
	except NameError as e:
		showerror("Issue","Name must be combination of Alphabets only")
		
	except TypeError as e:
		showerror("Issue","Length of name must be  greater than or equal to 2")
	except  AttributeError as e:
		showerror("Issue","Salary should be in numbers only")
	except  ReferenceError as e:
		showerror("Issue","Salary Should be minimum 8000")
	#except  Exception as e:
		#showerror("Issue","Id Already Exists")
	finally:
		if con is not None:
			con.close()
		uw_ent_id.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_salary.delete(0,END)
		uw_ent_id.focus()


		

def f7():
	mw.withdraw()
	dw.deiconify()
	#dw_st_data.delete(1.0,END)
	#wapp to delete emp records

	con=None
	try:
		con=connect("emp1.db")
		cursor=con.cursor()
		sql="delete from employee where id = '%s' "
		id=int(dw_ent_id.get())
		id=dw_ent_id.get()
		if not id.isdigit():

			raise ValueError("Issue","ID must be in +ve Integer only and should not be blank")
		cursor.execute(sql %(id))
		if cursor.rowcount == 1:
			showinfo(id,"record deleted")
			con.commit()
		else:
			showerror(id,"record does not exist")
	except ValueError as e:
		con.rollback()
		showerror("issue","ID must be in +ve Integer only and should not be blank")
	finally:
		if con is not None:
			con.close()
		dw_ent_id.delete(0,END)
		dw_ent_id.focus()


def f8():
	uw.withdraw()
	mw.deiconify()


def f9():
	dw.withdraw()
	mw.deiconify()
	
def f11():
	mw.deiconify()
	cw.withdraw()
"""def f12():
	mw.deiconify()
	lw.withdraw()

def f13():	
	mw.withdraw()
	lw.deiconify()"""

def f10():
	mw.deiconify()
	cw.withdraw()


	try:
		con =connect("emp1.db")
		cursor = con.cursor()
		cursor.execute("select name,salary from employee order by salary desc limit 5")
		result = cursor.fetchall

		name = []
		salary = []
	
		for i in cursor:
			name.append(i[0])
			salary.append(i[1])
	
		plt.bar(name,salary)
		plt.xlabel("Name of Employee")
		plt.ylabel("Salary of Employee")
		plt.title("Top 5 Highest Salary Employee Information")
		plt.show()

	except Exception as e:
		if con is not None:
			showerror("Issue", e)
	finally:
		if con is not None:
			con.close()








mw=Tk()
mw.title("Employee Management System by Vivek")
mw.geometry("700x700+50+50")
mw.configure(bg="#FFFFC1")
f=("Arial",36,"bold")

canvas=Canvas(mw,width=1100,height=100)
image=ImageTk.PhotoImage(Image.open("C:\\Python Program's Practice\\EMP Project\\image.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()




	


ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\emp.png')
photo = ImageTk.PhotoImage(ico)
mw.wm_iconphoto(False, photo)




  

mw_btn_add=Button(mw,text="Add Employee",font=f,width=15,fg="#ffffff", bg="green",command=f1)
mw_btn_view=Button(mw,text="View Employee",font=f,width=15,fg="#ffffff", bg="#528DFF",command=f3)
mw_btn_update=Button(mw,text="Update Employee",font=f,width=15,fg="#ffffff", bg="grey",command=f6)
mw_btn_delete=Button(mw,text="Delete Employee",font=f,width=15,fg="#ffffff", bg="red",command=f7)
mw_btn_chart=Button(mw,text="Charts",font=f,width=15,fg="#ffffff", bg="purple",command=f10)
#mw_btn_loctemp=Button(mw,text="Location & Temp",font=f,command=f13)

mw_btn_add.pack(pady=10)
mw_btn_view.pack(pady=10)
mw_btn_update.pack(pady=10)
mw_btn_delete.pack(pady=10)
mw_btn_chart.pack(pady=10)
#mw_btn_loctemp.pack(pady=10)

aw=Toplevel(mw)
aw.title("Add employee")
aw.geometry("700x700+50+50")

aw_label=Label(aw,text="Add Employee Details",font=("Times New Roman", 40, "bold","underline"))
aw_lab_id=Label(aw,text="Enter Empoyee ID ",font=f)
aw_ent_id=Entry(aw,font=f)
aw_lab_name=Label(aw,text="Enter Name of an Employee",font=f)
aw_ent_name=Entry(aw,font=f)
aw_lab_salary=Label(aw,text="Enter Salary of an Employee",font=f)
aw_ent_salary=Entry(aw,font=f)
aw_btn_save=Button(aw,text="Save",font=f,fg="#ffffff",bg="grey",command=f5)
aw_btn_back=Button(aw,text="Back",font=f,fg="#ffffff",bg="coral",command=f2)
aw.configure(bg="#8B8B69")

aw_label.pack(pady=10)
aw_lab_id.pack(pady=10)
aw_ent_id.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lab_salary.pack(pady=10)
aw_ent_salary.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
aw.withdraw()


ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\businessman_add.png')
photo = ImageTk.PhotoImage(ico)
aw.wm_iconphoto(False, photo)



vw=Toplevel(mw)
vw.title("View employee")
vw.geometry("700x700+50+50")

vw_label=Label(vw,text="View Employee Details",font=("Times New Roman", 40, "bold","underline"))
vw_emp_data=ScrolledText(vw,width=200,height=8,font=f)
vw_btn_back=Button(vw,text="Back",fg="#ffffff",bg="coral",font=f,command=f4)

vw_label.pack(pady=10)
vw_emp_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()
vw.configure(bg="#CDCD9B")

ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\find-employee-icon.png')
photo = ImageTk.PhotoImage(ico)
vw.wm_iconphoto(False, photo)

uw=Toplevel(mw)
uw.title("Update employee")
uw.geometry("700x700+50+50")

uw_label=Label(uw,text="Update Employee Details",font=("Times New Roman", 40, "bold","underline"))
uw_lab_id=Label(uw,text="Enter Employee Id to be Updated ",font=f)
uw_ent_id=Entry(uw,font=f)
uw_lab_name=Label(uw,text="Enter Employee Name to be Updated ",font=f)
uw_ent_name=Entry(uw,font=f)
uw_lab_salary=Label(uw,text="Enter The Updated Salary ",font=f)
uw_ent_salary=Entry(uw,font=f)
uw_btn_save=Button(uw,text="Save",font=f,fg="#ffffff",bg="grey",command=f6)
uw_btn_back=Button(uw,text="Back",font=f,fg="#ffffff",bg="coral",command=f8)

uw_label.pack(pady=10)
uw_lab_id.pack(pady=10)
uw_ent_id.pack(pady=10)
uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10)
uw_lab_salary.pack(pady=10)
uw_ent_salary.pack(pady=10)
uw_btn_save.pack(pady=10)
uw_btn_back.pack(pady=10)
uw.withdraw()
uw.configure(bg="#EEEEB4")

ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\update.png')
photo = ImageTk.PhotoImage(ico)
uw.wm_iconphoto(False, photo)

dw=Toplevel(mw)
dw.title("Delete employee")
dw.geometry("700x700+50+50")

dw_label=Label(dw,text="Delete Employee Details",font=("Times New Roman", 40, "bold","underline"))
dw_lab_id=Label(dw,text="Enter Employee Id to be Deleted ",font=f)
dw_ent_id=Entry(dw,font=f)
dw_btn_save=Button(dw,text="Save",font=f,fg="#ffffff",bg="grey",command=f7)
dw_btn_back=Button(dw,text="Back",font=f,fg="#ffffff",bg="coral",command=f9)

dw_label.pack(pady=10)
dw_lab_id.pack(pady=10)
dw_ent_id.pack(pady=10)
dw_btn_save.pack(pady=10)
dw_btn_back.pack(pady=10)
dw.withdraw()
dw.configure(bg="#C0C0C0")

ico = Image.open('C:\\Users\\NEW\\OneDrive\\Pictures\\Saved Pictures\\delete.png')
photo = ImageTk.PhotoImage(ico)
dw.wm_iconphoto(False, photo)

cw=Toplevel(mw)
cw.title("Employee's performance")
cw.geometry("700x700+50+50")

"""cw_lab_name1=Label(cw,text="Enter Name of an Employee1",font=f)
cw_ent_name1=Entry(cw,font=f)
cw_lab_name2=Label(cw,text="Enter Name of an Employee2",font=f)
cw_ent_name2=Entry(cw,font=f)
cw_lab_name3=Label(cw,text="Enter Name of an Employee3",font=f)
cw_ent_name3=Entry(cw,font=f)
cw_lab_name4=Label(cw,text="Enter Name of an Employee4",font=f)
cw_ent_name4=Entry(cw,font=f)
cw_lab_name5=Label(cw,text="Enter Name of an Employee5",font=f)
cw_ent_name5=Entry(cw,font=f)

cw_lab_salary1=Label(cw,text="Enter Salary of an Employee1",font=f)
cw_ent_salary1=Entry(cw,font=f)
cw_lab_salary2=Label(cw,text="Enter Salary of an Employee2",font=f)
cw_ent_salary2=Entry(cw,font=f)
cw_lab_salary3=Label(cw,text="Enter Salary of an Employee3",font=f)
cw_ent_salary3=Entry(cw,font=f)
cw_lab_salary4=Label(cw,text="Enter Salary of an Employee4",font=f)
cw_ent_salary4=Entry(cw,font=f)
cw_lab_salary5=Label(cw,text="Enter Salary of an Employee5",font=f)
cw_ent_salary5=Entry(cw,font=f)"""


#cw_btn_save=Button(cw,text="Save",font=f,command=)
#cw_btn_back=Button(cw,text="Back",font=f,command=f11)

"""cw_lab_name1.pack(pady=2)
cw_ent_name1.pack(pady=2)
cw_lab_name2.pack(pady=2)
cw_ent_name2.pack(pady=2)
cw_lab_name3.pack(pady=2)
cw_ent_name3.pack(pady=2)
cw_lab_name4.pack(pady=2)
cw_ent_name4.pack(pady=2)
cw_lab_name5.pack(pady=2)
cw_ent_name5.pack(pady=2)

cw_lab_salary1.pack(pady=2)
cw_ent_salary1.pack(pady=2)
cw_lab_salary2.pack(pady=2)
cw_ent_salary2.pack(pady=2)
cw_lab_salary3.pack(pady=2)
cw_ent_salary3.pack(pady=2)
cw_lab_salary4.pack(pady=2)
cw_ent_salary4.pack(pady=2)
cw_lab_salary5.pack(pady=2)
cw_ent_salary5.pack(pady=2)"""

#cw_btn_save.pack(pady=2)
#cw_btn_back.pack(pady=2)
cw.withdraw()

"""lw=Toplevel(mw)
lw.title("Location and temperature")
lw.geometry("700x700+50+50")

lw_lab_loc=Label(lw,text="Enter Name of an City",font=f)
lw_ent_loc=Entry(lw,font=f)
lw_btn_save=Button(lw,text="Save",font=f,command=loc)
lw_btn_back=Button(lw,text="Back",font=f,command=f12)

lw_lab_loc.pack(pady=10)
lw_ent_loc.pack(pady=10)
lw_btn_save.pack(pady=10)
lw_btn_back.pack(pady=10)"""




#mw.title("Weather App")
#mw.geometry("700x700+50+50")
#f=("Times New Roman","40","bold")
try:
	a1="https://api.openweathermap.org/data/2.5/weather?"
	a2="q=" + "Mumbai"
	a3="&appid="+"c6e315d09197cec231495138183954bd"
	a4="&units=" +"metric"
	wa=a1+a2+a3+a4
	res=requests.get(wa)
	
	data=res.json()
	temp=data["main"]["temp"]
	lab_temp=Label(mw,text=temp,font=f,fg="red")
	lab_temp.place(x=950,y=700)
	lab_tempdeg=Label(mw,text="°C",fg="red")
	lab_tempdeg.place(x=1005,y=700)

	
	
	wa="https://ipinfo.io/"
	res=requests.get(wa)
	
	data=res.json()
	
	city=data["city"]

	lab_city=Label(mw,text=city,font=f,fg="red")
	lab_city.place(x=100,y=700)
except Exception as e:
	print("issue",e)


mw.mainloop()


































































		















