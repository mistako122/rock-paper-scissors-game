import random

cilvēka_izvēle = input("Tava izvēle? ")
iesējamās_izvēles = ["akmens" , "šķēres" , "papīrs"]
datora_izvēle = random.choice (iesējamās_izvēles)

if cilvēka_izvēle == datora_izvēle :
    print("Neizšķirts")
elif cilvēka_izvēle  == "akmens" and  datora_izvēle == 'šķēres' :
    print("Cilvēks uzvar")
elif cilvēka_izvēle == "šķēres" and  datora_izvēle == 'papīrs' :
    print("Cilvēks uzvar")
elif cilvēka_izvēle == "papīrs" and datora_izvēle == "akmens" :
    print("Cilvēks uzvar")  
else: 
    print("Cilvēks zaudē")    
