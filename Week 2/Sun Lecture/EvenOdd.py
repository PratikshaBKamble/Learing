'''
num = int(input("Enter number"))

if ((num%2)==0):
    print("Even")
else:
    print("Odd")

a=5
b=2
c=a//b
print(c)

d=((num%2)==0)
print(type(d))

a=10
b=10
c=(a==b)
print(type(c))

a=int(input("value for a"))
b=int(input("value for b"))
c=int(input("value for c"))

if(a==b & b==c):
    print("good")
else:
    print("bad")
'''

X = [1,2,3,4,5,10,11,12]
Y=["Ram",2,"Love","U"]
print(type(X))
#b=Y([0]+Y[2]+Y[3]+Y[1]

name= str(input("Enter your name"))
#age = int(input("Enter your age"))
#hobby = str(input("Your hobby"))
#gender =str(input("Your gender"))
#x=name+ "is" +gender

#print("This indiviuals name is {},age is {} ,hobby is {} and gender is {}.format(name,age,hobby,gender))
#nickName=name[0:4]+"u"
nname =name[0:9:2]
print(name)
print(nname)

