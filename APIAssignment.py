# Aarian Dhanani from Maria Suarez
# 02/23/2022
# Word Game

import os, random, json, requests, sys, datetime
os.system('clear')

#Get the json
request1 = requests.get('https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json')
words = request1.json()
wordChoices = words.keys()

#Define variables
global word
gameOn = True
tries = 0
letterGuessed = ""
wordSelection = ""
difficultyDone = 0
difficultyChoice = ""
guess = ""
global playAgainOrNo
score = 0

#Ask for the username
global username
username = input("What is your username? ")

#Guess function that can be called
def guessFunction():
    global guess
    check = True
    while check:
        try:
            guess = input("Enter a letter to guess the word: ")
            if guess.isalpha() and len(guess)==1:
                check = False
            else:
                print("Please only enter one letter: ")
        except ValueError:
            print("Please only enter one letter: ")

#Play again class
def playGame():
    playAgainOrNo = input("Enter y to play again or any other letter to quit: ")
    return playAgainOrNo

#Main game loop
while gameOn:
    # print(difficultyDone) For testing purposes
    #Getting the difficulty
    while (difficultyDone != 1):
        difficultyChoice = input("Please select a difficulty level from 3-5: ")
        wordLength = []
        if difficultyChoice == '3':
            for i in wordChoices:
                if len(i) == 3:
                    wordLength.append(i)
            wordSelection = random.randint(0,len(wordLength))
            wordWord = wordLength[wordSelection]
            difficultyDone = 1
        elif difficultyChoice == '4':
            for i in wordChoices:
                if len(i) == 4:
                    wordLength.append(i)
            wordSelection = random.randint(0,len(wordLength))
            wordWord = wordLength[wordSelection]
            difficultyDone = 1
        elif difficultyChoice == '5':
            for i in wordChoices:
                if len(i) == 5:
                    wordLength.append(i)
            wordSelection = random.randint(0,len(wordLength))
            wordWord = wordLength[wordSelection]
            difficultyDone = 1
        else:
            print("Please enter one of these difficulty levels: 3, 4, or 5")

    print(wordWord)
    guessFunction()
    # print(guess)
    letterGuessed += guess  #letterGuessed=letterGuessed + guess
    #Check if the letter is in the word
    if guess not in wordWord:
        tries +=1
        # print(tries)# for testing delete when game is ready
    countLetter = 0
    for letter in wordWord:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter += 1
        else:
            print("_", end=" ")
    #Loser if statement
    if tries > 6:
        print("You're out of chances.")
        playAgainOrNo = playGame()
        if playAgainOrNo == "y":
            gameOn = True
            tries = 0
            letterGuessed = ""
            wordSelection = ""
            difficultyDone = 0
            difficultyChoice = ""
            guess = ""
            wordWord = ""
            score = 0
        else:
            gameOn = False
            sys.exit()
    #Winner if statement
    if countLetter == len(wordWord):
        print ("You guessed the word!")
        score = 6 - tries
        date = datetime.datetime.now()
        scoreReport = "Username: " + username + ". Date: " + str(date) + ". Score: " + str(score) + "\n"
        print(scoreReport)
        with open('/Users/aariandhanani/Desktop/AarianDhananiDataScience/scoreFile.json', 'a') as f:
            json.dump(scoreReport, f)
        playAgainOrNo = playGame()
        if playAgainOrNo == "y":
            gameOn = True
            tries = 0
            letterGuessed = ""
            wordSelection = ""
            difficultyDone = 0
            difficultyChoice = ""
            guess = ""
            wordWord = ""
            score = 0
        else:
            gameOn = False
            sys.exit()