#Zip

lst_1=["Prajesh","Aditya","Adnana","Abhirup"]
lst_2=[25,23,24,30]
print(list(zip(lst_1,lst_2)))
print("-"*30)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print([list(row) for row in zip(matrix)])
print([list(row) for row in zip(*matrix)])
print([list(row) for  row in zip(*[list(row) for row in zip(*matrix)])])
print("-"*30)

lst3=[2,4,5]
lst4=[1,3,5]

print(sum([i*j for i,j in zip(lst3,lst4)]))

#Filter
lst=[1,2,3,6,40,10,55,22]

def is_even(n):
    return n%2==0 

print(list(filter(is_even,lst)))


#Lambda
add_num=lambda x,y:x+y
print(add_num(4,5))

num=[20,30,55,77,84,59]
print(list(filter(lambda x:x%2==0,num)))
print("-"*30)

#map
names=["Prajesh","Arvind","Waghela"]
print(list(map(lambda x : len(x),names)))
print("-"*30)



is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
print(is_even_list)
for item in is_even_list:
	print(item(), end = ' ')
      
print()

#Combining all functions
names=["Geeks","for","Geeks"]
scores=[30,35,40]
filtered_name=list(filter(lambda x:len(x)>4,names))
uppercase_names=list(map(lambda x:x.upper(),filtered_name))

zipped_data=list(zip(uppercase_names,scores))
print(zipped_data)



