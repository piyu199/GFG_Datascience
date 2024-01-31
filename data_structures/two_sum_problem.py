def two_sum_tuple(num,target):
    num_indices={}

    for i, element in enumerate(num):
        complement=target-element

        if complement in num_indices:
            return (complement,element)

        num_indices[num]=i


if __name__=="__main__":
    num=[2,7,11,15]
    target=9
    result=two_sum_tuple(num,target)
    print("Tuple of elements are: ",result)