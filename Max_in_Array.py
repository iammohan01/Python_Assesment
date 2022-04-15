from asyncio.windows_events import NULL
import random as r
exArray = []
max = 0 
min = 9999999999
for i in range(0,r.randint(0,450)) :
    exArray.append(r.randint(0,20000))

for i in exArray :
    if  i > max :
        max = i 
    if i < min  :
        min = i

####

#print(exArray)
print('Minimum Number in Array : ' + str(min))
print('Maximum Number in Array : ' + str(max))