#Programmet kontrollerar med hjälp av en funktion om en punkt med
#koordinatern (x,y) befinner sig innanför eller utanför en cirkel
#som har centrumpunkt (xc, yc) och radien rc



#Kontrollera om (x,y) befinner sig inom cirkeln med
#ekvation (x-xc)^2+(y-yc)^2=rc^2
def insideCircle(x, y, xc, yc, rc):
    xkatet=abs(x-xc)
    ykatet=abs(y-yc)
    distance=(xkatet**2+ykatet**2)**0.5
    return distance<=rc



#Kontroll
resultat1=insideCircle(5,8,1,2,2)
print(resultat1)

resultat2=insideCircle(1,2,-1,-3,19)
print(resultat2)

    
