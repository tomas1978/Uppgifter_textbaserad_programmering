#Programmet översätter en inmatad textsträng till rövarspråket

text=input("Skriv en textsträng att översätta: ")
vokaler=['a','A','o','O','u','U','å','Å','e','i','I','E','y','Y','ä','Ä','ö','Ö']
rövartext=[]

for i in range(0,len(text)):
    if text[i] not in vokaler:
        temp=text[i]
        temp+='o'
        temp+=text[i]
        rövartext+=temp
    else:
        rövartext+=text[i]
        
rövarsträng=''.join(rövartext)
print("Texten på rövarspråket: ",rövarsträng)
    
