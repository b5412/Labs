from random import randint
from time import sleep
print(randint(1,6))
print("Welcome to the game! ")
num=int(input("Enter your price: "))
turnes=int(num//3)
print("you can try " + str(num//3) + " times!\n" + "your change is: " + str((num%3)))
price=0
for i in range(turnes):
    print("round" + str(i+1))
    cube1=randint(1,6)
    cube2=randint(1,6)
    print("cube1: " + str(cube1) + "\n cube2: " + str(cube2))
if(cube1==cube2):
    if(cube1==6):
     price=price+1000
    else:
     price=price+100
elif(cube1==1):
     price=price+20
elif(cube2==2):
     price=price+40
print("your price is: " + str(price))