from data import question_data     

class Question:
    def __init__(self,text,ans):
        self.text = text
        self.ans = ans
        # print(self.text)
        # print(self.ans)

class QuizzBrain:
    def __init__(self,q_list):
        self.q_list = q_list
        self.score = 0
        self.question_number=0

    def check_ans(self,choice):
        if choice == self.current_question.ans.lower():
            self.score+=1
            print(f'You got it right!!!! \ncurrent score is {self.score}/10 \n\n' )
            return self.score
        else:
            print(f'correct answer is {self.current_question.ans} \ncurrent score is {self.score}/10 \n\n')
            return self.score
    def next_question(self):
        for i in self.q_list:
            self.current_question = self.q_list[self.question_number]
            self.question_number+=1
            choice = input(f'Q. {self.question_number}. {self.current_question.text} (True/False)')
            score = self.check_ans(choice)
        print(f' Total score is {score}')

question_bank = []
for question in question_data:
    question_text = question['text']
    question_ans = question['ans']
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quizz = QuizzBrain(question_bank)
quizz.next_question()