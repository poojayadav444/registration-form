from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

# Heading
Label(root, text="Student Registration Form", font="arial 15 bold").grid(row=0, column=3)

#Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
email = Label(root, text="Email")
gender= Label(root, text="Gender")
age= Label(root, text="Age")

#Packinf Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
age.grid(row=4, column=2)
email.grid(row=5, column=2)

# Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
agevalue = StringVar
emailvalue = StringVar
checkvalue = IntVar

#Creating entry field
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
ageentry = Entry(root, textvariable =agevalue)
emailentry = Entry(root, textvariable =emailvalue)

#Packing entry fields
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
ageentry.grid(row=4,column=3)
emailentry.grid(row=5,column=3)

# Creating checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column= 3)

# Submit button
Button(text="Submit", command=getvals).grid(row=7,column=3)

root.mainloop()