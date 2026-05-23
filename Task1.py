import random
words = ["python", "apple", "tiger", "house", "robot"]
word = random.choice(words)
guessed = ["_"] * len(word)
wrong = 0
print("=== Hangman Game ===")
while wrong < 6 and "_" in guessed:
    print("\n", " ".join(guessed))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        wrong += 1
        print("Wrong! Attempts left:", 6 - wrong)

if "_" not in guessed:
    print("\n🎉 You Won! Word is:", word)
else:
    print("\n❌ Game Over! Word was:", word)