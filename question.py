#Desmond Ho | A01266785
# Feb 2, 2022
import random
import math
class Question:
    """[question class, resposnible for printing out the questions and keeping
        track of answers]

        Args:
            question (str): [the question text]
            correct_answer (str): [the correct answer]
            incorrect_answers (list): [the incorrect answer (3 of them)]
            category (str, optional): [the category of question]. Defaults to None.
            difficulty (str, optional): [the difficulty of the question]. Defaults to None.

        Raises:
            AttributeError: [if the difficulty is not in ths list]
        """        
    def __init__(self, question: str, correct_answer:str, incorrect_answers: list, category:str= None, difficulty:str =None):
        
        self.question = question
        self.category = category
        if difficulty not in ['easy', 'medium', 'hard'] and difficulty != None:
            raise AttributeError
        else:
            self.difficulty = difficulty
        '''list of answers'''
        self.answers =  []
        self.answers.append(correct_answer)
        for i in incorrect_answers:
            self.answers.append(i)
        '''shuffle list'''
        random.shuffle(self.answers)

        '''answer id attribute, and a correct answer attribute that is used in the game.py program'''
        self.answer_id = self.answers.index(correct_answer) + 1
        self.correct_answer = self.answers[(self.answer_id -1)]

    
    def __str__(self):
        '''__str__ dunder method, same as as_string

        Args:
            None
        
        Returns:
            str
        
        '''
        temp_list = ['']
        temp_list[0] += self.question 
        for x, answer in enumerate(self.answers):
            temp_list[0] += f'\n{x+1}. {answer}'
            pass
        return temp_list[0]

    def get_score(self, time_taken: int) -> int:
        
        '''get_score function, calculates score based on time

        Args:
            time_taken(int): the amount of time taken
        
        Returns:
            score (int): the score
        
        '''
        dict = {'easy':1, 'medium': 2, 'hard': 3}
        if time_taken > 5:
            return math.floor(10 * dict[self.difficulty])
        elif time_taken < 5:
            return math.floor(dict[self.difficulty] * (225/time_taken - 7 * time_taken))


