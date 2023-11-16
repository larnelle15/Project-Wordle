In the game Wordle, the user is trying to guess a secret 5 letter word. The user will type in a 5 letter guess, and the computer will share information about how close the guess is to the actual answer. 
If a letter in the guess exactly matches a letter in the answer (same letter and correct position), the letter will be marked green.
If a letter in the guess almost matches a letter in the answer (same letter, but incorrect position), the letter will be marked yellow.
If a letter in the guess doesn’t match a letter in the answer (guessed letter doesn’t exist in answer), the letter will be marked red. I know the actual game marks the letter gray, but I will mark it red to be super clear.

The user will use this information to then make another guess, and will keep guessing until they guess the answer (they win), or they run out of their 6 guesses (they lose).

For example, if the secret answer is TOWEL and the user guesses LOWER, the computer should print out LOWER. 

The O, W, and E(in the words TOWEL and LOWER) are all green because the user guessed those letters in the correct position.
The L(in TOWEL and LOWER) is yellow because L is the last letter in the answer, but the user guessed it in the first position.
The R(in TOWEL and LOWER) is red because it does not appear in the answer.

For this project, I will be implementing the game in hard mode. In hard mode, if a user guesses a letter in a previous guess that was either yellow or green, they must use it in their next guess (it needn’t be in the same position). 

For example, if the user guesses LOWER and the computer prints out LOWER (L is in yellow; O, W, E are in green; R is in red), the user must reuse the letters L, O, W, and E in their subsequent guesses. In invalid guess will not count towards one of the user’s 6 guesses
Here are the few differences from the real game:
In this project, I will be doing the user input and output in the terminal (as opposed to an online web browser like the real game).
I will also assume that no answer or guess has duplicate letters (i.e. a guess like TOTEM is not allowed because it has 2 Ts).  Allowing duplicates makes the project more complicated, and requires additional data structures like arrays, which I haven’t learned yet. I will also assume that all guesses will be all capitalized.
You do not need to check if any of the guesses are real words.
In hard mode, a user does not need to reuse green letters in the same position. As long as they use all green/yellow letters from their previous guesses in their new guess (regardless of which position they’re in), their guess is valid. 

