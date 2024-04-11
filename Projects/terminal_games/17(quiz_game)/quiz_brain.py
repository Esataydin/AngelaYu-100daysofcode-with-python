from question_model import Question


class QuizBrain:

    def __init__(self, q_list: list[Question]):
        self.question_number: int = 0
        self.score: int = 0
        self.question_list: list[Question] = q_list

    def still_has_questions(self) -> bool:
        """Returns True until there is no question left"""
        return self.question_number < len(self.question_list)

    def next_question(self) -> None:
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
