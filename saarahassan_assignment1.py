#set in computer's random guesses so it can calculate at the end:
import random
import sys
# ask if the player wants to play the game with the computer first 

# added in ).strip().lower() because I want it to accept all possible variables/spaces of Yes and No 
#examples: yes, no, Yes, No, YEs, NO, etc.
start = input ("Would you like to play the Lotto with Me? Type: Yes or No").strip().lower()
print(start)

#if they click yes, the game will resume
if start == "yes":
    print("Okay, Let's Do it!")
#if they write no, then the game will end here
elif start == "no":
        print("Aww, okay. Maybe next time!") 
#needed to add extra coding here to end the game and not loop to the next question for a "yes" answer 
        import sys
        sys.exit()


#if they put "yes" the computer will ask the player their name:
name = input ("What is your name?")
print (name, "Get Ready! Choose Numbers 1 - 50 only.")

#set aside the right guesses for the computer to follow the prize through with the right answers
answers = [2, 16, 28, 47, 35, 14]
#set a list empty for the player's guesses - numbers 1 through 50
guesses = []

#give it a name, with the range same as player (1-50) and 6 guesses
computer_guesses = random.sample(range(1,50),6)        
print(f"The Computer will play also!: Here are its guesses: {computer_guesses}")  

#let the player choose six numbers between 1-50, with a limit error if they pick above or below the range 1-50:
for i in range(6):
      while True:
            guess = int(input(f"Enter Guess {i + 1})"))

# Then show the player guesses that they have entered as they come up with 6 guesses:
            if 1 <= guess <= 50:
                guesses.append(guess)
                print("Here are your guesses:", guesses)
                break
            else:
                   print("Sorry, please choose numbers between 1 and 50 only.")


# Then we define to see how many numbers were guessed correctly, 
right_guesses = 0
prize = 0

# we will check here how many of the player's guesses are correct, giving $10 for each correct number 
for guess in guesses:
      if guess in answers:
        right_guesses += 1
        prize += 10

#then this code will calculate and display which of the 6 numbers they earned $10 each for: 
if right_guesses > 0:
      print(f"Yay! You guessed {right_guesses} right!")
      print(f"You won: ${prize}." "Nice Work!")
else:
      print("Sorry :( None are correct. Better luck next time!)")
      
# this code is for generating how many the computer got right at random, but computer doesn't get any prize
computer_right_answers = 0
for guess in computer_guesses:
      if guess in answers:
            computer_right_answers += 1
if computer_right_answers > 0:
        print(f"The Computer guessed {computer_right_answers} correctly!")
else: 
      print("The Computer didn't guess any correct numbers :/ Good Game.")

#If you want to ask the player if they want to play again(added.lower so any N/n/Y.y variations are accepted):
while True:
      restart_game = input ("Would you like to play again? Type Yes or No:").strip().lower()
      if restart_game == "yes":
            print("Awesome! Let's go Again.")
            continue

#if they say no, the game ends:
      elif restart_game == "no":
            print("Aww, okay. That was fun. See you next time!")
            import sys
            sys.exit()
      else: 
            print("Please type: Yes or No").strip().lower()

# I wanted to go above and beyond and try to loop the game to restart if the player says yes, but 
# it seems to be a little difficult for me.. I tried all afternoon
#I had soo much fun making this.... I played this game myself like a million times LOL 