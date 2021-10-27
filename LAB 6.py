menu=input("Menu: \n1.insert number **3\n2.insert 4 ip and print\n3.insert 4 dns\n4.check if string is polindrom")
if(menu=="1"):
    print(int(input("enter number: "))**3)
elif(menu=="2"):
    lista=[]
    lista.append(input("enter ip: "))
    lista.append(input("enter ip: "))
    lista.append(input("enter ip: "))
    lista.append(input("enter ip: "))
    print("the list is: " + str(lista))
elif(menu=="3"):
    dns_e={}
    dns_e.update({input("enter url: ") : input("enter ip: ")})
    dns_e.update({input("enter url: ") : input("enter ip: ")})
    dns_e.update({input("enter url: ") : input("enter ip: ")})
    dns_e.update({input("enter url: ") : input("enter ip: ")})
    print("dns list is : " + str(dns_e))
elif(menu=="4"):
    word=input("Enter a word: ")
    if (word==word[::-1]):
        print("it is good !")
    else:
        print("is no good !")
else:
    print("choose 1-4!!")
