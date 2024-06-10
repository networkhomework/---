import random

def guess_the_number():
  min_number = 1
  max_number = 100

  secret_number = random.randint(min_number, max_number)
  num_guesses = 0

  print(f"I'm thinking of a number between {min_number} and {max_number}. Try to guess it!")

  while True:
    try:
      guess = int(input("Take a guess: "))
      num_guesses += 1

      if guess < secret_number:
        print("Too low. Guess again.")
      elif guess > secret_number:
        print("Too high. Guess again.")
      else:
        print(f"You guessed it! The number was {secret_number} in {num_guesses} guesses.")
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  guess_the_number()
