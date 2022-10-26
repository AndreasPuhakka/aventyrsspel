import random

list_Huset = ["Baratheon", "Stark", "Lannister", "Tyrell", "Martell", "Tully", "Arryn", "Targaryen"]     #Vilken familj (kungarike) du föds in i väljs här!

huset = random.choice(list_Huset)  
#Väljer hus av listan list_Huset

def välj_styrka(huset):
    if huset == "Baratheon" or huset == "Stark":
        styrka = random.randint(7,10)
    elif huset == "Lannister" or huset == "Tyrell" or huset == "Martell":
        styrka = random.randint(4,7)
    elif huset == "Tully" or huset == "Arryn":
        styrka = random.randint(1,4)
    else:
        styrka = 11
    return styrka
    #Väljer din styrka beroende på ditt hus

class Person():
    def __init__(self, namn, nivå, kön, roll):
        self.namn = namn
        self.nivå = nivå
        self.kön = kön 
        self.roll = roll
        self.HP = 100
        self.hus = huset
        self.styrka = välj_styrka(self.hus)
        self.ryggsäck = []
#Håller alla stats för personen som spelar

    def __str__(self):
        return f"Du är {self.namn} av huset {self.hus} och har styrkan [{self.styrka}]"
#Gör så att man ser ett string när man printar Huvudperson istället för ett konstigt medelande

    def get_name(self, namn):
        self.namn = namn
#Tror att den här är helt onödig just nu, men kommer säkert användas senare. 


Huvudperson = Person("Andreas", 1, "Man", "Kungavakt")
 



print(input(f'''


















{Huvudperson}
Klicka [ENTER] för att forstätta'''))

print(input('''
















Du har anlänt till kungens landning för att få ett viktigt uppdrag av kung Tommen Baratheon.
[ENTER]'''))

print(input('''














    
- "Whallah yhanni nu ska du på uppdrag!", Tommen
'''))
#Printsatser med flera tomma paragrafer för att det ser snyggare ut i terminalen :)

print(input('''- "Tjo bre, jag fixar whalla", 
'''))

while True:
#Loopar valet av vapen
    vilket_vapen = input(f'''- "Du din lilla shomme kan välja mellan olika försvarsmedel att ha med dig på gatan:"

       1. Pilpåge  2. Yxa  3. Svärd

---->>>  ''')

    if vilket_vapen == "1":
        print('''
        
Du valde vapnet Pilbåge.
''')
        Huvudperson.ryggsäck.append("Pilbåge")
        print(f'''Din Ryggsäck:
{Huvudperson.ryggsäck}''')
        break
    elif vilket_vapen == "2":
        print('''
        
Du valde vapnet Yxa.
''')
        Huvudperson.ryggsäck.append("Yxa")
        print(f'''Din Ryggsäck:
{Huvudperson.ryggsäck}''')
        break
    elif vilket_vapen == "3":
        print('''
        
Du valde vapnet Svärd.
''')
        Huvudperson.ryggsäck.append("Svärd")
        print(f'''Din Ryggsäck:
{Huvudperson.ryggsäck}''')
        break
    else:
        print(input('''
        
Du måste välja mellan 1, 2 eller 3.
[ENTER]'''))
    print('''












''')
    #Igen en printsats med tomma paragrafer för att när den loopar om igen ska det inte vara massa onödig text i terminalen.
    continue