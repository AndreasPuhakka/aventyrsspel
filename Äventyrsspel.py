import random

def monst(monster):
    monster_styrka = random.randint(1,15)
    
    return monster_styrka

def strid(tot_styrka, monster_styrka, HP, monster_hp):
    print("Whalla bre, du måste strida!")
    if tot_styrka == monster_styrka:
        monster_hp - tot_styrka
        HP - monster_styrka
        print("Det blev lika yänni")
    elif tot_styrka < monster_styrka:
        Huvudperson.HP - monster_styrka
    elif tot_styrka > monster_styrka:
        monster_hp - monster_hp


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
        return f"Du är {self.namn} nivå [{self.nivå}] av huset {self.hus} och har styrkan [{self.styrka}]"
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
#Loopar valet av vapen om man gör fel
    vilket_vapen = input(f'''- "Du din lilla shomme kan välja mellan olika försvarsmedel att ha med dig på gatan:"

       1. Pilpåge  2. Yxa  3. Svärd

---->>>  ''')

    if vilket_vapen == "1":
        print('''
        
Du valde vapnet Pilbåge.
''')
        vilket_vapen = "Pilbåge"
        Huvudperson.ryggsäck.append("Pilbåge")
        print(f'''Din Ryggsäck:
    {Huvudperson.ryggsäck}''')
        vapen_styrka = 4
        break
    
    elif vilket_vapen == "2":
        print('''
    
Du valde vapnet Yxa.
''')
        vilket_vapen = "Yxa"
        Huvudperson.ryggsäck.append("Yxa")
        print(f'''Din Ryggsäck:
{Huvudperson.ryggsäck}''')
        vapen_styrka = 6
        break

    elif vilket_vapen == "3":
        print('''
        
Du valde vapnet Svärd.
''')
        vilket_vapen = "Svärd"
        Huvudperson.ryggsäck.append("Svärd")
        print(f'''Din Ryggsäck:
{Huvudperson.ryggsäck}''')
        vapen_styrka = 4
        break
    else:
        print(input('''
        
Du måste välja mellan 1, 2 eller 3.
[ENTER]'''))
    print('''












''')
    #Igen en printsats med tomma paragrafer för att när den loopar om igen ska det inte vara massa onödig text i terminalen.
    continue

vapen_namn = input(f"Du kan välja ett namn för ditt {vilket_vapen} \n")
print(f'''Ditt vapen heter nu {vapen_namn}! 
--->>> ''')
print(f"Ditt vapen heter nu {vapen_namn}")

print(f'Ditt vapen "{vapen_namn}" har styrkan {vapen_styrka}. \nDin totala styrka är "????"\n')


while True:
    
    Locations = ["Highgarden", "Riverrun", "Eyrie", "Casterly Rock", "Sunspear", "Winterfell"]
    var_monster = "Highgarden"
    var_drakglas = random.choice(Locations)
    var_kista = random.choice (Locations)

    print("Du är just nu i kungens landning och har ett stort val framför dig. Du måste hitta drak glaset, det enda materialet som kan ta död på en white walker...") #fortsätt skriva
    val_vilket_kungarike = input("Du kan välja att resa mellan de tre närmaste olika kungariken. \n Från kungens landning kan du välja att resa mellan: \n\n Highgarden (Huset Tyrell), Riverrun (Huset Tully), Eyrie (Huset Arryn) \n\n Gör ditt val här --> ")
    if val_vilket_kungarike == "Highgarden":
        print("Du reser mot Highgarden!")
        if "Highgarden" == var_drakglas:
            print("Du hittade drakglas! \n Detta läggs i din ryggsäck")
            Huvudperson.ryggsäck.append("drakglas")
            break
        elif "Highgarden" == var_monster:
            print("Du hittade ett monster vid Highgarden! Du måste strida!")
            strid(2,3,4,1)
            break
        elif "Highgarden" == var_kista:
            val_i_kista = input("Du hittade en kista med ett svärd av valyrienskt stål! \n Tryck 1 om du vill läga till den i din ryggsäck")
            if val_i_kista == "1":
                Huvudperson.ryggsäck.append("Svärd av valyrienskt stål")
                break
            else:
                print("Du går vidare")
                break

    elif val_vilket_kungarike == "Riverrun":
        print("Du reser mot Riverrun")
        break
    elif val_vilket_kungarike == "Eyrie":
        print("Du reser mot Riverrun")
        break
    else:
        print("Du gjorde något fel")
        continue

