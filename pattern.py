x = 1


for i in range(1,6) :
    for j in range(1,6) :
        x += 1
        if x%2==0:
            print(1, end='')
        else :
            print(0, end='')
        
    print()