def divide_number(a,b):
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide my zero")
        return a/b
    except Exception as e:
        print(f"An error ocurred,{e}")
        raise ValueError("Custom error message") from e

try:
    result=divide_number(10,0)
    print(result)
except ValueError as ve:
    print(f"Caught a ValueError: {ve}")
except ZeroDivisionError as zde:
    print(f"Caught a ZeroDivisionError: {zde}")


#Assert
try:
    name="Ra"
    assert len(name)>=3,"Name should be atleast 3 charactr long"
except Exception as e:
    print(e)