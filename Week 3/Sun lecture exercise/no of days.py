m=str(input("Please enter month:"))
month=m.capitalize()
def m_d(month):
    if month=="February":
        print("Your selected {} has 28 no of days".format(month))
    elif month=="January" or month=="March" or month=="May" or month=="July" or month=="August" or month=="October" or month=="December":
        print("Your selected {} has 31 no of days".format(month))
    elif month=="April" or month=="June" or month=="September" or month=="November":
        print("Your selected {} has 30 no of days".format(month))
    else:
        print("Invalid output")
m_d(month)




