class mathematics:
    def factorial(self,num):
        if num==0 or num==1:
            return 1
        else:
            return num * self.factorial(num-1)

    def lst_multiplication(self,lst):
        s=1
        for i in lst:
            s *= i
        return s
    
    def lst_dot(self,lst_1,lst_2):
        return [lst_1[i]*lst_2[i] for i in range(len(lst_1))]

            
m1=mathematics()
print(m1.factorial(5))
print("-"*30)
print(m1.lst_multiplication())
print("-"*30)