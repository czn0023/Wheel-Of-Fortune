open(r"words.txt")
import random
playerlist = [0, 1, 2]
totalmoney = [0, 0, 0]
player = random.choice(playerlist)
wheel = ['LOSE A TURN', 'BANKRUPT', 'BANKRUPT', 800, 500, 650, 500, 900, 450, 500, 600, 700, 600, 650, 500, 700, 500, 700, 500, 600, 550, 500, 600, 650, 700, 750]
round = 1
vowels = ["A","E","I","O","U"]
consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
rlstine = ['R', 'S', 'T', 'L', 'N', 'E']
print(f"Welcome to Wheel of Fortune!\n=======================================\nPlayer {player + 1} has been selected to go first!")
notsolved = True
#First two rounds
while round != 3:    
    roundmoney = [0, 0, 0]
    word = random.choice(list(open(r"words.txt")))
    word = word.upper()
    word = word.rstrip("\n")
    pickedword = []
    while word in pickedword:
        word = random.choice(list(open(r"words.txt")))
    pickedword.append(word)
    brokenword = list(word)
    blankword = "-" * len(word)
    while notsolved == True:
        print(word)
        print(pickedword)
        print(brokenword)
        print(blankword)
#Determine which player money to report
        print(f"\nRound {round}\n========\nPlayer {player + 1}, it's your turn!\nYou have ${roundmoney[player]}.\n")
        choice = str(input(f"'Spin' to spin the wheel, or type 'Solve' to solve the puzzle.\n"))
        choice = choice.upper()
        if choice == "SPIN":
            wedge = random.choice(wheel)
            if wedge == "BANKRUPT":
                #Bankrupt
                print(f"\nYou landed on {wedge}. Oh no! Your turn has ended, and you have lost your money for the round.\n")
                roundmoney[player] = 0
                player += 1
                if player == 3:
                    player = 0
            elif wedge == "LOSE A TURN":
                #Lose a Turn
                print(f"\nYou landed on {wedge}. Oh no! Your turn has ended.\n")
                player += 1
                if player == 3:
                    player = 0
            else:
                guess = str(input(f"\nYour letter is worth ${wedge}!\nPlease enter your consonant.\n"))
                guess = guess.upper()
                while guess in vowels:
                    guess = str(input(f"\nThat is a vowel! You need to guess a consonant.\n"))
                if guess in brokenword:
                    print(f"\n{guess} is in the word!\n")
                    #Display guessed letters and their location in the word
                    index = 0
                    while index != len(brokenword):
                        if guess == brokenword[index]:
                            blankword = blankword[:index] + guess + blankword[index + 1:]
                            index += 1
                        else:
                            index += 1
                    print(blankword)
                    #ADD MONEY EARNED
                    roundmoney[player] = roundmoney[player] + wedge
                    choice = "Y"
                    while choice == "Y":
                        choice = str(input(f"\nDo you want to buy a vowel for $250? Y/N\n"))
                        choice = choice.upper()
                        if choice == "Y":
                            if roundmoney[player] < 250:
                                print(f"\nYou only have {roundmoney[player]}, you need $250 to buy a vowel!\n")
                                choice  = "N"
                                break
                            roundmoney[player] = roundmoney[player] - 250
                            guess = str(input(f"Y\nPlease enter your vowel.\n"))
                            guess = guess.upper()
                            while guess in consonants:
                                guess = str(input(f"\nThat is a consonant! You need to guess a vowel.\n"))
                            if guess in brokenword:
                                print(f"\n{guess} is in the word!\n")
                                #Display guessed letters and their location in the word
                                index = 0
                                while index != len(brokenword):
                                    if guess == brokenword[index]:
                                        blankword = blankword[:index] + guess + blankword[index + 1:]
                                        index += 1
                                    else:
                                        index += 1
                                print(blankword)
                else:
                    print(f"\n{guess} is not in the word.\n")
                    print(blankword)
                    player += 1
                    if player == 3:
                        player = 0
        else:
            guess = str(input(f"\nPlease enter the full word.\n"))
            guess = guess.upper()
            if guess == word:
                totalmoney[player] = totalmoney[player] + roundmoney[player]
                print(f"\nCongragulations! You guessed correctly!\nPlayer {player + 1} added {roundmoney[player]} to the bank.")
                print(f"\nTotal Money for Contestants\nPlayer 1:{totalmoney[0]}\nPlayer 2:{totalmoney[1]}\nPlayer 3:{totalmoney[2]}\n\n")
                round += 1
                player += 1
                if player == 3:
                    player = 0
                break
            else:
                print("That is not correct!")
                player += 1
                if player == 3:
                    player = 0
print(f"\nThis is the final round!\n")
#Determine highest totalmoney
top = max(totalmoney)
player = totalmoney.index(top)
print(f"Player {player + 1} has the highest amount of money, with ${totalmoney[player]} in the bank!\nThat means you're playing the final round!")
word = random.choice(list(open(r"words.txt")))
word = word.upper()
word = word.rstrip("\n")
pickedword = []
while word in pickedword:
    word = random.choice(list(open(r"words.txt")))
pickedword.append(word)
brokenword = list(word)
blankword = "-" * len(word)
print(f"In the final round, the player gets to choose three consonants and a vowel to help them guess the word.\n")
print(f"\nThe letters R, S, T, L, N, and E are chosen automatically. Here is the word with these letters already displayed.\n")
#Factor RSTLNE into chosen word
for x in rlstine:
    index = 0
    while index != len(brokenword):
        if x == brokenword[index]:
            blankword = blankword[:index] + x + blankword[index + 1:]
            index += 1
        else:
            index += 1
print(word)
print(pickedword)
print(brokenword)
print(blankword)
con1 = str(input(f"\nPlease enter your first consonant:\n"))
con1 = con1.upper()
while con1 in vowels:
    con1 = str(input(f"\nThat is a vowel! You need to guess a consonant.\n"))
if con1 in brokenword:
    index = 0
    while index != len(brokenword):
        if con1 == brokenword[index]:
            blankword = blankword[:index] + con1 + blankword[index + 1:]
            index += 1
        else:
            index += 1
con2 = str(input(f"\nPlease enter your second consonant:\n"))
con2 = con2.upper()
while con2 in vowels:
    con2 = str(input(f"\nThat is a vowel! You need to guess a consonant.\n"))
if con2 in brokenword:
    index = 0
    while index != len(brokenword):
        if con2 == brokenword[index]:
            blankword = blankword[:index] + con2 + blankword[index + 1:]
            index += 1
        else:
            index += 1
con3 = str(input(f"\nPlease enter your third consonant:\n"))
con3 = con3.upper()
while con3 in vowels:
    con3 = str(input(f"\nThat is a vowel! You need to guess a consonant.\n"))
if con3 in brokenword:
    index = 0
    while index != len(brokenword):
        if con3 == brokenword[index]:
            blankword = blankword[:index] + con3 + blankword[index + 1:]
            index += 1
        else:
            index += 1
vowel = str(input(f"\nPlease enter your vowel:\n"))
vowel = vowel.upper()
while vowel in consonants:
    vowel = str(input(f"\nThat is a consonant! You need to guess a vowel.\n"))
if vowel in brokenword:
    index = 0
    while index != len(brokenword):
        if vowel == brokenword[index]:
            blankword = blankword[:index] + vowel + blankword[index + 1:]
            index += 1
        else:
            index += 1
guess = str(input(f"\n{blankword}\nPlease guess the word above:"))
guess = guess.upper()
if guess == word:
    print(f"\n\nCONGRAGULATIONS!\nPlayer {player} won the final round with ${totalmoney[player]}!")
else:
    print("\n\nOh no! Thats incorrect!\nGAMA OVAR")