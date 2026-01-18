# 🧩 Hangman Game

A lightweight, interactive terminal-based game written in Python. Players are challenged to guess the missing letters in a series of words within a limited number of attempts.

---

## 🚀 Features
* **Three Strikes Rule:** You get exactly 3 attempts per word.
* **Live Feedback:** Tells you if your guess is right or wrong instantly.
* **Automatic Scorecard:** Summarizes your performance (Correct vs. Wrong) at the end.
* **Clean Loop:** Play as many rounds as you want or exit gracefully.

---

## 🛠️ How It Works

The game uses a **Zip** logic to pair hidden words with their answers:

1.  **Word List:** `["H_t", "c_t", "r_d", "p_rk"]`
2.  **Answer List:** `["o", "a", "e", "a"]`
3.  **The Logic:** The script zips these together so the program knows exactly which character completes which word.



---

## 🎮 How to Run

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/A-P08/Hangman-game.git
    ```
2.  **Run the Script:**
    ```bash
    python game.py
    ```
3.  **Input:** When prompted, enter `1` to start. Type your character guesses in lowercase.

---

## 📝 Example Gameplay
```text
1. 'H_t' :
your answer player1: o
Right guess! The word is 'Hot'
