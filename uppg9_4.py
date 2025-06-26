#Programmet skriver ut multiplikationstabellen upp till 11 för
#en multiplikator som anges av användaren. Multiplikatorn är
#i detta program ett flyttal.
def multiplikationstabell(multiplikator):
    for i in range(1, 11):
        print(f"{multiplikator} * {i} = {multiplikator * i}")

mult=float(input("Ange multiplikator:"))              
multiplikationstabell(mult)
