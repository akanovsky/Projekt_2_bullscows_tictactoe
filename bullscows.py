import random
import time
ODDELOVAC = "-" * 30

# tisk uvodniho textu
def pozdraveni():
    print("Hi there!")
    print(ODDELOVAC)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(ODDELOVAC)

# zadani a kontrola cisla
def zadani_cisla():
    not_ok = True
    bez_duplicit = False
    while not_ok:
        vstup = input("Enter a number: ")
        for i in vstup:   #kontrola duplicit v zadani
            if i in vstup[vstup.index(i)+1:len(vstup)]:
                print("There is duplicity in the input !")
                bez_duplicit = False
                break
            else:
                bez_duplicit = True
        if len(vstup) != 4: #kontrola poctu cisel
             print ("Enter 4 digits !")
        elif vstup[0] == "0": #kontrola nuly na zacatku
             print ("First number has to be higher than 0.")
        elif vstup.isnumeric() and bez_duplicit:
             # vstup = int(vstup)
             not_ok = False
    vstup_init = vstup
    vstup = [int(i) for i in vstup] #prevod cisla na list
    return vstup,vstup_init

# generovani nahodneho cisla

def generuj():
    pole = [0,1,2,3,4,5,6,7,8,9]
    g_cislo = []
    for i in range(0,4):
        if i == 0: # 0 nesmi byt na zacatku
            x = random.randint(1, len(pole)-1)
        else :
            x = random.randint(0,len(pole)-1)
        g_cislo.append(pole[x])
        pole.remove(pole[x])

    return g_cislo


# vyhodnoceni spravnosti tipu
def vyhodnot_shodu(g_cislo,z_cislo,pokus):
    bulls,cows = 0,0
    b_text = "bull"
    c_text = "cow"
    if pokus == 1:
        g_text = "guess"
    else:
        g_text = "guesses"
    for i in range(0,4): #srovnani jednotlivych prvku obou cisel
        if z_cislo[i] in g_cislo:
            if z_cislo[i] == g_cislo[i]:
                bulls += 1
                if bulls > 1:
                    b_text = "bulls"
            else:
                cows += 1
                if cows > 1:
                    c_text = "cows"

    if bulls == 4: #vyhodnoceni vyjimecnosti rychlosti uhadnuti
        print(f"Correct, you've guessed the right number in {pokus} {g_text} !")
        if pokus < 5:
            print("That's amazing.")
        elif pokus < 10:
            print("That's average.")
        else:
            print("That's not so good.")
        return False
    else:
        print(f"{bulls} {b_text}, {cows} {c_text}")
        return True



# ulozeni statistiky do souboru
def vysledky(generovane_cislo,pokus,herni_cas):

    def uloz_stav(g_cislo, pokus, h_cas): #ulozeni statistiky do souboru
        with open("bullscows_stat.txt", "a+") as f:
            zapis = "Number :" + str(g_cislo) + ", rounds :" + str(pokus) + ", game time :" + str(h_cas) + " s"+"\n"
            # print(zapis)
            f.write(zapis)

    print(ODDELOVAC) #finalni statistika
    print("Game statistic :")
    print(f"Time of game : {herni_cas} s")
    uloz_stav(generovane_cislo, pokus, herni_cas)
    print(ODDELOVAC)
    print("End of game.")

# hlavni smycka hry
def main():
    pokus = 0
    game_on = True
    start = time.time()
    pozdraveni()
    generovane_cislo = generuj()
    #print(generovane_cislo)
    while game_on:
        pokus +=1
        zadane_cislo,vstup = zadani_cisla()
        game_on = vyhodnot_shodu(generovane_cislo,zadane_cislo,pokus)
    konec = time.time()
    herni_cas = round(konec - start,1)
    vysledky(vstup,pokus,herni_cas)



main()
