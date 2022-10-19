import random

word_list = ['apple','banana','pear','raspberry','strawberry']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Which letter will you guess? : ')

i = 0
while i != 1:
    if len(guess) == 1:
        if guess.isalpha() == True:
            print('Good guess!'); i += 1 
        else: print('Oops! That is not a valid input.'); guess = input('Try again : ')
    else: print('Oops! That is not a valid input.'); guess = input('Try again : ')