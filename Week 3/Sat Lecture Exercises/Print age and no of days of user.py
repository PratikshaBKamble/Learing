name=str(input("Please enter your name"))
DOB=str(input("Please enter your dob"))
cy=str(input("Please enter current year"))

year=DOB[4:8]
age=int(cy)-int(year)
#print(age)

month=DOB[2:4]
#print(int(month))
m=int(month)

def m_d(m):
    if (m==2):
        print("Hi,{} your {} year old.Your bday month has 28 no of days".format(name,age))
    elif(m==1 or m==3 or m==5 or m==7  or m==8 or m==10 or m==12):
        print("Hi,{} your {} year old.Your bday month has 31 no of days".format(name,age))
    elif (m==4 or m==6 or m==9 or m==11):
        print("Hi,{} your {} year old.Your bday month has 30 no of days".format(name,age))
    else:
        print("Invalid input")
m_d(m)


