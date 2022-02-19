import question_library as q
import question as qs
import time


class Game:
    def __init__(self):
        self.question_lib_instance = q.QuestionLibrary()
        for x, y in enumerate(self.question_lib_instance.get_categories()):
            print(f"{x+1}.'{y}'")
            pass
        self.category = input("Enter a category: ")
        self.difficulty = input("Enter a difficulty (easy, medium, hard): ")
        self.num = input("Enter the amount of questions you want: ")

        if self.category == "":
            self.category = None
        if self.difficulty not in ["easy", "medium", "hard"]:
            self.difficulty = None
        if self.num == "":
            self.num = None
        else:
            while not (self.num.isnumeric):
                if int(self.num <= 0):
                    self.num = input("Please enter a Number!: ")
                else:
                    self.num = input("Please enter a Number!")
            self.num = int(self.num)

        self.questions = self.question_lib_instance.get_questions(
            self.category, self.difficulty, self.num
        )

    def play(self):
        correct = 0
        total_score = 0
        for x in self.questions:
            print("<---------------------------------------------------------->")
            start = time.time()
            print(x)
            user_answer = input("Your Answer (1, 2, 3, 4): ")
            """checks if user input is a number and if its 1, 2, 3, or 4"""
            while True:
                try:

                    int(user_answer)
                    if user_answer not in ["1", "2", "3", "4"]:
                        user_answer = int(input("Answer must be 1, 2, 3 or 4 BOZO!: "))
                    break
                except ValueError:
                    user_answer = input("Please enter a Number!! ")

            """checks if user input is the correct answer"""
            if int(user_answer) != int(x.answer_id):
                print(
                    f"YOU GOT IT WRONG LOSER! \U0001F923, The correct answer is {x.answer_id}: {x.correct_answer}"
                )
            else:
                print("GOOD JOB \U0001f600")
                correct += 1
                end = time.time()
                total_score += x.get_score(end - start)
                print(
                    f"You scored: {x.get_score(end-start)} points for this question!!"
                )

        """prints info after all questions have been answered, displays user score"""
        print(
            f"You got {correct} answers correct out of {len(self.questions)}, you final grade is {round(((correct/len(self.questions))*100), 2)}%."
        )
        print(f"Time Weighted Score: {total_score}")


a = Game()
a.play()
