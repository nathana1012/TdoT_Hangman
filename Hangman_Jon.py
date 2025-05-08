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


#Erstelle eine Liste aus Worten in der Form ['informatik', 'hardware', 'switch'] usw.
#Da diese Eingabe als Liste sehr muehsam ist, kannst du auch einen String eingeben un diesen splitten. "wort wort".split()

words = [
    "algorithmus",
    "python",
    "variable",
    "funktion",
    "schleife",
    "array",
    "liste",
    "klasse",
    "objekt",
    "software",
    "hardware",
    "verschlüsselung",
    "bit",
    "byte",
    "künstlicheintelligenz",
    "cloud",
    "debugging",
    "entwicklungsumgebung",
    "schnittstelle",
    "server",
    "client",
    "protokoll",
    "windows",
    "linux"
]

#Waehle ein zufaelliges Wort aus der Liste wordList und gib dieses mit return zurück
def getRandomWord(wordList):
    wort = choice(wordList)
    return wort

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Falsche Buchstaben:', end=' ')
    #Zeige hier alle falschen Buchstaben hintereinander an, welche in missedLetters gespeichert sind.
    #hier kommt dein Code
    print(missedLetters)

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end=' ')
    print()


#Hier soll ein Buchstabe vom Benutzer abgefragt werden. Aber Achtung nur ein Buchstabe.
#Falls es eine Zahl, mehrere Buchstaben oder ein Sonderzeichen oder nichts ist. Wiederhole die Abfrage
def getGuess(alreadyGuessed):

    alphabet = 'abcdefghijklmnopqrstuvwxyzöäü'
    #hier kommt dein Code
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

#Willst Du nochmals spielen? Frage den Spieler. Als Rueckgabewert wird True oder False erwartet.
def playAgain():
    #hier kommt dein Code
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

    return again #hier kommt dein Code


#Hier beginnt das Programm
#Gib einen schoenen Titel aus, damit der Benutzer weiss, worum es geht
print('H A N G M A N')
#hier kommt dein Code


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

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
        #Falls der Spieler nochmals spielen will, muessen alle Variablen (missedLetters, correctLetters) wieder geleert werden und gameIsDone auf False gesetz werden
        #Auch sollte ein neues Wort in secretWord ueber die Methode getRandomWord(words) gewaehlt werden
        if playAgain():
            #hier kommt dein Code
            print("Nochmals Spielen ...")
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break


        #Arvin testing