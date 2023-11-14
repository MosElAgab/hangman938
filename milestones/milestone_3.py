from milestone_2 import (build_words_list, choose_word, get_user_guess)

# guess = get_user_guess()
# print(guess)

def validate_user_guess(guess):
    if len(guess) == 1 and guess.isalpha():
        return True
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        return False

def check_guess(guess: str, chosen_word: str) -> None:
    guess = guess.lower()
    chosen_word = chosen_word.lower()
    if guess in chosen_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input() -> bool:
    while True:
        guess = get_user_guess()
        if validate_user_guess(guess):
            break
    word_list = build_words_list()
    chosen_word = choose_word(word_list)
    print(chosen_word)
    check_guess(guess, chosen_word)
    return guess



# tests
if __name__ == '__main__':
    ask_for_input()
