# Import the class from the question_saver.py
from question_saver import QuestionSaver
import tkinter as tk
# Create a class that has the following functions:
class QuizCreator():
    # Can access the GUI(tkinter)
    def __init__(self):
        self.saver = QuestionSaver()
        self.base = tk.Tk()
        self.base.title("Quiz Creator")
        self.entries = {}
        self.status_label = None
        self.widgets()
        self.base.mainloop()

    # Create the widgets
    def widgets(self):
        fields = [("Enter Question here:", "Question"),
            ("Enter Option A here:", "A"),
            ("Enter Option B here:", "B"),
            ("Enter Option C here:", "C"),
            ("Enter Option D here:", "D"),
            ("Enter Correct Answer (A/B/C/D) here:", "Answer")]

        for label, key in fields:
            tk.Label(self.base, text=label).pack()
            entry = tk.Entry(self.base, width=50)
            entry.pack()
            self.entries[key] = entry

        tk.Button(self.base, text="Save Question", command=self.save).pack(pady=5)
        tk.Button(self.base, text="Exit", command=self.base.destroy).pack(pady=5)
        self.status_label = tk.Label(self.base, text="")
        self.status_label.pack()

    # Put the user inputs in the quiz_questions.txt
    def save(self):
        data = {key: entry.get() for key, entry in self.entries.items()}
        result = self.saver.save(data)
        if result == "success":
            for entry in self.entries.values():
                entry.delete(0, tk.END)
            self.status_label.config(text="Saved successfully!", fg="green")
        else:
            self.status_label.config(text=result, fg="red")