# Import the class from question_loader.py
from question_loader import QuestionLoader
import tkinter as tk
import random
# Create a class that has the following functions:
class QuizTaker():
    def __init__(self):
        self.loader = QuestionLoader()
        self.questions = self.loader.load_questions()
        self.order = list(self.questions.keys())
        random.shuffle(self.order)

        self.index = 0
        self.score = 0

        self.base = tk.Tk()
        self.base.title("Quiz Taker")
        self.widgets()
        self.load_question()
        self.base.mainloop()

    # Create the widgets that can interact with te user
    def widgets(self):
        self.question_label = tk.Label(self.base, wraplength=800)
        self.question_label.pack(pady=10)

        self.option_labels = []
        for _ in range(4):
            label = tk.Label(self.base, wraplength=800)
            label.pack()
            self.option_labels.append(label)

        self.feedback = tk.Label(self.base, wraplength=800)
        self.feedback.pack(pady=10)

        self.buttons = []
        frame = tk.Frame(self.base)
        frame.pack()
        for i, opt in enumerate("ABCD"):
            btn = tk.Button(frame, text=opt, command=lambda o=opt: self.check_answer(o))
            btn.pack(side="left", padx=5)
            self.buttons.append(btn)

        self.next_button = tk.Button(self.base, text="Next", command=self.next_question)
        self.restart_button = tk.Button(self.base, text="Restart", command=self.restart)
        tk.Button(self.base, text="Exit", command=self.base.destroy).pack(pady=5)

    def load_question(self):
        if self.index >= len(self.order):
            self.question_label.config(text="Quiz is Over!")
            for i, lbl in enumerate(self.option_labels):
                lbl.config(text=["You scored", str(self.score), "out of", str(len(self.order))][i])
            self.feedback.config(text="Press Restart or Exit")
            for btn in self.buttons:
                btn.config(state="disabled")
            self.restart_button.pack(pady=5)
            return

        qdata = self.questions[self.order[self.index]]
        self.question_label.config(text=qdata["question"])
        for i, key in enumerate("ABCD"):
            self.option_labels[i].config(text=f"{key}.) {qdata[key.lower()]}")

    
    # Takes track of the score of the user
    def check_answer(self, user_answer):
        correct = self.questions[self.order[self.index]]["answer"]
        if user_answer == correct:
            self.feedback.config(text="Correct!")
            self.score += 1
        else:
            self.feedback.config(text="Wrong!")

        for btn in self.buttons:
            btn.config(state="disabled")
        self.next_button.pack(pady=5)

    # Progresses on the questions randomly
    def next_question(self):
        self.index += 1
        self.feedback.config(text="")
        for btn in self.buttons:
            btn.config(state="normal")
        self.next_button.pack_forget()
        self.load_question()

    def restart(self):
        random.shuffle(self.order)
        self.index = 0
        self.score = 0
        for btn in self.buttons:
            btn.config(state="normal")
        self.restart_button.pack_forget()
        self.load_question()
