lst=["Adnan","Aditya","Prajesh","Sagar","Saquib"]
print(lst)
#Modify Value
lst[1]="Abhirup"
print(lst)
#slicing
print(lst[0:2])
#reverse slicing
print(lst[::-1])
print(lst[-2::-2])
print(lst[-2::-1])

#removing specific element from the list
lst.remove("Abhirup")
print(lst)

#sorting a list
lst1=[3,23,44,67,899,433,21,3,3,3]
print(lst1)
print(sorted(lst1))

#finding an element
print(lst1.index(44))

#count the frequency of an element in a list
print(lst1.count(3))

#Extending a list : using extended() we can append multiple values at the same time in a list
lst.extend(["Mozzam","Milind"])
print(lst)

#Max and Min value in a list
print("Maximum value in a list:",max(lst1))
print("Manimum value in a list:",min(lst1))


#reverse a list using for loop
for i in range(len(lst1)-1,-1,-1):
    print(lst1[i])


#multidimensional list
details=[["Prajesh",34,76,88,54,90],
        ["Adnan",64,54,98,87,97]
]    
print(details[0][0])
print(details[0][1])
print(details[1][0])

for i  in details:
    for j in i:
        print(j)







