# print("a",end=" ")
# print("b",end=" ")
# print("c",end=" ")
# print()
print("a","b","c",sep="-")
print("a","b","c",sep=",")
print("-------------")
#Strings
print("prajesh"+"waghela")
name="prajesh waghela"
print(len(name))

# #replication of a string
print("prajesh "*5)

# #slicing
print(name[0:5])
print(name[1:5])
print("Hustle"[0])
print("Hustle"[-1])
print("Hustle"[::-1])  #Reverse a string
print("Hustle"[-5:-1])
print("Hustle"[::-1][0:3])
print("-"*20)
print("Prajesh".lower())
print("Prajesh".upper())
print("-"*20)
print("    Prajesh  ".strip())
print("    Prajesh  ".rstrip())
print("    Prajesh  ".lstrip())
print("-"*20)
print("Prajesh".replace("ra","ru"))
print("Prajesh".count("a"))
print("prajesh waghela".find("jesh"))
print("prajesh waghela".index("wag"))
print("Prajesh".isalpha())
print("Prajesh1234".isalnum())
print("prajesh waghela".capitalize()) #Take the first word as capital and rest all lower case
print("prajesh waghela".title()) #first character of every word is upper case
print("prajesh waghela".startswith("pra"))
print("prajesh waghela".endswith("ela"))
print("-"*20)
print("Prajesh Waghela".center(20,"*"))
print("Prajesh Waghela".ljust(20,"*"))
print("Prajesh Waghela".rjust(20,"*"))

print("*"*20)
#Variables
a,b,c,d=1,2,3,4
print(a,b,c,d)
age=input("Enter the age: ")
print(age)

#naming convention
#1) Snack Case(my_variable_name)
#2) Camel Case (myVaraibleName)
#3) Passcal case (MyVariableName)








