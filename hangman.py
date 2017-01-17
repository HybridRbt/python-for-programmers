# Hangman

lives = 10
word = "Apple"

def prompt_user(word):
    sentence = "Welcome! The word has "
    word_len = len(word)
    sentence += str(word_len)

    if word_len == 1:
        sentence += " character."
    else:
        sentence += " characters."

    print(sentence)

def verify_answer(guess):
    sentence = "You guess is: "
    sentence += guess
    print(sentence)

prompt_user(word)
guess = input("Please take a guess.\n")
verify_answer(guess.lower())
