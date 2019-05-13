x=str(input("Please enter your name"))

def nick_name(x):
    Y = str(input("Enter the letters that you want to append"))
    Z = int(input("Enter the no of initials to your nickname"))
    nickname = x[0:Z] + Y
    print("Your nickname is:",nickname)
nick_name(x)