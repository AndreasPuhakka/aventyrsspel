import time 
import random
import colorama
from colorama import Back, Fore, Style

#-----------------------------------------------------------------------------

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

def xp(nivå,xp):
    if nivå == 1:
        xp == 100
        return xp
    elif nivå == 2:
        xp == 125
        return xp
    elif nivå == 3:
        xp == 150
        return xp
    elif nivå == 4:
        xp == 175
        return xp
    elif nivå == 5:
        xp == 200
        return xp
    elif nivå == 6:
        xp == 225
        return xp
    else:
        print("funktionen borrgirxp")

class Person():
    def __init__(self, namn, nivå, kön, roll):
        self.namn = namn
        self.nivå = nivå
        self.xp = 0
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

def nivå_check(Huvudperson,xp,xp_tot,nivå):
    if xp == xp(nivå,xp):
        Huvudperson.nivå =+ 1
        print(f"lvl up {Huvudperson.nivå}")
    else:
        print("fel")
    

class Monster():
    def __init__(self,styrka):
        self.HP = 100
        self.styrka = styrka

def item_styrka(Item):
    if Item == "Äpple":
        print("tom")

class Item_vapen ():
    def __init__(self, namn, styrka):
        self.namn = namn
        self.styrka = styrka

class Item_konsumerbart ():
    def __init__(self, namn, beskrivning, HP):
        self.namn = namn
        self.beskrivning = beskrivning
        self.HP = HP

Valyrianskt_svärd = Item_vapen("Valyrianskt svärd", 10)
bra_pilbåge = Item_vapen("Bra pilbåge", 7)
bra_yxa = Item_vapen("Bra yxa", 8)
yay_drakglas = Item_vapen("Drakglas", 0)


äpple = Item_konsumerbart("Äpple", "Ett vanligt äpple" , 10)
tårta = Item_konsumerbart("Tårta", "En vanlig tårta", 15)
monter = Item_konsumerbart("Monster Energidricka", "Tillverkades av ingen annan än Andreas av Huset Puhakka" , 30)

namn = input("Skriv ditt namn --> ")

Huvudperson = Person(f"{namn}", 1, "Man", "Kungavakt")
monster1 = Monster(5)

#-----------------------------------------------------------------------------

def strid(Huvudperson, Monster, vapen_styrka):
    print("Nu är det fajt")
    time.sleep(3)
    if Huvudperson.styrka == monster1.styrka:
        Huvudperson.HP = Huvudperson.HP - monster1.styrka
        monster1.HP = monster1.HP - Huvudperson.styrka - vapen_styrka
        print(f'''
        
        Det blev lika, båda tog lite skada

        HP efter strid:
        Monster: {monster1.HP}
        {namn}: {Huvudperson.HP}
        
        ''')

    elif Huvudperson.styrka > monster1.styrka:
        monster1.HP = monster1.HP - Huvudperson.styrka - vapen_styrka
        print(f'''
        
        {namn} av Huset {huset} vann striden

        HP efter strid:
        Monster: {monster1.HP}
        {namn}: {Huvudperson.HP}
        
        ''')

    elif Huvudperson.styrka < monster1.styrka:
        Huvudperson.HP = Huvudperson.HP - monster1.styrka
        print(f'''
        
        {namn} av Huset {huset} förlorade striden

        HP efter strid:
        Monster: {monster1.HP}
        {namn}: {Huvudperson.HP}
        
        ''')

    else:
        print("funktionen borrrgirtridit")
    time.sleep(3)
    
    return Huvudperson, Monster #bug: skriver inte ut korrekt Hp efter strid 

#-----------------------------------------------------------------------------

def visa_instruktioner():
    print('''
    
    (Game Of Thrones inspererat)

    Spelet går ut på att vinna
    Du kan vinna genom att antingen besegra monstret eller att nå nivå 10. 
    
    ''')
    return print

print(input(Fore.GREEN+f'''
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
print(f'Ditt vapen heter nu {vapen_namn}')

print(f'Ditt vapen "{vapen_namn}" har styrkan {vapen_styrka}. \nDin totala styrka är {vapen_styrka + Huvudperson.styrka}\n')

#-----------------------------------------------------------------------------

platser = ["Highgarden", "Riverrun", "Eyrie", "Casterly Rock", "Sunspear", "Winterfell", "Kingslanding"] #möjliga platser att resa till. 

var_fällor = random.choice(platser)
var_drakglas = random.choice(platser)             
i = 0

while True:
    
    var_monster = random.choice(platser)
    var_kista = random.choice(platser) #fyller ingen funktion just nu
    monster1.styrka = monster1.styrka + 1

    spelar_plats = "Kingslanding"
    print('------------------------------------\nOm du vill avbryta under spelets gång skriv "end"\nOm du vill se dina stats skriv "stats"\nOm du vill se instruktioner skriv "Instruktioner"')
    print('Möjliga destinationer: "Highgarden", "Riverrun", "Eyrie", "Casterly Rock", "Sunspear", "Winterfell", "Kingslanding"')
    var_resa = input("\nVart vill du resa? Du kan välja mellan alternativen ovan! \n-->")
   
    if var_resa in platser:  
        print(f'''
------------------------------------
Du väljer att resa till {var_resa}
            ()          
        c==//\         
   _-~~/-._|_|         
  /'_,/,   //'~~~\;;,  
  `~  _( _||_..\ | ';; 
    /'~|/ ~' `\<\>  ;  
    "  |      /  |     
       "      "  "    
------------------------------------''')    
        time.sleep(3)
        spelar_plats = var_resa
        print(f"Du har rest till {spelar_plats}\n")

        if spelar_plats == var_monster:
            if monster1.HP == 0 or "Drakglas" in Huvudperson.ryggsäck:
                print("Du van spelet, bra gjort!")
                break
            else:
                Huvudperson = strid(Huvudperson, monster1, vapen_styrka)
                if monster1.HP == 0:
                    print('''
                    
                    Exakt yänni, ställ dig inte upp shomme.
                    
                    Spelaren vann spelet 

                    ''')
                    break
                else:
                    continue
        elif spelar_plats == var_fällor:
            Huvudperson.HP = Huvudperson.HP - 25
            print(f"Du gick i en fälla. Du har nu {Huvudperson.HP}HP")

        elif spelar_plats == var_drakglas:
            print("Du hittade drakglas. Detta läggs i din ryggsäck")
            Huvudperson.ryggsäck.append("Drakglas")

        elif spelar_plats == var_kista:
            print("Du hittade en kista!\n")

        else:
            print("Det fanns inget här!\n")

    elif var_resa == spelar_plats:
        print("Du är redan på denna plats. Skriv något annat\n")
        continue

    elif var_resa == "end":
        print("Du har valt att avsluta programmet")
        break

    elif var_resa == "stats":
        print(f'''
        HP: {Huvudperson.HP}
        Styrka: {Huvudperson.styrka} av Huset {Huvudperson.hus}
        Nivå: {Huvudperson.nivå}
        Ryggsäck: {Huvudperson.ryggsäck} - {vapen_namn} , Vapensstyrka: {vapen_styrka}
        Totalsyrka: {vapen_styrka + Huvudperson.styrka}
        ''')
        time.sleep(6)

    elif var_resa == "Instruktioner":
        visa_instruktioner()
    elif var_resa == "var":
        print(f"Du är vid {spelar_plats}")
    else:

        print("loppen borgir")

#-----------------------------------------------------------------------------