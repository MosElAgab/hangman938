import random as r


# game class
class Hangman:
    """
    A class representing a simple Hangman game.

    Attributes:
    - word_list (list): A list of words to choose from.
    - num_lives (int): The number of lives the player has. Default is 5.
    - word_guessed (list): A list representing the current state of guessed letters in the word.
    - num_letters (int): The number of unique letters in the chosen word.
    - list_of_guesses (list): A list of letters that have been guessed.

    Methods:
    - __init__(self, word_list, num_lives=5): Initialize the Hangman game.
    - ask_for_input(self): Prompt the user for a letter guess and update the game state accordingly.
    """
    word_list: list
    num_lives: int
    __word: str
    word_guessed: list
    num_letters: int
    list_of_guesses: list

    def __init__(self, word_list, num_lives = 5) -> None:
        """
        Initialize the Hangman game.

        Parameters:
        - word_list (list): A list of words to choose from.
        - num_lives (int): The number of lives the player has. Default is 5.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.__word = r.choice(word_list).lower()
        self.word_guessed = ['_' for _ in range(len(self.__word))]
        self.num_letters = len(set([letter for letter in self.__word]))
        self.list_of_guesses = []

    def __check_guess(self, guess):
        """
        Check if the guessed letter is in the word and update the game state.

        Parameters:
        - guess (str): The guessed letter.

        Returns:
        - None
        """
        guess = guess.lower()
        if guess in self.__word.lower():
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.__word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} left")

        
    
    def ask_for_input(self):
        """
        Prompt the user for a letter guess and update the game state accordingly.

        Returns:
        - None
        """
        while True:
            guess = input('Choose a letter please?\n')
            if not guess.isalpha() or not len(guess) == 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.__check_guess(guess)
                self.list_of_guesses.append(guess)
                if self.num_lives < 1:
                    print("Game over :(")
                    break
                elif '_' not in self.word_guessed:
                    print(f'Fantastic, you guessed {self.__word} correctly!! :)')
                    break
                
# function to run the game 
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    game.ask_for_input()

# if __name__ == '__main__':
#     play_game((['Mango', 'Banana', 'Apple', 'Kiwi', 'Pineapple']))