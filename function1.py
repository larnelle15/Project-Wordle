
def is_valid_guess(guess, required_letters):
  for i in range(len(required_letters)):
    if required_letters[i] not in guess:
      return False
  return True

