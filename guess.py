import random

def choose_word():
   words = ["python", "programming", "challenge", "guess", "word",
"game", "exhibition", "gallery",  "interval",  "image", "ADMISSION",
"MATCH",  "EXAMINATION", "present", "New Year", "holiday",  "operate",
"injure", "guide",  "culture", "terminal",  "museum", "reception",
"demonstrate", "maintain", "manage",  "consultant" , "experience",  "assistant",
"meetings", " organise ", "efficiency",  "patience", "analysed ", "information ",
"university",   "strengths", "business plan",  "broadband"," download", "hyperlink",
"HARDWARE", " CURSOR ", ]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Welcome to the Word Guessing Game!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 9

    while attempts > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word:", current_display)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

        if set(guessed_letters) >= set(word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if attempts == 0:
        print("Sorry, you've run out of attempts. The correct word was:", word_to_guess)

if __name__ == "__main__":
    main()
