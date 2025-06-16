import random

def hangman():
    # Predefined list of words
    words = ['python', 'hangman', 'program', 'computer', 'keyboard']
    
    # Select a random word
    secret_word = random.choice(words)
    
    # Initialize game variables
    guessed_letters = []
    remaining_attempts = 6
    word_progress = ['_'] * len(secret_word)
    
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time. You have 6 incorrect attempts allowed.")
    print(' '.join(word_progress))
    
    while remaining_attempts > 0 and '_' in word_progress:
        # Get user input
        guess = input("\nEnter a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try another one.")
            continue
        
        guessed_letters.append(guess)
        
        # Check if guess is in the word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            # Update word progress
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    word_progress[i] = guess
        else:
            remaining_attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {remaining_attempts} attempts left.")
        
        # Display current progress
        print(' '.join(word_progress))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
    
    # Game over - check result
    if '_' not in word_progress:
        print("\nCongratulations! You guessed the word correctly!")
    else:
        print(f"\nGame over! You ran out of attempts. The word was: {secret_word}")

# Start the game
hangman()