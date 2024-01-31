lst=[1,2,3,4,5]

def sqr(lst):
    return [i**2 for i in lst]

def cub(lst):
    return [i**3 for i in lst]


def final(lst):
    lst_1=sqr(lst)
    lst_2=cub(lst)
    return [lst_1[i]+lst_2[i] for i in range(len(lst_1))]

print(final(lst))