# Write the is_game_over function here.

def is_game_over(secret_word, guess, tries_left):
  if (tries_left <= 0):
    print("Game over! The correct word is "+secret_word+".")
    return True
  elif secret_word == guess:
    print("Correct! You got it in",(6-tries_left),"tries!")
    return True
  else:
    return False
