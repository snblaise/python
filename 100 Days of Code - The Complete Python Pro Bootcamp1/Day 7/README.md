# Building a Hangman Game: Day 7 of 100 Days of Python Code

Today marked an exciting milestone in my Python journey with Angela Yu's 100 Days of Code bootcamp. We built a complete Hangman game from scratch, implementing core programming concepts in a fun and practical way.

## GitHub Repository
🔗 Check out the complete project code on GitHub: [DAY 7- PROJECT](https://github.com/snblaise/python/tree/main/100%20Days%20of%20Code%20-%20The%20Complete%20Python%20Pro%20Bootcamp1/Day%207)

## Project Overview

The Hangman project was broken down into multiple steps, making it easier to understand and implement complex game logic. We created a classic word-guessing game where players try to guess a hidden word one letter at a time.

## Key Technical Concepts

### 1. Word Selection and Initialization
- Used Python's `random` module for word selection
- Implemented word lists in separate modules for better code organization
- Created dynamic placeholder system using underscores

### 2. Game Logic Implementation
```python
# Code snippet showing core game mechanics
import random
chosen_word = random.choice(word_list)
lives = 6
display = []
for position in range(word_length):
    display += "_"
```

### 3. User Input Handling
- Input validation and case normalization
- Duplicate guess detection
- Life management system

### 4. Advanced Features
- ASCII art integration for visual feedback
- Lives counter display
- Game state management
- Win/lose condition checking

## Code Architecture

The project was structured into multiple modules:
1. `main.py` - Core game logic
2. `hangman_words.py` - Word database
3. `hangman_art.py` - ASCII art and visual elements

## Key Learning Points

1. **Modular Programming**
   - Separating concerns into different files
   - Code organization and maintenance

2. **String Manipulation**
   - Converting strings to lists and back
   - Character-by-character processing

3. **Control Flow**
   - While loops for game continuation
   - Conditional statements for game logic
   - Loop control with boolean flags

4. **List Operations**
   - Dynamic list updates
   - List comprehension
   - Index-based operations

## Technical Challenges Overcome

1. Implementing the lives system
2. Managing displayed word updates
3. Handling repeated guesses
4. Creating user-friendly feedback

## Code Example: Game State Management
```python
while not game_over:
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        
    # Update display and check win/lose conditions
    if "_" not in display:
        game_over = True
        print("You Win!")
```

## Project Highlights

- **User Experience**: Clear feedback messages
- **Error Handling**: Graceful handling of invalid inputs
- **Visual Elements**: ASCII art integration
- **Game Logic**: Robust win/lose conditions

## Future Improvements

1. Adding difficulty levels
2. Implementing score tracking
3. Creating a word category system
4. Adding multiplayer functionality

## Conclusion

Day 7 was a significant milestone in my Python journey. Building the Hangman game helped solidify important programming concepts while creating something fun and interactive. The project demonstrated how breaking down a complex problem into smaller, manageable steps can lead to a successful implementation.

#Python #Programming #100DaysOfCode #GameDevelopment #CodingJourney
