# Write the print_guess function here.
from modules import print_in_color
### DO NOT MODIFY ABOVE
def color(num, secret_word, guess):
  if guess[num] == secret_word[num]:
    return 'green'
  elif guess[num] not in secret_word:
    return 'red'
  else:
    return 'yellow'

def print_guess(secret_word, guess):
  required_letters = []
  for i in range(0,5):
    print_in_color(guess[i], color(i, secret_word, guess))
    if color(i, secret_word, guess) != 'red':
      required_letters.append(guess[i])
  return required_letters
