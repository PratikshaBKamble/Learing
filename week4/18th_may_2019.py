# -*- coding: utf-8 -*-
"""18th May 2019.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14dbi-hmddZH84m-S9vuKWb5ZIe26btDl
"""

#reverse string
x="Pratiksha"
y=5
z=len(x)
if(z!=y):
  print(x[y:9])
  print(x[-9:y])
  print(x[y::-1])

#to check type of dictionary
x={"Ram":1,"Laxshman":2}
print(type(x))
print(len(x))
x["Ram"]

#Dictionary example
x={"Pratiksha":[{"Empid":1187554,"DOB":17121994,"Gender":"Female"}]}
x["Pratiksha"][0]["Gender"]

x={"Ram":[{"Empid":1,"Dob":17121994,"Gender":"Male"}],"Lakshman":[{"Empid":2,"Dob":13121994,"Gender":"Male"}],"Charan":[{"Empid":3,"Dob":14121994,"Gender":"Female"}]}
y=str(input("Enter name")).capitalize()
z=str(input("Prefrence")).capitalize()

x[y][0][z]

#new value add in existing dictionary
color={"Vedant":"Pink",
      "Jovin":"Sky Blue",
      "Nitin":"Sky Blue",
      "Ishika":"Purple",
      "Komal":"Navy Blue",
      "Dipesh":"Oxf Blue"}
color["Pratiksha"]="Red"
color["Mayur"]="Pink"
print(color)

"""del method for dict"""

#delete value from dictionary
x={"Ram":[{"Empid":1,"Dob":17121994,"Gender":"Male"}],"Lakshman":[{"Empid":2,"Dob":13121994,"Gender":"Male"}],"Charan":[{"Empid":3,"Dob":14121994,"Gender":"Female"}]}

x["Ravan"]=[{"Empid":4,"Dob":21051994,"Gender":"Male"}]
del x["Ravan"]
print(x)

#add key & values in empty dictionary
x={}
def adduser():
    name=str(input("Enter your name"))
    empid=int(input("Enter your id"))
    gender=str(input("Enter your gender"))
    dob=int(input("Enter dob"))
    x[name]=[{"Empid":empid,"Gender":gender,"DOB":dob}]
    print(x)
adduser()


