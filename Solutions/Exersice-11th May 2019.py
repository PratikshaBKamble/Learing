name=str(input("Please enter your name"))
DOB=str(input("Please enter your dob"))
cy=str(input("Please enter current year"))
month_intrest= str(input("Please enter your month of intrest"))

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
def mi(month_intrest):
    list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    x=month_intrest.capitalize()
    if (x=="January" or x=="March" or x=="May"  or x=="July" or x=="August" or x=="October" or x=="December"):
        a=list[0:31]
        print("Your month of intrest has {} no of days".format(a))
    elif (x=="April" or x=="June" or x=="September" or x=="November"):
        a=list[0:30]
        print("Your month of intrest has {} no of days".format(a))
    elif(x=="February"):
        a=list[0:28]
        print("Your month of intrest has {} no of days".format(a))
    else:
        print("Invalid input")

m_d(m)
mi(month_intrest)


