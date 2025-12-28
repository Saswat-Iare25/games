import tkinter as tk
from tkinter import messagebox
import random

choices = ["Rock", "Paper", "Scissors"]
user_history = {"Rock": 0, "Paper": 0, "Scissors": 0}

user_score = 0
ai_score = 0

def ai_choice():
    most_used = max(user_history, key=user_history.get)

    counter = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }

    if user_history[most_used] > 1:
        return counter[most_used]
    else:
        return random.choice(choices)

def play(user_pick):
    global user_score, ai_score

    user_history[user_pick] += 1
    ai_pick = ai_choice()

    result_text.set(f"You chose {user_pick}\nAI chose {ai_pick}")

    if user_pick == ai_pick:
        result = "It's a tie!"
    elif (
        (user_pick == "Rock" and ai_pick == "Scissors") or
        (user_pick == "Paper" and ai_pick == "Rock") or
        (user_pick == "Scissors" and ai_pick == "Paper")
    ):
        user_score += 1
        result = "You win!"
    else:
        ai_score += 1
        result = "I win!"

    score_text.set(f"Score  You: {user_score}  AI: {ai_score}")
    result_text.set(result_text.get() + "\n" + result)

def reset_game():
    global user_score, ai_score
    user_score = 0
    ai_score = 0

    for key in user_history:
        user_history[key] = 0

    result_text.set("Make your move!")
    score_text.set("Score  You: 0  AI: 0")

root = tk.Tk()
root.title("Rock Paper Scissors")

result_text = tk.StringVar(value="Make your move!")
score_text = tk.StringVar(value="Score  You: 0  AI: 0")

tk.Label(root, textvariable=result_text, font=("Arial", 14)).pack(pady=10)
tk.Label(root, textvariable=score_text, font=("Arial", 12)).pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for choice in choices:
    tk.Button(
        button_frame,
        text=choice,
        width=12,
        font=("Arial", 12),
        command=lambda c=choice: play(c)
    ).pack(side=tk.LEFT, padx=5)

tk.Button(
    root,
    text="Play Again",
    font=("Arial", 11),
    command=reset_game
).pack(pady=10)

root.mainloop()
