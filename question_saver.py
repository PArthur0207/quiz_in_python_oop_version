# Create a class that has the following functions:
class QuestionSaver():
    def __init__(self, file_name = "quiz_questions.txt"):
        self.file_name = file_name

    # Check if the returned values are valid and completed
    def save(self, data):
        answer = data['Answer'].upper()
        if not all(data.values()):
            return "Please input all that is necessary"
        if answer not in ['A', 'B', 'C', 'D']:
            return "Answer must be A, B, C, or D"

        # Append the questions to be put into the text file
        with open(self.file_name, "a") as f:
            f.write(f"Question: {data['Question']}\n")
            f.write(f"A.) {data['A']}\n")
            f.write(f"B.) {data['B']}\n")
            f.write(f"C.) {data['C']}\n")
            f.write(f"D.) {data['D']}\n")
            f.write(f"Answer: {answer}\n")
            f.write("------------------------\n")
        return "success"