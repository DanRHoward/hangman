import random

word_list = ['apple','banana','pear','raspberry','strawberry']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Which letter will you guess? : ')