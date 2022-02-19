# Desmond Ho | A01266785
# Feb 2, 2022
import json
import random
import question as quest


class QuestionLibrary:
    """[question library class]"""

    def __init__(self, filename="trivia.json"):
        self.filename = filename

        self.questions = []
        f = open(self.filename)
        data = json.load(f)

        for question in data:
            self.questions.append(
                quest.Question(
                    question["question"],
                    question["correct_answer"],
                    question["incorrect_answers"],
                    question["category"],
                    question["difficulty"],
                )
            )
        f.close()

    def get_questions(
        self, category: str = None, difficulty: str = None, num: int = None
    ):
        """[summary]

        Args:
            category (str, optional): [description]. Defaults to None.
            difficulty (str, optional): [description]. Defaults to None.
            num (int, optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        self.num = num
        self.category = category
        if difficulty not in ["easy", "medium", "hard"]:
            self.difficulty = None
        else:
            self.difficulty = difficulty
        difficulties = []
        categories = []
        for i in self.questions:
            if i.category not in categories:
                categories.append(i.category)
            if i.difficulty not in difficulties:
                difficulties.append(i.difficulty)

        if len(categories) <= len(difficulties):
            for i in self.questions:
                if category == None and difficulty != None:
                    if i.difficulty == self.difficulty:
                        self.category = i.category
                elif category != None and difficulty == None:
                    self.category = category
                    if i.category == self.category:
                        self.difficulty = i.difficulty

        else:
            if category == None:
                self.category = categories[random.randint(0, len(categories)) - 1]
            else:
                self.category = category
            if difficulty == None:
                self.difficulty = difficulties[random.randint(0, len(difficulties) - 1)]
            else:
                self.difficulty = difficulty

        """logic for num, if parameter = None
            it will assign catergory to a random one from the list"""

        """getting the questions based on the above values"""
        self.filtered_questions = []

        for i in self.questions:
            # lol
            if i.category == self.category and i.difficulty == self.difficulty:
                self.filtered_questions.append(i)

        if (
            self.category == None
            and self.difficulty == None
            and len(categories) <= len(difficulties)
        ):
            for i in self.questions:
                self.filtered_questions.append(i)
            self.num = len(self.filtered_questions)
        else:
            if num == None:
                self.num = random.randint(1, len(self.filtered_questions))
            else:
                self.num = num

        if self.num == 1:
            return [random.choice(self.filtered_questions)]
        else:
            random.sample(self.filtered_questions, k=self.num)
            return random.sample(self.filtered_questions, k=self.num)

    def get_categories(self) -> list:
        """[summary]

        Returns:
            list: [list of categories unique]
        """ """"""
        categories = []
        for i in self.questions:
            if i.category not in categories:
                categories.append(i.category)
        return categories

    def __len__(self):
        return len(self.questions)
