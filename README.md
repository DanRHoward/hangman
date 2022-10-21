# Hangman Game in Python

This code attempts to create a virtual game of Hangman. This version contains only 5 different possible words which may be found in the list named 'word_list'. I have incorporated a validation mechanic for inputs that the players make to ensure that they enter single characters from the English alphabet.

## Defined functions

In file milestone_3.py, there are defined functions which relate to the 2 operators which have already been implemented. One of which is in regards to the checking the validity of the players input ("ask_for_input(guess)"), and the other determines whether the guessed input is within the randomly chosen word ("check_input()").

## Classes and methods

In file milestone_4.py, the 'Hangman' class is created. The two methods involved regards the checking of the player input and the asking for input from the player, along with responses. At the bottom of the class definition there is an example which can be run to trial with a test list of words.

## Completed version of the Hangman game

The finished version of the Hangman game can be found in file finished_game.py. The final version is based upon the code created in file called milestone.py, where the 'Hangman' class is defined which contains the initial state of the game, along with the appropriate methods corresponding with verifying guesses and aquiring inputs from the player. Furthermore, the function 'play_game' is an addition which defines the logic of the game dependent upon the outputs from the class and certain arguments. More ellaborate explanation which explains line-wise the code can be found in the file as notes after each line.
