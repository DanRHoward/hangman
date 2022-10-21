class Hangman: #Defining class named 'Hangman'
    def __init__(self,word_list,num_lives=5): #Establish initial state of the game
        self.word_list = word_list 
        self.num_lives = num_lives
        
        import random #Import 'random' package
        self.word = random.choice(self.word_list) #Random element from list
        self.word_guessed = ['_']*len(self.word) #List of elements, '_', of times the number of characters of randomly chosen word
        self.num_letters = len(set(self.word)) #'Set' command collapses lists to only unique elements
        self.list_of_guesses = [] #Initial lists of attempts is naturally empty
    
    def check_guess(self,guess): #Defining method named check_guess
        guess = guess.lower() #Setting all characters to lowercase
        if guess in self.word: #Criterea if guess is in our word
            print(f'Good guess! "{guess}" is in the word.')
            for i in range(len(self.word)): #'range' command to create interval for i
                if guess == self.word[i]: #Checking each character is they are the same
                    self.word_guessed[i] = guess #Redefinning empty spaces with correctly guessed letter
            print(self.word_guessed)
            self.num_letters -= 1 #Reducing its value by 1
        else:
            self.num_lives -= 1 #Reducing its value by 1
            print(f'Sorry, "{guess}" is not in the word.')
            if self.num_lives == 1:
                print(f'You have {self.num_lives} life left.')
            else:
                print(f'You have {self.num_lives} lives left.')
        self.list_of_guesses.append(guess) #Concatinating list_of_quesses with out new guess 
    
    def ask_for_input(self): #Defining method named ask_for_input
        while True: #Creating infinite loop
            guess = input('Guess a single alphabetical letter! : ')
            if len(guess) != 1 or guess.isalpha() == False: #Either/or criterea for 'if' command
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses: #Elif allows for other criterea
                print('You already tried that letter!')
            else:
                self.check_guess(guess) #Perform check_guess method found in same (self) class
            break #To break infinite loop
                
def play_game(): #Defining game logic
    word_list = ['apple','grape','mango','guava','lemon'] #Our defined list of possible words
    game = Hangman(word_list,num_lives=5) #Instance of Hangman class
    while True: #To create infinite loop
        if game.num_lives == 0:
            print('You lost!')
            break #To break the infinite looping
        elif game.num_letters > 0:
            game.ask_for_input() #To initialise next move in the game
        else:
            print('CONGRATULATIONS!!! You have won the game.')
            print(f'The correct answer is {game.word}.')
            break #To break infinite looping

play_game() #To start the game