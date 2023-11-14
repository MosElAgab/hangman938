from milestone_2 import (build_words_list, choose_word, get_user_guess)


# Validate user guess function
def validate_user_guess(guess: str) -> bool:
    """
    Validate the user's guess.

    Parameters:
    - guess (str): The user's letter guess.

    Returns:
    - bool: True if the guess is valid, False otherwise.
    """
    if len(guess) == 1 and guess.isalpha():
        return True
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        return False


# check user guess data type and format vality fucntion
def check_guess(guess: str, chosen_word: str) -> None:
    """
    Check if the user's guess is in the chosen word and print the result.

    Parameters:
    - guess (str): The user's letter guess.
    - chosen_word (str): The word chosen for the game.

    Returns:
    - None
    """
    guess = guess.lower()
    chosen_word = chosen_word.lower()
    if guess in chosen_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input() -> bool:
    """
    Get a valid user guess, play a word-guessing game, and return the user's guess.

    The function continues prompting the user for a valid guess until one is provided.
    The game involves choosing a random word from a list, checking if the user's guess
    is in the chosen word, and providing feedback.

    Returns:
    - str: The user's valid letter guess.
    """
    
    while True:
        guess = get_user_guess()
        if validate_user_guess(guess):
            break
    word_list = build_words_list()
    chosen_word = choose_word(word_list)
    check_guess(guess, chosen_word)
    return guess



# tests
if __name__ == '__main__':
    ask_for_input()
