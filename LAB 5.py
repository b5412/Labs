my_dict= {"dekel":10000 , "niv":15000 , "amit":20000 , "dvir":25000 , "ben":30000}
print(my_dict)
summery=(my_dict["dekel"] + my_dict["ben"])
print("The summery is: " + str(summery))
my_dict.update({"avi":summery})
print(my_dict)
print("number of entries: " + str(len(my_dict)))
print("idan" in my_dict)