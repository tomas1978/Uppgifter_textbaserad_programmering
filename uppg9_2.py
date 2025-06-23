#Programmet fyller en given lista med slumptal mellan 1 och 99
#och sorterar därefter listan.
#Några while-loopar utbytta mot for-loopar jämfört med uppg9_1.py

import random

listan = [12,34,9,11,14,5,6]

avg=0
count=0
total=0
temp=0

for i in range(0,len(listan)):
    count+=1 
    listan[i]=random.randint(1,100)
    total+=listan[i]
 
avg=total/count

#i=0

for _ in range(len(listan)):
    for i in range(0,len(listan)-1):
        if listan[i]>listan[i+1]:
            temp=listan[i+1]
            listan[i+1]=listan[i]
            listan[i]=temp

print(listan)
