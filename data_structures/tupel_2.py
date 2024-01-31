'''
Input:
numbers = ( 1 ,5, 9, 13, 17 )
Output: 
1 5 9 13 17 21 25 29
Explanation: It's an increasing sequence by 4. So, the next three numbers are 17+4= 21,  21+4=25, 25+4=29.
'''
def sequence(numbers):
    diff=numbers[1]-numbers[0]
    num=numbers[0]
    out=[]
    for i in range(len(numbers)+3):
        num += diff
        out.append(num)
    return tuple(out) 

if __name__=="__main__":
    numbers = ( 1 ,5, 9, 13, 17 ) 
    sequence(numbers)
