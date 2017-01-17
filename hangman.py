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
    sentence += " Please take a guess."
    print(sentence)

prompt_user(word)
