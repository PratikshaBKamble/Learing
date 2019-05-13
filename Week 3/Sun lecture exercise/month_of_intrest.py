month= str(input("Please enter your month of intrest"))
def mi(month):
    list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    x=month.capitalize()
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
mi(month)
