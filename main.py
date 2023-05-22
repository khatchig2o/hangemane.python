import random

words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'frog', 'goat', 'horse', 'house', 'key', 'lion', 'monkey',
         'mouse', 'orange', 'pen', 'queen', 'robot', 'star', 'tree', 'umbrella', 'van', 'whale', 'x-ray', 'yoyo',
         'zebra']
word = ""
hidden_word = ""
tries = 0
limit = 6
used_letters = []


def get_word():
    global word, hidden_word
    word = random.choice(words)
    hidden_word = ['_'] * len(word)


def game():
    global tries
    get_word()
    while tries < limit:
        print("".join(hidden_word))
        user_guess = input("Guess a letter: ")
        if user_guess in used_letters:
            print("you have already tried this letter ")
            continue
        else:
            used_letters.append(user_guess)
        print(used_letters)
        if user_guess in word:
            for i in range(len(word)):
                if word[i] == user_guess:
                    hidden_word[i] = user_guess

        else:
            tries += 1
            print("you lost one of your tries and have " + str(limit - tries) + " left")
        if "".join(hidden_word) == word:
            print("congrats you won!")
            break
    if tries == limit:
        print("your out of moves Game over!")
    again()


def again():
    global word, hidden_word, tries, used_letters
    play_again = input("Would you like to play again? (y/n): ").lower()
    while play_again not in ["y", "n"]:
        print("Please enter y or n.")
        play_again = input("Would you like to play again? (y/n): ").lower()

    if play_again == "y":
        word = ""
        hidden_word = ""
        tries = 0
        used_letters = []
        game()
    else:
        print("Thank you for playing")
        return 0


if __name__ == '__main__':
    game()
