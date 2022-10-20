class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        
        import random
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! "{guess}" is in the word.')
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, "{guess}" is not in the word.')
            print(f'You have {self.num_lives} lives left.')
        self.list_of_guesses.append(guess)
    
    def ask_for_input(self):
        while True:
            guess = input('Guess a single alphabetical letter! : ')
            if len(guess) != 1 or guess.isalpha() == False:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                
Hangman(['pear','apple','grape','plum','mango','date','guava','lime']).ask_for_input()