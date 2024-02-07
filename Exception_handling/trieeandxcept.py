try:
    num1,num2=10,5
    print(num1/num2)

except Exception as e:
    print(e)
except:
    print("Some random error occured")
else:
    print("Progam ran successfully")
finally:
    print("Program Ended")


    