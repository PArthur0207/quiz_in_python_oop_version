# Import the classes from the creator app and the taker app
import tkinter as tk
from creator_app import QuizCreator
from taker_app import QuizTaker

# Create a class that Uses tkinter to ask the user wether to run the creator_app or the taker_app
class MainLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz App Launcher")
        self.root.geometry("300x150")

        label = tk.Label(self.root, text="Choose an option:", font=("Arial", 14))
        label.pack(pady=10)

        # Click to run quiz creator
        btn_create = tk.Button(self.root, text="Create Quiz", width=20, command=self.open_creator)
        btn_create.pack(pady=5)

        # Click to run quiz taker
        btn_take = tk.Button(self.root, text="Take Quiz", width=20, command=self.open_taker)
        btn_take.pack(pady=5)

        self.root.mainloop()

    def open_creator(self):
        self.root.destroy()  # Close launcher
        QuizCreator()        # Launch Creator GUI

    def open_taker(self):
        self.root.destroy()  # Close launcher
        QuizTaker()         # Launch Taker GUI

if __name__ == "__main__":
    MainLauncher()

# Run this file