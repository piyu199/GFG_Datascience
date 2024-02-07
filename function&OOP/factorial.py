def factorial(n):
    try:
        if n==0 or n==1:
            return 1
        else:
            return n * factorial(n-1)
    except Exception as e:
        print(e)
if __name__=="__main__":
    result=factorial(5)
    print(result)