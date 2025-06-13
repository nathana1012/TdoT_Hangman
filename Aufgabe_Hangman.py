from random import *
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


#Hier kannst du noch weitere Wörter hinzufügen:
words = [
    "algorithmus",
    "python",
    "variable",
    "funktion",
    "schleife",
    "array"
]


def getRandomWord(wordList):
    wort = choice(wordList)
    return wort

#Mache eine Methode mit dem Namen "displayBoard" und als Parameter gibst du "HANGMANPICS, missedLetters, correctLetters, secretWord" mit

    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Falsche Buchstaben:', end=' ')
    #Gib die "missedLetters" aus die der Benutzer falsch geraten hat
    

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end=' ')
    print()



def getGuess(alreadyGuessed):

    #Mache hier eine variable mit dem Namen "alphabet" die alle Buchstaben aus dem Alphabet hat
    
    while True:
        try:
            derBuchstabe = input("Ein neuer Buchstaben den du noch nicht getippt hast: ")
            if len(derBuchstabe) != 1:
                raise ValueError("Nur ein Buchstaben")
            elif derBuchstabe in alreadyGuessed:
                raise ValueError("Du hast den Buchstaben bereits eingegeben!")
            elif not(derBuchstabe.upper() in alphabet.upper()):
                raise ValueError("Das ist kein Buchstaben")
            else:
                break
        except  ValueError as e:
            print(e)   

    return derBuchstabe


def playAgain():


    while True:
        try:
            nochmalsSpielen = input("Willst du nochmals Spielen? (Y/N)")
            if nochmalsSpielen.upper() == "Y" or nochmalsSpielen.upper() == "JA":
                again = True
                break
            elif nochmalsSpielen.upper() == "N" or nochmalsSpielen.upper() == "NEIN":
                again = False
                break
            else:
                raise ValueError("Ungültige eingabe")
        except  ValueError as e:
            print(e) 

    #Gib "again" zurück
     



#Gib einen schoenen Titel aus, damit der Benutzer weiss, worum es geht




missedLetters = ''
correctLetters = ''
#Mache eine Variable, die den Namen "secretWord" hat und die Funktion "getRandomWord" aufruft und als Parameter die Liste "words" hat

#Mache eine Variable Namens "gameIsDone" die den Boolean Wert "False" hat


while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yep! Das gesuchte Wort ist "' + secretWord + '"! Du hast gewonnen!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('Du hast alle Versuche verbraucht\nNach ' + str(len(missedLetters)) + ' falschen Versuchen und ' + str(len(correctLetters)) + ' korrekten Versuchen, wäre das Wort "' + secretWord + '" gewesen')
            gameIsDone = True

    if gameIsDone:
        #ADVANCED
        #Falls der Spieler nochmals spielen will, muessen alle Variablen (missedLetters, correctLetters) wieder geleert werden 
        #und gameIsDone auf False gesetz werden
        #Auch sollte ein neues Wort in secretWord ueber die Methode getRandomWord(words) gewaehlt werden
        if playAgain():
            print("Nochmals Spielen ...")

        else:
            #BRICH die Schleife ab da der Benutzer nicht mehr spielen will
           


        