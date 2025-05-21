# Create a class that has the following functions:
class QuestionLoader():
    def __init__(self, file_name = "quiz_questions.txt"):
        self.file_name = file_name

    def load_questions(self):
        # Reads the quiz_questions file
        with open(self.file_name, "r") as file:
            lines = file.readlines()

        # Figure out the correct answer from the txt file
        questions = {}
        index = 0
        for i in range(0, len(lines), 7):
            if i + 6 >= len(lines): break
            question = lines[i].split("Question: ")[-1].strip()
            option_a = lines[i+1].split("A.) ")[-1].strip()
            option_b = lines[i+2].split("B.) ")[-1].strip()
            option_c = lines[i+3].split("C.) ")[-1].strip()
            option_d = lines[i+4].split("D.) ")[-1].strip()
            answer = lines[i+5].split("Answer: ")[-1].strip()
            questions[index] = {
                "question": question, "a": option_a, "b": option_b, "c": option_c, "d": option_d, "answer": answer
            }
            index += 1
        return questions
