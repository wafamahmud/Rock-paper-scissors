import tkinter as tk
import random

root = tk.Tk()
root.title("Rock, paper, scissor App")
root.geometry("400x400")

choices = ["Rock", "Paper", "Scissors"]

label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12))
label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

def play(user_choice):
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        winner = f"Tie! You chose {user_choice}, Computer chose {computer_choice}"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        winner = f"You Win! {user_choice} beats {computer_choice}"
    else:
        winner = f"You Lose! {computer_choice} beats {user_choice}"
    
    result_label.config(text=winner)

tk.Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

root.mainloop()