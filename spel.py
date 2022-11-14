import time 
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
        return f"Du är {self.namn} nivå [{self.nivå}] av huset {self.hus} och har styrkan [{self.styrka}]"
#Gör så att man ser ett string när man printar Huvudperson istället för ett konstigt medelande

    def get_name(self, namn):
        self.namn = namn
#Tror att den här är helt onödig just nu, men kommer säkert användas senare. 

class Monster():
    def __init__(self,styrka):
        self.monster_HP = 100
        self.styrka = styrka

def item_styrka(Item):
    if Item == "Äpple":
        print("tom")

class Item ():
    def __init__(self):
        self.HP = 2
        self.styrka = item_styrka(Item)


namn = input("Skriv ditt namn --> ")

Huvudperson = Person(f"{namn}", 1, "Man", "Kungavakt")
monster1 = Monster(5)
Äpple = Item
Tårta = Item
Päron = Item
Monter = Item

def strid(Huvudperson, Monster):
    print("Striden pågår i full gång")
    if Huvudperson.styrka == Monster.styrka:
        Monster.monster_HP - Huvudperson.styrka
        Huvudperson.HP - Monster.styrka
        print("Det blev lika yänni")

    elif Huvudperson.styrka < Monster.styrka:
        Huvudperson.HP - Monster.styrka
        print('''
        
        aboooo, orka wallah, jag taggar
        
        Monstret vann
        
        ''')

    elif Huvudperson.styrka > Monster.styrka:
        Monster.monster_HP - Huvudperson.styrka
        print('''
        
        Asså grabben, du trodde du va något va? Exaxt yähnni stick härifrån!
        
        Spelaren vann

        ''')

    elif Huvudperson.ryggsäck == "Drakglas":
        Monster.monster_HP - Huvudperson.styrka
        print(''''
        
        Asså grabben, du trodde du va något va? Exaxt yähnni stick härifrån!
        
        Spelaren vann
        
        ''')

    return Huvudperson, Monster #bug: skriver inte ut korrekt Hp efter strid 


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
print(f'Ditt vapen heter nu {vapen_namn}')

print(f'Ditt vapen "{vapen_namn}" har styrkan {vapen_styrka}. \nDin totala styrka är {vapen_styrka + Huvudperson.styrka}\n')



platser = ["Highgarden", "Riverrun", "Eyrie", "Casterly Rock", "Sunspear", "Winterfell", "Kingslanding"] #möjliga platser att resa till. 

var_fällor = random.choice(platser)
var_drakglas = random.choice(platser)             
i = 0

while True:

    i = i + 1
    if i % 2 == 0:
        Huvudperson.nivå = Huvudperson.nivå + 1
        vilket_nivå = int(input(f'''
        Du har gått upp till nivå {Huvudperson.nivå}! Du kan nu välja mellan tre olika förmål att lägga till i din ryggsäck.

        1. Äpple 2. Tårta  3. Päron 
        
        -->
        '''))

        if vilket_nivå == 1:
            print("\nDu valde Äpple")
            Huvudperson.ryggsäck.append("Äpple")

        elif vilket_nivå == 2:
            print("\nDu valde Tårta")
            Huvudperson.ryggsäck.append("Tårta")

        elif vilket_nivå == 3:
            print("\nDu valde päron")
            Huvudperson.ryggsäck.append("Päron")

        else:
            print("Nivå boorgit")

    else:
        print("Nivå booorgir")
    
    var_monster = random.choice(platser)
    var_kista = random.choice(platser) #fyller ingen funktion just nu
    monster1.styrka = monster1.styrka + 1

    spelar_plats = "Kingslanding"
    print('------------------------------------\nOm du vill avbryta under spelets gång skriv "end"\nOm du vill se dina stats skriv "stats"\n')
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
            if monster1.monster_HP == 0 or "Drakglas" in Huvudperson.ryggsäck:
                print("Du van spelet, bra gjort!")
                break
            else:
                print("""
                
                -aboo...jävla monster orka wallah
                
                -du tror du är något va? Gahba nu ska vi se vad du går för yänni
                
                """)

                Huvudperson = strid(Huvudperson, monster1)
                if monster1.monster_HP == 0:
                    print('''
                    
                    Exakt yänni, ställ dig inte upp shomme.
                    
                    Spelaren vann spelet 

                    ''')
                    break
                else:
                    print(f"Efter stiden har du {Huvudperson.HP} HP och monstret har {monster1.monster_HP} HP")
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
    elif var_resa == "var":
        print(f"Du är vid {spelar_plats}")
    else:

        print("loppen borgir")

