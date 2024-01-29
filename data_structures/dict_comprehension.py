dct={i:i**3 for i in range(1,11)}
print(dct)
print("-"*20)
dct1={i:i**3 for i in range(1,11) if i%2==0}
print(dct1)

lst=["Apple","Mange","Banana","Grapes"]
dict1={item:len(item) for item in lst}
print(lst)
print(dict1)

#special keys with strings
dctzzz={'num_'+str(i):i for i in range(1,11)}
print(dctzzz)
print('-'*30)

dctzzz={'num_'+str(i):i for i in range(1,11) if i%2==0}
print(dctzzz)

matrix=[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
# final_dct={(i,j):matrix[i][j] for i in range(4) for j in range(3)}
#or
final_dct={(i,j):matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))}
print(final_dct)