### My Hangman Project - Rico

### 1. Game Initialization
## Store a list of word. Ensure it's a data type.
## Utilize the random library to randmly select a word from the list.

from random import choice
from time import time
#import threading

list_of_word = ["camel","kangaroo", "given", "dinosour", "tigers"]
chosen_word = choice(list_of_word)


### 4. Tracking Incorrect Attempts
## 4.1 Limit the number of incorrect quesses (e.g, 6 incorrect guesses)
## 4.2 Display the Hangman figure progressively for each incorrect guess.


def show_hangman(wrong):

## 4.2 Display the Hangman figure progressively for each incorrect guess.
    
    if wrong == 0:
        print("\n*********** ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print("=====         ")
    elif wrong == 1:
        print("\n*********** ")
        print("  |          O")
        print("  |           ")
        print("  |           ")
        print("=====         ")
    elif wrong == 2:
        print("\n*********** ")
        print("  |       O   ")
        print("  |       |   ")
        print("  |           ")
        print("=====         ")
    elif wrong == 3:
        print("\n*********** ")
        print("  |       O   ")
        print("  |      /|   ")
        print("  |           ")
        print("=====         ")
    elif wrong == 4:
        print("\n*********** ")
        print("  |       O   ")
        print("  |      /|\  ")
        print("  |           ")
        print("=====         ") 
    elif wrong == 5:
        print("\n*********** ")
        print("  |       O   ")
        print("  |      /|\  ")
        print("  |      /    ")
        print("=====         ")
    elif wrong == 6:
        print("\n*********** ")
        print("  |       O"   )
        print("  |      /|\  ")
        print("  |      / \  ")
        print("=====         ")


    ## Put the correct letter guess here

def correct_word(guessed_letter):
    counter = 0
    correct_letters=0
    for char in chosen_word:
        if (char in guessed_letter):
            print(chosen_word[counter], end=" ")
            correct_letters +=1
        else:
            print(" ", end=" ")
        counter +=1
    return correct_letters

            
def printline():
    print("\r")
    for char in chosen_word:
       print("\u203E", end=" ") # will print underline onthe letter being guess


#def countdown():
#    global my_timer
#
#    my_timer = 5
#
#    for x in range(10):
#        my_timer = my_timer - 1
#        sleep(1)
#    print ("Out of Time!")

#countdown_thread = threading.Thread (target = countdown)

#countdown_thread.start()

#while my_timer > 0:

def main(): # this is for game restart

### 2. Displaying the Game State
## 2.1 Display a welcome message indicating the number of letters in the hidden word, represented by underscores.
## 2.2 Update the displayed word after each correct letter guess.

    print ("\n \n")
    print ("My First Project - Welcome to the World of Hangman")
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("\n \nThe word for you has", len(chosen_word), "letters: " + "_ " * len(chosen_word)) ## 2.1 Display a welcome message indicating the number of letters in the hidden word, represented by underscores.
    print ("\n \n")

    length_of_word_to_guess = len(chosen_word)
    number_of_wrong = 0
    current_guessed_index = 0
    current_guessed_letter = []
    current_right_letter = 0 

#    start_time = time



    while(number_of_wrong != 6 and current_right_letter != length_of_word_to_guess):
        print("\nLetters Guessed so far: ")
     #   print(" ")
        for letter in current_guessed_letter:
            print(letter, end=" ")

### 3. Taking User Input
## 3.1 Prompt the user to input the letter for their guess
## 3.2 Ensure the input is a valid single letter and ignore case.
        
        guess = input("\nTime to Guess a letter: ").lower() ## 3.1 Prompt the user to input the letter for their guess

### 6. Timer Restriction
## Add a timer restriction of 30 seconds per user to guess a word    

        #time.sleep(3)
        #elapsed_time = time() - start_time
        #   if elapsed_time >30:
        #      print ("Time is UP!")
         #     break
                
        ## user is right
        if(chosen_word[current_guessed_index] == guess):
            show_hangman(number_of_wrong)
            ## Print Word
            current_guessed_index +=1
            current_guessed_letter.append(guess)
            current_right_letter = correct_word(current_guessed_letter)
            print(current_guessed_letter)
            printline() ## 2.2 Update the displayed word after each correct letter guess.
        
        ## User was wrong
        else:
            number_of_wrong +=1
            current_guessed_letter.append(guess)
            show_hangman(number_of_wrong) ## update the drawing
            ## print word
            current_right_letter = correct_word(current_guessed_letter)
            printline()

        if guess.isalpha() or len(guess) == 1: ## 3.2 Ensure the input is a valid single letter and ignore case.
            print("\nYou Type a Letter: ") # to test is user enter a letter string only
        else: 
            print("Please type a single letter and no numberic!")

### 5. Win/Lose Conditions
## Implement contidions for a win (correctly guessing the word) and a loss (exceeting allowed incorrect guesses)
## Display and appropriate message for the outcome

    
    if number_of_wrong >= 6: ## 4.1 Limit the number of incorrect quesses (e.g, 6 incorrect guesses)
        print (" ")
        print("\nSorry, you ran out of attempts. The word was: ", chosen_word)
    
     
    elif set(chosen_word) == set(chosen_word):
        print("\nCongratulations! You guessed the word: ", chosen_word)




### 7. Play Again Option
## 7.1 After a game ends, ask the player if they want to play again
## 7.2 If yes, reset the game; if no, display a farewell message

    play_again = input("\nDo you want to try again? (y) or (n): ").lower() ## 7.1 After a game ends, ask the player if they want to play again

    if play_again.startswith('y'): ## 7.2 If yes, reset the game; if no, display a farewell message
        main() # this will reset the game
    else:
        print("\nThanks for playing! Hope you enjoy the game.") ## 7.2 If yes, reset the game; if no, display a farewell message
        print (" ")

main() # call function to run the game






