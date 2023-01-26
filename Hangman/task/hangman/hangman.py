import random

GAME_NAME = "H A N G M A N"

list_of_words = ("python", "java", "swift", "javascript")

won = 0
lose = 0


def game():
    attempts = 8
    global won
    global lose
    secret_word = list(random.choice(list_of_words))
    hidden_word = list("-" * len(secret_word))
    guess_letters = set()
    guess_word = False

    while attempts > 0 and not guess_word:
        print("\n{0}".format("".join(hidden_word)))
        user_input = input("Input a letter: ")
        if len(user_input) == 1:
            if user_input.islower():
                if user_input not in guess_letters:
                    guess_letters.add(user_input)
                    if user_input in secret_word:
                        index = [i for i in range(len(secret_word)) if secret_word[i] == user_input]
                        for x in index:
                            hidden_word[x] = user_input
                        if "".join(hidden_word) == "".join(secret_word):
                            guess_word = True
                    else:
                        attempts -= 1
                        print("That letter doesn't appear in the word. # {0} attempts".format(attempts))
                else:
                    print("You've already guessed this letter.")
            else:
                print("Please, enter a lowercase letter from the English"
                      " alphabet.")
        else:
            print("Please, input a single letter.")

    if guess_word:
        print("You guessed the word {0}!".format("".join(secret_word)))
        print("You survived!")
        won += 1
    else:
        print("\nYou lost!")
        lose += 1


def main():
    print("{0}".format(GAME_NAME))
    while True:
        user_input = input('Type "play" to play the game,'
                           ' "results" to show the scoreboard, and'
                           ' "exit" to quit: ')
        if user_input == "play":
            game()
        elif user_input == "results":
            print("You won: {0} times.".format(won))
            print("You lost: {0} times".format(lose))
        elif user_input == "exit":
            break


main()
