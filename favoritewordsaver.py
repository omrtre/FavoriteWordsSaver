import os

wordList = []

def registerWord():

    if os.path.exists("favoriteWords.txt"):
        wordFile = open("favoriteWords.txt", "a") 
    else:
        wordFile = open("favoriteWords.txt", "w") 
          
    wordAddLoop = "Yes"
    wordDefinitionLoop = "Yes"

    count = 0

    while wordAddLoop == "Yes" or wordAddLoop == "yes" or wordAddLoop == "y":
        wordNew = input("What is your new favorite/interestring word(s) of the day? ")         
        wordFile.write(wordNew + "\n")

        wordDefinitionAmount = int(input("How many definitions does this word have? "))
        
        for x in range(wordDefinitionAmount):
            wordSpeechType = input("noun / pronoun / verb / adjective / adverb / preposition / conjunction / interjection ? ") ### adjective, noun, etc
            wordDefinition = input("Definition of the word? ") ### definitnio of the word
            count += 1
            wordFile.write(wordSpeechType + "\n")
            wordFile.write(str(count) + ". " + wordDefinition + "\n")
        
        #while wordDefinitionLoop == "Yes":
        #    wordDefinitionLoop = input("Is there another definition to the word? (Yes/No) ")
        #    if wordDefinitionLoop == "Yes":
        #        wordSpeechTypeMulti = input("Alternative speech type of the word? ")
        #        wordDefinitionMulti = input("Alternative definition of the word? ")
        wordFile.write("\n")
        count = 0
        wordAddLoop = input("Would you like to add another word? (Yes/No) ")

    wordFile.close()
    return [wordNew, wordSpeechType, wordDefinition]



def main():
    registerWord()
### openFIlewrite
#### if open Filewrite exists, write to the same file
#### Word Template

#### 'Word' - (Speech Type)
#### Definition
    #### 1st deifnition
    #### 2nd definition
#### Acessed whatever date

### store word in a list 1 x 3, [word, speech type, definition]; 0 is head, -1 is tail always within another array, the 2nd array is always speech type, the middle are always other deifnitions

### a oop to ask if there is another definition
### if so, ask the quesiton, store thi deifinitino in its proper array position
### if not move on in sequences

### a loop to ask if you want to enter qanother word.
### ask to end program, y/n, force quit if press something

main()