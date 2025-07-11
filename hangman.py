import random

def hangman():
    words = ['python', 'developer', 'challenge', 'dinosaur', 'gaming']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    tries = 6
    guessed_letters = set()

    print("Welcome to Hangman!")

    while tries > 0 and '_' in guessed:
        print('Word:', ' '.join(guessed))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct! 🎉")
        else:
            tries -= 1
            print(f"Wrong! You have {tries} tries left. 😬")

    if '_' not in guessed:
        print(f"Congrats! You guessed the word: {word}")
    else:
        print(f"You lost! The word was: {word}")

hangman()
