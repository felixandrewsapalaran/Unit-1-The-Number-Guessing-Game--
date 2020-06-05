"""
Python Web Development Techdegree
Project 1 - Number Guessing Game

Felix Andrew Sapalaran (felixandrewsapalaran@gmail.com)
-------------------------------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

#store number of user attemp here
num_attempt = []


#create function that will display the score
def display_score():
    #check if there's current available score
    if len(num_attempt) <= 0:
        print("Great news! There is no currenly high score on the table. You could be the first!")
    else:
        #display the minimum attempt on the list
        print("The current high score is {} attempts".format(min(num_attempt)))
#create function that will control the game
def Game():

    #Generate a random number from 1 to 10
    jackpot_num = int(random.randint(1,10))
    name = input("Hi! What is your name? ")
    #Create welcome page
    greetings = print("""
    ----------------------------------------------
    Welcome to the Number Guessing Game {}!
    ----------------------------------------------
    """.format(name))

    #prompt user if they want to play
    play = input("Do you want to play the Guessing Game? (Yes/No): ")

    #count every attempt
    attempt = 0

    #if user answered yes start the game
    while play.lower() == 'yes':
        try:
            #capture user chosen number
            guess  = int(input("Please pick a number between 1 and 10: "))
            #raise error when user input is outside the given range
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            #compare user guessed number to jackpot number
            if guess == jackpot_num:
                print("You got it! My number was {}".format(jackpot_num))
                #once user guessed correct number increment
                attempt += 1
                #store number of attemp into the list
                num_attempt.append(attempt)
                #let user know how many times it took them to guessed the number
                print("It took you {} tries to guessed the number \n".format(attempt))
                #prompt the user if they want to play again
                play_again = input("Would you like to play again? (Yes/No): ")
                #restart number of attempt
                attempt = 0
                display_score()
                #generate random number again
                jackpot_num = int(random.randint(1,10))
                #if user answered 'no' to play again
                if play_again.lower() == 'no':
                    print("That's Ok, thanks for trying again.")
                    #break out of the game
                    break
            #if user answer yes do the following
            #check if the guess number is greater than the jackpot number
            #Give them a HINT
            elif guess > jackpot_num:
                print("It's lower than {}".format(guess))
                #increment attempt
                attempt += 1
            #check if the guess number is less than the jackpot number
            elif guess < jackpot_num:
                print("It's higher than {}".format(guess))
                attempt += 1
        #print message below if user input other than integer
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        #if user doesnt want to play the game
        print("That's OK, It's nice meeting you {}!".format(name))

#calling the function
if __name__ == '__main__':
    Game()
