from get_guess_fn import get_guess                 #
from is_game_over_fn import is_game_over           #
from modules import print_in_color                 #
from print_guess_fn import print_guess             #
####################################################
secret_word = input("Enter the secret word: \n")
required_letters = []
runner = False
tries_left = 5
while runner == False:
  guess = get_guess(required_letters)
  runner = is_game_over(secret_word, guess, tries_left)
  if runner == True:
    continue
  required_letters = print_guess(secret_word, guess)
  print()
  tries_left -= 1
