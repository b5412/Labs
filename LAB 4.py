
my_list= ["bar moshe",22,"bar@gmail.com","0500000000"]
print(my_list)
print("my name: " + my_list[0] + "\nAge: " + str (my_list[1]) + "\nMail: " + my_list[2] + "\nphone number: " + my_list[3])


ip_list= ["1.1.1.1","2.2.2.2"]
print(ip_list)
ip_list.append("3.3.3.3")
ip_list.append("4.4.4.4")
ip_list.append("5.5.5.5")
print(ip_list)

ip_list.pop(2)
print("ip list length is: " + str(len(ip_list)) + "\nthe ip list is: " + str(ip_list))



