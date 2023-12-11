import tkinter as tk
from tkinter import messagebox
import random

class CardGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Карточная игра")

        self.cards = []
        self.points = 0

        self.label_score = tk.Label(root, text="Очки: 0", font=("Helvetica", 12))
        self.label_score.pack(pady=10)

        self.label_cards = tk.Label(root, text="Список карт:", font=("Helvetica", 12))
        self.label_cards.pack()

        self.cards_listbox = tk.Listbox(root, height=5, width=30)
        self.cards_listbox.pack()

        self.start_button = tk.Button(root, text="Начать игру", command=self.start_game)
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Сбросить руку", command=self.reset_hand, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

    def start_game(self):
        if self.start_button["text"] == "Начать игру":
            self.cards = [random.randint(1, 11) for _ in range(2)]
            self.points = sum(self.cards)
            self.update_ui()
            self.start_button["text"] = "Взять карту"
            self.reset_button["state"] = tk.NORMAL
        else:
            new_card = random.randint(1, 11)
            self.cards.append(new_card)
            self.points += new_card
            self.update_ui()

    def reset_hand(self):
        self.cards = []
        self.points = 0
        self.update_ui()
        self.start_button["text"] = "Начать игру"
        self.reset_button["state"] = tk.DISABLED

    def update_ui(self):
        cards_str = ", ".join(map(str, self.cards))
        self.label_cards.config(text=f"Список карт: {cards_str}")
        self.label_score.config(text=f"Очки: {self.points}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CardGameApp(root)
    root.mainloop()
