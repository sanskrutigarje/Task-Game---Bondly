import tkinter as tk
import random
remaining_tasks = []
from tkinter import PhotoImage
from tasks import family_tasks, sisters_tasks, friends_tasks, couples_tasks

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Task Game")
root.geometry("500x400")
root.configure(bg="#d08ab4")

players = ["Player 1", "Player 2"]
current_player_index = 0

bg_image = PhotoImage(file="bg.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


current_tasks = []

# ---------------- FUNCTIONS ----------------
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def next_player():
    global current_player_index
    current_player_index = (current_player_index + 1) % len(players)


def show_home():
    clear_screen()

    title = tk.Label(
        root,
        text="Roll the Moment 🎲",
        font=("Helvetica", 22, "bold"),
        #fg="white",
        #bg="#9393c4"
    )
    title.pack(pady=30)

    create_button("Family", family_tasks)
    create_button("Sisters", sisters_tasks)
    create_button("Friends", friends_tasks)
    create_button("Couples", couples_tasks)

def create_button(text, task_list):
    btn = tk.Button(
        root,
        text=text,
        font=("Helvetica", 14),
        width=20,
        height=2,
        bg="#a533ec",
        fg="white",
        command=lambda: start_game(task_list)
    )
    btn.pack(pady=8)

def start_game(tasks):
    global current_tasks, remaining_tasks
    current_tasks = tasks
    remaining_tasks = tasks.copy()  # fresh copy
    show_game_page()

def show_game_page():
    clear_screen()

    global current_player_index

    title = tk.Label(
        root,
        text="🎲 Roll the Dice 🎲",
        font=("Helvetica", 18, "bold"),
        fg="white",
        bg="#000000"
    )
    title.pack(pady=10)

    player_label = tk.Label(
        root,
        text=f"Turn: {players[current_player_index]}",
        font=("Helvetica", 14, "bold"),
        fg="#ffcc00",
        bg="#000000"
    )
    player_label.pack(pady=5)

    dice_label = tk.Label(
        root,
        text="🎲",
        font=("Helvetica", 50),
        fg="white",
        bg="#000000"
    )
    dice_label.pack(pady=10)

    task_text = tk.Label(
        root,
        text="",
        font=("Helvetica", 14),
        wraplength=400,
        fg="white",
        bg="#000000"
    )
    task_text.pack(pady=20)

    def dice_animation(count=12):
        if count > 0:
            dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
            dice_label.config(text=random.choice(dice_faces))
            root.after(100, dice_animation, count - 1)
        else:
            task_text.config(text=random.choice(current_tasks))
            next_player()
            player_label.config(text=f"Turn: {players[current_player_index]}")

    roll_btn = tk.Button(
        root,
        text="ROLL 🎲",
        font=("Helvetica", 16, "bold"),
        bg="#ff6584",
        fg="white",
        width=12,
        height=2,
        command=dice_animation
    )
    roll_btn.pack(pady=10)

    back_btn = tk.Button(
        root,
        text="⬅ Back",
        command=show_home
    )
    back_btn.pack(pady=10)

# ---------------- START ----------------
show_home()
root.mainloop()
