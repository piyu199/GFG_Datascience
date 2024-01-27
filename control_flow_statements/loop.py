#what is the probability of getting any individual number when 2 dice are rolled

for n in range(1,13):
    number=0
    for i in range(1,7):
        for j in range(1,7):
            if i+j == n:
                number += 1
    print((number/36)*100)


#what is the probability of getting any individual number when 3 dice are rolled
possible_sum=3*6 #it means we can have numbers between 1 to 18, on adding 3 dice i.e 6+6+6=18,4+5+6=15
for n in range(1,possible_sum+1):
    number = 0
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                if i + j + k==n:
                    number+=1
    print(f"{n}={round((number/216)*100,2)}")