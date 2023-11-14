import random as r


def build_words_list(new_list=False, number_of_words=5):
    """
    Build a list of words.

    Parameters:
    - new_list (bool): If True, prompts the user to input new words. Default is False.
    - number_of_words (int): Number of words to input if new_list is True. Default is 5.

    Returns:
    - list: A list of words.
    """
    if new_list:
        word_list = []
        for i in range(number_of_words):
            new_word = input('Choese a word\n')
            word_list.append(new_word)
        return word_list
    else:
        word_list =['Mango', 'Banana', 'Apple', 'Kiwi', 'Pineapple']
        return word_list


def choose_word(word_list: list) -> str:
    """
    Choose a random word from the given list.

    Parameters:
    - word_list (list): List of words to choose from.

    Returns:
    - str: A randomly chosen word.
    """
    word = r.choice(word_list)
    return word


def get_user_guess():
    """
    Get a single letter as user input.

    Returns:
    - str: The user's letter guess.
    """
    guess = input('Choose a letter please?\n')
    return guess


def check_guess_validity(guess):
    """
    Check the validity of the user's guess.

    Parameters:
    - guess (str): The user's letter guess.

    Returns:
    - None: Prints a message indicating if the guess is valid or not.
    """
    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
    else:
        print("Oops! That is not a valid input.")

if __name__ == '__main__':
    # test 1
    word_list = build_words_list()
    print(word_list)
    word = choose_word(word_list)
    print(word)
    guess = get_user_guess()
    check_guess_validity(guess)

    # test 2
    print('____________________')
    word_list = build_words_list(new_list=True, number_of_words=4)
    print(word_list)
    word = choose_word(word_list)
    print(word)
    guess = get_user_guess()
    check_guess_validity(guess)