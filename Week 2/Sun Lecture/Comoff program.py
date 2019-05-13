no_of_working_days=int(input("Please enter no of working days"))
compoff=int(input("Please enetr no of compoff days"))

if(no_of_working_days<=31 & compoff<=10):
  x=1000*no_of_working_days
  y=2000*compoff
  salary=x+y
  print("Your net salary is:",salary)
else:
  print("Invalid input")