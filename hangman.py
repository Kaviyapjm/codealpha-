import random

# Predefined word list
word_list = ["python", "tiger", "robot", "chair", "plant"]

# Randomly select a word
secret_word = random.choice(word_list)
guessed_letters = []
tries_left = 6

# Display welcome
print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {tries_left} incorrect attempts.\n")

display_word = ["_" for _ in secret_word]

# Game loop
while tries_left > 0 and "_" in display_word:
    print("Word: ", " ".join(display_word))
    print("Guessed letters: ", " ".join(guessed_letters))
    guess = input("🔤 Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet only.\n")
        continue

    if guess in guessed_letters:
        print("⛔ Already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("✅ Good guess!\n")
    else:
        tries_left -= 1
        print(f"❌ Wrong guess. Tries left: {tries_left}\n")

# Game over messages
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Out of attempts! The word was:", secret_word)
