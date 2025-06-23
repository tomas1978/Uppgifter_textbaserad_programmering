#Programmet fyller en given lista med slumptal mellan 1 och 99
#och sorterar därefter listan.
import random

listan = [12,34,9,11,14,5,6]

avg=0
count=0
i=0
total=0
temp=0

while i!=len(listan):
    count+=1 
    listan[i]=random.randint(1,100)
    total+=listan[i]
    i+=1

avg=total/count

i=0

for _ in range(len(listan)):
    while i <len(listan)-1:
        if listan[i]>listan[i+1]:
            temp=listan[i+1]
            listan[i+1]=listan[i]
            listan[i]=temp
        i+=1
    i=0

print(listan)
