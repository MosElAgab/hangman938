import random as r

class Hangman:
    word_list: list
    num_list: int
    word_guessed: list
    num_letters: int
    list_of_guesses: list

    def __init__(self, word_list, num_lives = 5) -> None:
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = r.choice(word_list).lower()
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set([letter for letter in self.word]))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            print('word guessed', self.word_guessed)
            self.num_letters -= 1
            print(self.num_letters)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} left")

        
    
    def ask_for_input(self):
        while True:
            guess = input('Choose a letter please?\n')
            if not guess.isalpha() or not len(guess) == 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print('list of guesses', self.list_of_guesses)
                if self.num_lives < 1:
                    print("Game over :(")
                    break
                elif '_' not in self.word_guessed:
                    print(f'Fantastic, you guessed {self.word} correctly!! :)')
                    break
                



# if __name__ == '__main__':
#     x = Hangman(['Mango', 'Banana', 'Apple', 'Kiwi', 'Pineapple'])
#     print(x.word_list)
#     print(x.num_lives)
#     print(x.word)
#     print(x.word_guessed)
#     print(x.num_letters)
#     print(x.list_of_guesses)


if __name__ == '__main__':
    x = Hangman(['Mango', 'Banana', 'Apple', 'Kiwi', 'Pineapple'])
    print(x.word)
    x.ask_for_input()
    # print(x.list_of_guesses)