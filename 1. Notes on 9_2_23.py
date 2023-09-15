# #read from console
# #value = input ("please enter new string")
# #output the string
# #print (f'you entered {value}')

# #message = "ypou enetered  %s" (value)
# #print message

# #dictionaries 

# mydict ={
#     "firstname": "jane",
#     "lastname": "doe",
#     "birthyear": 2001
# }
# print (mydict)
# print (mydict[ "firstname"])
# fname = mydict.get("firstname")
# print (fname)

# mydict ={
#     "firstname" : "jane",
#     "lastname": "doe",
#     "birthyear": 2001,
#     "children": ["jack", "John", "james"]
# }
# mydict["birthyear"] = 2000
# print(mydict)

# mydict.update({"birthyear": 1990})
# print(mydict)

# if "children" in mydict: 
#     print("this person has children")
    
    
# mydict["father"] = "jeff"
# print(mydict)

# mydict.pop("father")
# print(mydict)

# mydict["father"] = "jeff"
# del mydict["father"]
# print(mydict)

# mydict.clear()
# print(mydict)

#lists
#ordered, changeable, allow duplications of datatypes
mylist = ["apple,", " kiwi", "pear"]
print(mylist)

mylist = ["apple,", " kiwi", "pear", "apple", "apple"]
print(mylist)

list_length = len(mylist)
print(list_length)

mylist = [100, 15, 77, 99, 300]
mylist = [False, False, True]

mylist = ["apple", 300, True, 400, "Alex", [1,3,5,7,9]]
print(mylist)

print(mylist[1])
print(mylist[-1]) # item from end of list

print(mylist[2:5]) #range
print(mylist[:5]) #range from start
print(mylist[-4:-1]) #range from end of list

if "Alex" in mylist:
    print("Alex is part of the list")
    
if "monica" in mylist:
    print("Monica is part of the list")
else: 
    print("Monica is not part of the list")
    
mylist[1] = 500
print(mylist)

mylist.insert(2, "totally unrelated string") # insert something at index
print(mylist)

mylist.append("YELLOW")
print(mylist)

more_colors = ["red","blue","green"]
mylist.extend(more_colors)
print(mylist)

mylist.pop(0) #remove items at index
print(mylist)

del mylist[-1]
print(mylist)

for x in mylist:
    print(x)
    
    
#ylist.sort() # doing this will lead to error due to different datat types

mylist = ["red", "orange", "blue", "green", "black"]
print(mylist)

mylist.sort()
print(mylist)

mylist.clear()
print(mylist)