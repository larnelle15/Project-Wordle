First(Function one)
I'll start by writing the first required function, is_valid_guess(guess, required_letters). This function takes in a guess (string) and required_letters (list) and outputs
True if the guess is valid (i.e. it contains all of the letters in required_letters), and false otherwise.
Then (Function 2)
Now, I'll write get_guess(required_letters), where required_letters is a list.
The function should:
Prompt the player to input a guess with the message Enter your guess:.
If the guess is valid, return the guess. Otherwise, print Your guess must contain all yellow and green letters from your previous guesses. and then repeat step (1)
Then(Function 3)
I'll write
print_guess(secret_word, guess)
where guess and secret_word are strings.
The function should:
Print the characters inside of guess with the correct color.
Create a list of characters that are in both guess and secret_word and return that list.
Now(Function 4)
I'll write
is_game_over(secret_word, guess, tries_left)
where guess and secret_word are strings and tries_left is an int.
The function should:
Print Game over! The correct word is {secret_word}. if the game is over and the user did not guess the secret word.
Print Correct! You got it in X tries! if the user guessed the secret word.
Return True if the game is over and False otherwise
The game is considered over if:
user guesses correctly OR
until they use up all 6 tries
