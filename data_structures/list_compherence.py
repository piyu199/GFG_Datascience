lst=[1,2,3,4,5,6]
sqaure=[i**2 for i in  lst ]
print(lst)
print(sqaure)

#list comprehension using multidimensional list
test=[[j for j in range(2)] for i in range(3)]
print(test)

#Accessing all the elements of the list
lst1=[[1,2,3],[4,5,6],[7,8,9]]
print([j for i in lst1 for j in i ])
