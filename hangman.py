# Hangman

def prompt_user(word, lives):
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
            life = 0 #indicate that the answer is right and no life will be taken
        else:
            result += "_ "
            life = -1 #wrong answer, take 1 life
    print(result)
    return (life, result)

def hangman():
    lives = 10
    word = "Apple"
    print("Welcome!")

    while lives > 0:
        prompt_user(word, lives)
        guess = input("Please take a guess.\n")
        (life, result) = verify_answer(guess.lower(), word)
        if "_" in result:
             # still haven't got the word, continue
            lives += life
        else:
            print("You won! The word is: " + word)

hangman()
