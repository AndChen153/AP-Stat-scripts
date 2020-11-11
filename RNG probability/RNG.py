import random

def gen(trials):
    j = addictedlessthan40 = addictedmorethan40 = 0
    while j<trials:
        ones = twos = 0
        for i in range (0,100):
            x=random.randint(1,2)
            #print (x)
            if x==1:
                ones += 1
            else:
                twos += 1
        #print(ones, twos)
        if ones<=40:
            addictedlessthan40 += 1
        else:
            addictedmorethan40 += 1
        j += 1
    
    return (addictedlessthan40, addictedmorethan40)

print(gen(100000))