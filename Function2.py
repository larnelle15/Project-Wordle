from is_valid_guess_fn 
import is_valid_guess

# Write the get_guess function here.
def get_guess(required_letters):
  booler = False
  while booler == False:
    guess = input("Enter your guess: \n")
    booler = is_valid_guess(guess, required_letters)
    if booler == False:
      print("Your guess must contain all yellow and green letters from your previous guesses.")
  return guess
  pass
