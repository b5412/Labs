from random import randint
from time import sleep
def menu():
    while (True):
        choose=input("menu\n-----------\n1.dog details: \n2.friends list: \n3.n attzeret: \n")
        if (choose=="1"):
            dogs()
        elif(choose=="2"):
            friends()
        elif(choose=="3"):
            azzeret()
        else:
            print("enter 1-3 only!")
            continue
        exit=input("do you want to exit? y/n: ")
        if(exit=="y" or exit=="Y"):
            break
        else:
            print("welcome back!")
    print("Bye Bye..")
def dogs():
    name=input("Enter a dog name: ")
    Age=int(input("Enter the age: "))
    print("Dog details: \n" + "Name: " + name + "\n" + "Age: " + str(Age*7) + "\n")


def friends():
    freind_list=[]
    for i in range(5):
        freind_list.append(input("Enter a name: "))
    print(freind_list)
    name=input("Enter a name: ")
    if name in (freind_list):
        print("The name is found!")
    else:
        print(name + " is no found..")

def azzeret():
    namber=int(input("Enter a number: "))
    sum=1
    for i in range(1,namber+1):
        sum=sum*i
    print(str(namber) + " azzeret is: " + str(sum))











menu()

