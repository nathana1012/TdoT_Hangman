import random
import getpass

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

secretWords = [
    "Byte",
    "Code",
    "Data",
    "Disk",
    "Edit",
    "File",
    "Game",
    "Hack",
    "Icon",
    "Java",
    "Keys",
    "Link",
    "Mail",
    "Menu",
    "Node",
    "Port",
    "Rank",
    "Ruby",
    "Scan",
    "Site",
    "Sort",
    "Tech",
    "Type",
    "Unix",
    "User",
    "View",
    "Wave",
    "Web",
    "Wiki",
    "Zip",
    "Access",
    "Action",
    "Array",
    "Audio",
    "Binary",
    "Border",
    "Buffer",
    "Canvas",
    "Cipher",
    "Client",
    "Clouds",
    "Cluster",
    "Coding",
    "Column",
    "Config",
    "Console",
    "Control",
    "Cookie",
    "Cursor",
    "Daemon",
    "Debug",
    "Decode",
    "Domain",
    "Encode",
    "Engine",
    "Folder",
    "Format",
    "Header",
    "Helper",
    "Kernel"
]

def startscreen():
  print("+--------------------+")
  print("¦ WELCOME TO HANGMAN ¦")
  print("¦                    ¦")
  print("¦        +---+       ¦")
  print("¦        |   |       ¦")
  print("¦        O   |       ¦")
  print("¦       /|\  |       ¦")
  print("¦       / \  |       ¦")
  print("¦            |       ¦")
  print("¦     ==========     ¦")
  print("¦   Press R + Enter  ¦")
  print("+--------------------+")
  ready = input("")
  while ready != "R" and ready != "r":
    ready = input("")
  return "ready"

def mainOnePlayer():
  # anzahl versuche
  life = 0
  # wählt ein random Wort von der Liste
  secretWord = secretWords[random.randint(0,59)]
  secretWord = secretWord.upper()
  secretWord = list(secretWord)
  # erstellt die userguess Liste
  userGuess = ("_ ") * len(secretWord)
  #Liste mit den bereits falsch geratenen Buchstaben
  alreadyGuessed = []
  print(HANGMANPICS[life] + "\n")
  print(userGuess + "\n")
  # überprüft ob das Wort noch nicht erraten ist
  while "_" in userGuess:
    # fragt nach Buchstabe
    guess = input("Guess a letter or the hidden word:\n")
    guess = guess.upper()
    if guess == "".join(secretWord):
      return "win"
    # überprüft ob der guess den richtigen Datentyp hat und nicht ein bereits geratener Buchstabe ist
    while guess in alreadyGuessed or len(guess) > 1 or not guess.isalpha():
      print("\nYou already tried this letter or your input is invalid")
      print("Already guessed letters:\n" + " ".join(alreadyGuessed))
      guess = input("\nGuess a letter or the hidden word:\n")
      guess = guess.upper()
    alreadyGuessed.append(guess)
    # überprüft ob guess richtig ist
    if guess in secretWord:
      # fügt guess dem userGuess hinzu und zeigt dann das Menü
      for i in range(secretWord.count(guess)):
        positionGuess = secretWord.index(guess)
        userGuess = list(userGuess)
        userGuess[positionGuess*2] = guess
        userGuess = "".join(userGuess)
        secretWord[positionGuess] = "+"
      secretWord = "".join(secretWord)
      secretWord = secretWord.replace("+", guess)
      secretWord = list(secretWord)
      print("Your guess was correct!\n")
      print(HANGMANPICS[life], "\n")
      print(userGuess + "\n")
      if "_" in userGuess:
        print("Already guessed letters:\n" + " ".join(alreadyGuessed))
    elif guess not in secretWord: 
      # printed das entsprechende Menü + überprüft ob noch Versuche vorhanden sind
      life = life + 1
      print("Your guess was incorrect!\n")
      print(HANGMANPICS[life])
      print("\n" + userGuess + "\n")
      print("Already guessed letters:\n" + " ".join(alreadyGuessed) + "\n")
      # wenn keine versuche vorhanden sind Lossscreen
      if life == 6:
        print("\nThe word was: " + "".join(secretWord) + "\n")
        return "lose"
  # winscreen
  if life < 6:
    return "win"

def winscreen():
  print("+--------------------+")
  print("¦  YOU GOT IT RIGHT! ¦")
  print("¦      YOU  WON!     ¦")
  print("¦                    ¦")
  print("¦             +---+  ¦")
  print("¦             |   |  ¦")
  print("¦                 |  ¦")
  print("¦      O          |  ¦")
  print("¦     /|\         |  ¦")
  print("¦     / \         |  ¦")
  print("¦ ================== ¦")
  print("¦  WANNA PLAY AGAIN? ¦")
  print("+--------------------+")
  again = input("")
  again = again.lower()
  while again != "yes" and again != "no":
    print("(yes or no)")
    again = input("")
    again = again.lower()
  return again

def losescreen():
  print("+--------------------+")
  print("¦     YOU LOST!      ¦")
  print("¦  HE LEFT US! RIP!  ¦")
  print("¦                    ¦")
  print("¦        +---+       ¦")
  print("¦        |   |       ¦")
  print("¦        O   |       ¦")
  print("¦       /|\  |       ¦")
  print("¦       / \  |       ¦")
  print("¦            |       ¦")
  print("¦     ==========     ¦")
  print("¦  WANNA PLAY AGAIN? ¦")
  print("+--------------------+")
  again = input("")
  again = again.lower()
  while again != "yes" and again != "no":
    print("(yes or no)")
    again = input("")
    again = again.lower()
  return again

def mainTwoPlayer():
  # automatisch zwei durchgägne damit jeder spieler einmal raten darf
  for i in range(2):
    # anzahl versuche
    life = 0
    if i == 0:
      firstplayer = 2
    if i == 1:
      firstplayer = 1
    secretWord = getpass.getpass("Player" + str(firstplayer) + ": Your secret word:\n")
    while not secretWord.isalpha():
      print("invalid secret word, please use onle letters:")
      secretWord = getpass.getpass("Player" + str(firstplayer) + ": Your secret word:\n")
    secretWord = secretWord.upper()
    secretWord = list(secretWord)
    # erstellt die userguess Liste
    userGuess = ("_ ") * len(secretWord)
    #Liste mit den bereits falsch geratenen Buchstaben
    alreadyGuessed = []
    print(HANGMANPICS[life] + "\n")
    print(userGuess + "\n")
    while "_" in userGuess:
      # fragt nach Buchstabe
      guess = input("Player" + str(i+1) + ": Guess a letter or the hidden word:\n")
      guess = guess.upper()
      if guess == "".join(secretWord):
        print("\n")
        break
      # überprüft ob der guess den richtigen Datentyp hat und nicht ein bereits geratener Buchstabe ist
      while guess in alreadyGuessed or len(guess) > 1 or not guess.isalpha():
        print("\nYou already tried this letter or your input is invalid")
        print("Already guessed letters:\n" + " ".join(alreadyGuessed))
        guess = input("\nPlayer" + str(i+1) + ": Guess a letter or the hidden word:\n")
        guess = guess.upper()
      alreadyGuessed.append(guess)
      # überprüft ob guess richtig ist
      if guess in secretWord:
        # fügt guess dem userGuess guess hinzu und zeigt dann die Überschrift
        for i in range(secretWord.count(guess)):
          positionGuess = secretWord.index(guess)
          userGuess = list(userGuess)
          userGuess[positionGuess*2] = guess
          userGuess = "".join(userGuess)
          secretWord[positionGuess] = "+"
        secretWord = "".join(secretWord)
        secretWord = secretWord.replace("+", guess)
        secretWord = list(secretWord)
        print("Your guess was correct!\n")
        print(HANGMANPICS[life], "\n")
        print(userGuess + "\n")
        if "_" in userGuess:
          print("Already guessed letters:\n" + " ".join(alreadyGuessed))
      elif guess not in secretWord: 
        # printed das entsprechende Menü + überprüft ob noch Versuche vorhanden sind
        life = life + 1
        print("Your guess was incorrect!\n")
        print(HANGMANPICS[life])
        print("\n" + userGuess + "\n")
        print("Already guessed letters:\n" + " ".join(alreadyGuessed) + "\n")
        # wenn keine versuche vorhanden sind Lossscreen
        if life == 6:
          print("\nThe word was: " + "".join(secretWord) + "\n")
          print(HANGMANPICS[life] + "\n")
          print("You lost!")
          break
    # winscreen
    if life < 6:
      print("You got it!\n")
    
def mainGame():
  # script das alle defs zusammenhängt
  readystart = startscreen()
  if readystart == "ready":
    player = input("One Player(1) or two Players(2)?")
    while player != "1" and player != "2":
      print("Invalid Input")
      player = input("Oneplayer(1) or Twoplayer(2)? \n")
    if player == "1":
      while True:
        res = mainOnePlayer()
        if res == "win":
          winagain = winscreen()
          if winagain == "no":
           exit(0)
        if res == "lose":
          losagain = losescreen()
          if losagain == "no":
            exit(0)
    elif player == "2":
      while True:
        res = mainTwoPlayer()
        againTwo = input("Wanna play again?")
        againTwo = againTwo.lower()
        while againTwo != "yes" and againTwo != "no":
          print("yes/no")
          againTwo = input("Wanna play again?")
        if againTwo == "no":
          exit(0)

mainGame()