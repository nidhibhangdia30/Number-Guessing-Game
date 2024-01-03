
import random
print("Welcome to the number guessing game!")
print("Guess a number between 1 & 100")

correct_number = random.randint(1,100)

def guess_number(attempts):
  for i in range(attempts):
    user_guess = int(input("Make a guess: "))
    if user_guess == correct_number:
      return "You made the correct guess."
    elif user_guess < correct_number:
      print("Too low")
    elif user_guess > correct_number:
      print("Too High")
    print(f"Attempts left: {attempts - (i + 1)}")
  return f"Sorry you have run out of attempts. The correct guess was {correct_number}"

choice = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
if choice == 'easy':
  attempts = 10
  print(f"You have {attempts} to guess the number")
else:
  attempts = 5
  print(f"You have {attempts} to guess the number")
 
result = guess_number(attempts)
print(result)
