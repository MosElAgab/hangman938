import random as r


word_list =['Mango', 'Banana', 'Apple', 'Kiwi', 'Pineapple']
print(word_list)

word = r.choice(word_list)
print(word)

guess = input('Choose a letter please?\n')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print("Oops! That is not a valid input.")
