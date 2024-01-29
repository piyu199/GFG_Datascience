dct={1:"Prajesh",2:"Adnan",3:"Mozzam",4:"Abhirup"}
print(dct)
print(dct.get(1))
print(dct[3])
del dct[3]
print(dct)
dct.clear()
print(dct)
print('-'*20)
#check if the key is present
dct={1:"Prajesh",2:"Adnan",3:"Mozzam",4:"Abhirup"}
print(2 in dct)
print('-'*20)

#Dct updating the dictionaries
dct2={5:"Shrikant",6:"Milind",7:"Anil",8:"Swapnil"}
dct.update(dct2)
print(dct)
print('-'*20)


#Multidimensional Dictionaries
dict11={1:{"name":"Prajesh","goal":"To be the best"},
        2:{"name":"Kolhi","goal":"To win the match"}}

print(dict11)
print("length of dictinary : ",len(dict11))
print(dict11[1]["name"])



#Iterate through Multidimensional Dictionary
print('-'*20)
data={
    1:{"name":"Prajesh","phone":483513,"marks":{"hin":40,"mar":45,"eng":50}},
    2:{"name":"Dhariya","phone":235153,"marks":{"hin":30,"mar":35,"eng":30}},
    3:{"name":"Chetan","phone":835215,"marks":{"hin":40,"mar":43,"eng":34}},
    4:{"name":"Yash","phone":844325,"marks":{"hin":38,"mar":84,"eng":60}}
}

print(data)
print('-'*20)
for i in data.keys():
    print(i,data[i]['name'],data[i]["marks"]["hin"])













