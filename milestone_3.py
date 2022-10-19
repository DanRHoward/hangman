word = 'pear'

def guess_check(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! "{guess}" is in the word.')
    else:
        print(f'Sorry, "{guess}" is not in the word. Try again.')
    return 

def ask_for_input():
    while True:
        guess = input('Guess is single letter! : ')
        if len(guess) == 1:
            if guess.isalpha() == True:
                print('Good guess!')
                break
            else: print('Invalid letter. Please, enter a single alphabetical character.')
        else: print('Invalid letter. Please, enter a single alphabetical character.')
    guess_check(guess)

ask_for_input()