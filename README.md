Python Word Guessing Game
A simple, interactive terminal-based game where players guess missing characters to complete words. This project demonstrates the use of Python loops, list manipulation, and the zip() function.

📋 Features
Interactive Menu: Simple navigation to start or exit the game.

Limited Attempts: Players get 3 attempts per word to guess the correct missing character.

Dynamic Feedback: The game reveals the full word once a correct guess is made.

Score Tracking: Displays the total number of correct and wrong answers at the end of each round.

🎮 How to Play
Run the script: Execute the Python file in your terminal.

Select Start: Enter 1 to begin the game.

Guess the Character: You will see a word with a missing letter (e.g., H_t).

Input your guess: Type the single character you think completes the word.

Win/Loss: If you guess correctly within 3 tries, you move to the next word. If you fail all 3 tries, the correct answer is revealed, and it counts as a wrong guess.

🛠️ Logic Overview
The game uses three main lists to manage the data:

list1: Contains the words with underscores (placeholders).

list2: Contains the corresponding correct characters.

list3: Created using list(zip(list1, list2)) to pair the challenges with their solutions.

🚀 Getting Started
Prerequisites
Python 3.x installed on your machine.

Installation
Clone this repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
Navigate to the directory:

Bash

cd your-repo-name
Run the game:

Bash

python game_filename.py
