import random
import os

clear = lambda: os.system("cls")


Pics = ['''

  +---+
  |   |
      |
      |
      |
      |''', '''

  +---+
  |   |
  O   |
      |
      |
      |''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |''','''

  +---+
  |   |
      | Thanks for saving me!
  O   |
 /|\  |
 / \  |''','''

  +---+
  |   |
  O   | You failed to save stickman!
 /|\  |
 / \  |
      |''', '''
 _   _    _    _   _  ____ __  __    _    _   _ 
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_| by 0li
                                                 ''','''
  ____  _   _  ___  ____  
 / ___|| | | |/ _ \|  _ \ 
 \___ \| |_| | | | | |_) |
  ___) |  _  | |_| |  __/ 
 |____/|_| |_|\___/|_|    
                             ''',''' 
 __     _____ ____ _____ ___  ______   __
 \ \   / /_ _/ ___|_   _/ _ \|  _ \ \ / /
  \ \ / / | | |     | || | | | |_) \ V / 
   \ V /  | | |___  | || |_| |  _ < | |  
    \_/  |___\____| |_| \___/|_| \_\|_|  
                                         ''',''' 
  ____  _____ _____ _____    _  _____ 
 |  _ \| ____|  ___| ____|  / \|_   _|
 | | | |  _| | |_  |  _|   / _ \ | |  
 | |_| | |___|  _| | |___ / ___ \| |  
 |____/|_____|_|   |_____/_/   \_\_|  
                                      ''']

words = [
    "Haus", "Baum", "Hund", "Katze", "Auto", "Buch", "Stuhl", "Tisch", "Blume", "Vogel", "Berg", "Fluss", "Wolke", "Schule", "Fenster", "Brot", "Schlüssel", "Lampe", "Schuh", "Mensch", "Computer", "Garten", "Zug", "Flugzeug", "Fahrrad", "Koffer", "Bett", "Wald", "See", "Lampe"]

eng_words = [
     "House", "Tree", "Dog", "Cat", "Car", "Book", "Chair", "Table", "Flower", "Bird", "Mountain", "River", "Cloud", "School", "Window", "Bread", "Key", "Lamp", "Shoe", "Human", "Computer", "Garden", "Train", "Airplane", "Bicycle", "Suitcase", "Bed", "Forest", "Lake", "Lamp"]

def word_generator():
    global lingu

    selected_word = random.choice(lingu)
    selected_word = selected_word.upper()
    return selected_word

def input_verify(tries):

    global already_guessed, abspacing, falseG, falseW, hints, not_guessed

    clear()

    if falseG == "true":
        print(falseW)
        falseW = ""
        falseG = "false"
    print(Pics[tries])
    print("".join(abspacing))
    print("Word: ", " ".join(word_display))
    print("Letters guessed: ", " | ".join(already_guessed))
    i = input("\nGuess letter: ").upper().replace(" ", "")

    if len(i) == 1 and i.isalpha():

        if i in already_guessed:
            falseG = "true"
            falseW = 'You already guessed ' + i
            return tries

        elif i in selected_word:
            print(Pics[tries])
            print("".join(abspacing))
            print(i , "was right!:D\n")
            already_guessed.append(i)
            not_guessed.remove(i)
            print("After removing: ", not_guessed)
            abspacing.append("====")
            for position, letter in enumerate(selected_word):
                    if letter == i:
                        word_display[position] = i 
            return tries

        else:
            tries = tries + 1
            print("\nSädly ", i ," wasn't in the word \n")
            already_guessed.append(i)
            abspacing.append("====")
            return tries
        
    elif i == "HINT":
    
        if hints > 0:
            i = random.choice(not_guessed)
            for position, letter in enumerate(selected_word):
                    if letter == i:
                        word_display[position] = i 
            not_guessed.remove(i)
            already_guessed.append(i)
            hints = hints - 1
            return tries
        else:
            falseG = "true"
            falseW = "Not enough hints"
            return tries

    else:
        falseG = "true"
        falseW = "Invalid Input"
        return tries

def main_game():

    global selected_word, tries, word_display, already_guessed, abspacing, hints, wasShop, wincoins, took_coin, falseW, falseG


    if "_" not in word_display:
        clear()
        if falseG == "true":
            print(falseW)
        falseW = ""
        falseG = "false"
        print(Pics[11])
        print(Pics[7])
        print("".join(abspacing))
        if took_coin == "no":
            wincoins = wincoins + 1
            took_coin = "yes"
        print("The Word is:", ''.join(selected_word))
        print("\nYou have earned yourself a win-coin!")
        if wasShop == "yes":
            ask = "no"
            wasShop = "no"
        else:
            ask = "yes"

        while ask == "yes":
            again = str(input("Do you want to play again? Yes/No/Shop ")).lower().replace(" ", "")

            if again == "yes":
                restarter()
                wasShop = "yes"
                ask = "no"

            elif again == "shop":
                clear()
                itemshop()
                wasShop = "yes"
                main_game()

            elif again == "cyrillstinkt":
                hints = 99999999
                itemshop()
                main_game()
                ask = "no"

            elif again == "no":
                print("Thanks for playing :D")
                exit()

            else:
                falseG = "true"
                falseW = "Invalid Input"
                main_game()

    elif tries == 6:
        clear()
        if falseG == "true":
            print(falseW)
        falseW = ""
        falseG = "false"
        print(Pics[12])
        print(Pics[8])
        print("".join(abspacing))
        print("The Word was:", ''.join(selected_word))
        if wasShop == "yes":
            ask = "no"
            wasShop = "no"
        else:
            ask = "yes"

        while ask == "yes":
            again = str(input("Do you want to play again? Yes/No/Shop ")).lower().replace(" ", "")

            if again == "yes":
                restarter()
                wasShop = "yes"
                ask = "no"

            elif again == "shop":
                clear()
                itemshop()
                wasShop = "yes"
                main_game()

            elif again == "cyrillstinkt":
                hints = 99999999
                itemshop()
                main_game()
                ask = "no"

            elif again == "no":
                print("Thanks for playing :D")
                exit()

            else:
                falseG = "true"
                falseW = "Invalid Input"
                main_game()

    else:
        tries = input_verify(tries)

def restarter():
    global selected_word, tries, word_display, already_guessed, abspacing, again, ask, not_guessed, took_coin

    selected_word = word_generator()
    tries = 0
    word_display = ["_"] * len(selected_word)
    already_guessed = []
    not_guessed = []
    abspacing = ["="] * len(selected_word)
    abspacing.append("===")
    again = ""
    ask = "no"
    took_coin = "no"
    not_guessed = [*selected_word]
    print("New word has been generated")

def language():
    global lingu 

    while True:
        lingu = input("In which langauge should the words be in? de/eng ").lower().replace(" ", "")

        if lingu == "eng":
            lingu = eng_words
            break

        elif lingu == "de":
            lingu = words
            break
        
        else:
            print("Invalid Input")

def itemshop():
    global hints, add, wincoins
    add = 0

    clear()
    print(Pics[10])

    print("You own", hints , "hints and", wincoins, "win-coins")
    print("For every round you win, you earn one win-coin, that you can trade in for hints (1 win-coin = 2 hints)\n")
    add = input("How many coins do you want to trade in? ")
    
    if add.isnumeric() == True and wincoins >= int(add):
        hints = hints + (2 * int(add))
        wincoins = wincoins - int(add)
        print("\nSucessfull")

    else:
        print("Invalid Input")
        add = 0

def starter():
    global wasShop, abspacing, falseG, falseW, lingu, hints, selected_word, tries, word_display, already_guessed, not_guessed, abspacing, wincoins, took_coin
   
    clear()
    wincoins = 0
    wasShop = "no"
    abspacing = []
    falseG = "false"
    falseW = ""
    print(Pics[9])
    lingu = ""
    hints = 0
    language()
    selected_word = word_generator()
    tries = 0
    word_display = ["_"] * len(selected_word)
    already_guessed = []
    not_guessed = []
    abspacing = ["==="] * len(selected_word)
    abspacing.append("=====")
    not_guessed = [*selected_word]
    ask = ""
    took_coin = "no"

    while ask == "":
        again = str(input("Do you want to enter the shop? yes/no ")).lower().replace(" ", "")

        if again == "yes" or again == "shop":
            itemshop()
            StartScreens.shopscreen
            ask = "no"

        elif again == "no":
            main_game()
            ask = "no"

        elif again == "cyrillstinkt":
            hints = 99999999
            itemshop()
            StartScreens.shopscreen
            ask = "no"

        else:
            clear ()
            print("Invalid answer")

class StartScreens:
    
    def startscreen():
        global wasShop, abspacing, falseG, falseW, lingu, hints, selected_word, tries, word_display, already_guessed, not_guessed, abspacing, wincoins, took_coin
    
        clear()

        print(Pics[9])
        language()
        while ask == "":
            again = str(input("Do you want to enter the shop? yes/no ")).lower().replace(" ", "")

            if again == "yes" or again == "shop":
                itemshop()
                main_game()
                ask = "no"

            elif again == "no":
                main_game()
                ask = "no"

            elif again == "cyrillstinkt":
                hints = 99999999
                itemshop()
                main_game()
                ask = "no"

            else:
                clear ()
                print("Invalid answer")

    def shopscreen():
        global wasShop, abspacing, falseG, falseW, lingu, hints, selected_word, tries, word_display, already_guessed, not_guessed, abspacing, wincoins, took_coin
    
        clear()

        print(Pics[9])
        while ask == "":
            again = str(input("Do you want to enter the shop? yes/no ")).lower().replace(" ", "")

            if again == "yes" or again == "shop":
                itemshop()
                main_game()
                ask = "no"

            elif again == "no":
                main_game()
                ask = "no"

            elif again == "cyrillstinkt":
                hints = 99999999
                itemshop()
                main_game()
                ask = "no"

            else:
                clear ()
                print("Invalid answer")

starter()

while True:
    main_game()