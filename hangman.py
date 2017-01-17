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

def verify_answer(guess, word, previous_answer):
    sentence = "You guess is: "
    sentence += guess
    print(sentence)

    print("The word is: ")
    result = previous_answer
    for index in range(len(word)):
        if guess.lower() == word[index].lower():
            result[index] = guess
            life = 0 #indicate that the answer is right and no life will be taken

    life = -1 #wrong answer, take 1 life

    print(result)
    return (life, result)

def prepare_answer(word):
    answer = []
    for index in range(len(word)):
        answer.append("_")

    return answer

def hangman():
    lives = 10
    word = "Apple"
    print("Welcome!")

    while lives > 0:
        prompt_user(word, lives)
        guess = input("Please take a guess.\n")
        (life, result) = verify_answer(guess, word, answer)

        if "_" in result:
             # still haven't got the word, continue
             answer = result
             lives += life
             continue
        else:
            print("You won! The word is: " + word)

hangman()
