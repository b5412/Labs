# fibo=[1,2,3,5,8,13,21]
# boolend="True"
# for i in range(2,len(fibo)):
#     print(fibo[i])
#     print(fibo[i-1])
#     print(fibo[i-2])
#     print("\n")
#     if fibo[i]!=(fibo[i-1]+fibo[i-2]):
#         boolend = "False"
#         break
# if boolend=="True":
#     print("wow its good! ")
# else:
#     print("its not good!")
from random import randint
from time import sleep
while (True):
    choice=input("menu\n----------\n1.printing 100 numbers\n2.check fibo\n3.randint number until we get 12 or we count 10 times")
    if(choice=="1"):
        for i in range(1,101):
            print(i)
    elif(choice=="2"):
        #fibo=[1,2,3,5,8,13,21]
        fibo=[]
        for i in range(7):
            fibo.append(int(input("Enter a number: ")))
        boolean="True"
        for i in range(2,len(fibo)):
            print(fibo[i])
            print(fibo[i-1])
            print(fibo[i-2])
            print("\n")
        if fibo[i]!=(fibo[i-1]+fibo[i-2]):
            boolean = "False"
            break
        if boolean=="True":
            print("wow its good! ")
        else:
            print("its not good!")
    elif(choice=="3"):
        counter=1
        num=randint(1, 12)
        while(num!=12 and counter<11):
            print("Counter: " + str(counter) + " Number: " + str(num))
            counter=counter+1
            num = randint(1, 12)

    else:
        print("choose 1-3 only!!")
        continue
    exit=input("Do you want to exit ? y/n")
    if (exit=="y"):
            print("bye bye..")
            break









