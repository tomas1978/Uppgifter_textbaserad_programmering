#Datorn väljer ett slumptal mellan 1 och 100 och spelaren ska gissa talet.
#Datorn ska för varje gissning tala om ifall talet är högre eller lägre.
#Om spelaren gissar rätt skriver datorn ut antal gissningar som behövdes.

import random

slumptal=random.randint(1,101)
gissning=-1
antal_gissningar=0

while(gissning!=slumptal):
    antal_gissningar+=1
    gissning=int(input("Skriv din gissning: "))
    if slumptal>gissning:
        print("Slumptalet är högre")
    elif slumptal<gissning:
        print("Slumptalet är lägre")
    else:
        print("Bra! Du gissade rätt!")
        print("Antal gissningar",antal_gissningar)