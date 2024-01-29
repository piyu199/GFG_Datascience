def prime_number(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True


def prime_in_range(start_range,end_range):
    return [num for num in range(start_range,end_range+1) if prime_number(num)]

if __name__=="__main__":
    start_range=int(input("Enter the start range :"))
    end_range=int(input("Enter the end range :"))   
    result=prime_in_range(start_range,end_range)
    print(result)