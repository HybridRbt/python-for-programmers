# Hangman

lives = 10
word = "Apple"

def prompt_user(word, lives):
    sentence = "Welcome! The word has "
    word_len = len(word)
    sentence += str(word_len)

    if word_len == 1:
        sentence += " character."
    else:
        sentence += " characters."

    sentence += "\nYou have " + str(lives) + " lives left."
    print(sentence)

def verify_answer(guess, word):
    sentence = "You guess is: "
    sentence += guess
    print(sentence)

    result = "The word is: "
    for character in word:
        if guess == character:
            result += guess + " "
        else:
            result += "_ "
    print(result)


prompt_user(word, lives)
guess = input("Please take a guess.\n")
verify_answer(guess.lower(), word)
