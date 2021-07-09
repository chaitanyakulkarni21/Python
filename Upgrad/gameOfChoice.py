## Guess the Number | Decision Making | Looping | R & D
# 2 Players
# computerChoice : generate a random number between 1-20
# playerChoice : ask the user to enter a number between 1-20
 
# if the playerChoice is greater then computerChoice:
    # display "your guess is too high"
    
# if the playerChoice is lesser then computerChoice:
    # display your guess is too low
    
# if the playerChoice and  computerChoice matches:
    # display: "Gotcha! you guessed  it right"
    
#please note: a user can attempt a max of 6 guesses after 6 guesses
    # display "a oh ! you have exhausted all your attempts"

from random import randint
computerChoice = randint(1,20)
print("Computer Choice: ", computerChoice)
for count in range(6):
  playerChoice = int(input("Enter a number between 1 and 20: "))

  if playerChoice > computerChoice:
    print("Your guess is too high")
  elif playerChoice < computerChoice:
    print('Your guess is too low')
  elif playerChoice == computerChoice:
    print("Gotcha!! You guessed it right...")
else:
  print("You have exhausted your attempts...")