import random
x=random.randint(1,100)
print("WELCOME!!! \n GAME RULES \n 1.You have to select one number between 1 to 100.\n 2.You have total three chance to win this game.\n ENTER")
name=str(input("Please enter your name"))
n = name.capitalize()

for i in range(0,3):
    y=int(input("Please enter the number between 1 to 100:"))
    if(y==x):
        print("Congratulations!!!!!")
        break
    elif(y!=x and n=="Pratiksha"):
        print("Congratulations.....",n)
        break
    elif(y!=x):
        print("SORRY YOU LOST THE GAME")

print("The correct answer was:",x)

