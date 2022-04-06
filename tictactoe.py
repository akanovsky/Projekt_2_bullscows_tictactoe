ODDELOVAC = "=" * 50
DELIC_PLOCHA = ("+---+---+---+")
plocha = [[0,0,0],[0,0,0],[0,0,0]]
mozne_tahy =[1,2,3,4,5,6,7,8,9]

def win(game):  #algoritmus vyhodnoceni, prevzato z  https://pythonprogramming.net/horizontal-winner-learn-python-3-tutorials/

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontal
    for row in game:
        # print(row)
        if all_same(row):
            # print(f"Player {row[0]} is the winner horizontally!")
            return True

    # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            # print(f"Player {check[0]} is the winner vertically!")
            return True

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if all_same(diags):
        # print(f"Player {diags[0]} has won Diagonally (/)")
        return True

    # \ diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if all_same(diags):
        # print(f"Player {diags[0]} has won Diagonally (\\)")
        return True

    return False

def tisk_uvod():  #tisk uvodnich informaci
    print("Welcome to Tic Tac Toe")
    print(ODDELOVAC)
    print("""GAME RULES:
  Each player can place one mark (or stone)
  per turn on the 3x3 grid. The WINNER is
  who succeeds in placing three of their
  marks in a:
  * horizontal,
  * vertical or
  * diagonal row
  """)
    print(ODDELOVAC)
    print("Let's start the game")
    print("-" * 50)


def tisk_plocha(): #vizualizace herni plochy
    for i in range(0,3):
        print(DELIC_PLOCHA)
        radek = "|"
        for j in range(0,3):
            if plocha[i][j] == 0:
                radek += " - "
            elif plocha[i][j] == 1:
                radek +=" o "
            elif plocha[i][j] == 2:
                radek +=" x "
            radek += "|"
        print(radek)
    print(DELIC_PLOCHA)

def zadej_tah(hrac): #zadani tahu a vyhodnoceni spravnosti zadani
    status = True

    while status:
        print(ODDELOVAC)
        tah = input(f"Player {hrac} | Please enter your move number : ")

        if tah.isnumeric() and int(tah) in mozne_tahy:
            tah = int(tah)
            mozne_tahy.remove(int(tah))
            status = False
        elif tah.isnumeric() and int(tah) not in mozne_tahy and int(tah) in range(1,10):
            print("Field is already taken. Try it again !")
        else:
            print("Wrong input ! Try it once again.")

    print(ODDELOVAC)
    return tah



def zaznam_tahu(hrac,tah): #zaznamenani tahu do herni plochy
    tah -=1
    i = int(tah / 3)
    j = tah % 3
    if hrac == "o":
        plocha[i][j] = 1
    elif hrac == "x":
        plocha[i][j] = 2


def main(): #hlavni funkce pro beh hry
    tisk_uvod()
    tisk_plocha()
    game_on = True
    pocet_tahu = 0
    hrac = "o"
    while game_on:
        tah = zadej_tah(hrac)
        pocet_tahu += 1
        zaznam_tahu(hrac,tah)
        tisk_plocha()
        if win(plocha):
            print(ODDELOVAC)
            print(f"Congratulations, the player {hrac} WON !")
            print(ODDELOVAC)
            game_on = False
        elif pocet_tahu == 9 :
            print(ODDELOVAC)
            print(f"End of game. No winner :-(")
            print(ODDELOVAC)
            game_on = False
        if hrac == "o":
            hrac = "x"
        else:
            hrac = "o"


main()

