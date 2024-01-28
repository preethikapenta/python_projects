questionlist=[{"question":"India has more population in all over the world","answer":"False"},{"question":"The current PM of India is Narendra Modiji","answer":"True"},{"question":"The current Cm of AP is Chandrababunaidu","answer":"False"},{"question":"India has greatest economy in world","answer":"False"},{"question":"UP is the greatest populated country  India","answer":"True"}]
questionbank=[]
class Questions:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer
class Quiz:
    def __init__(self,q_list):
        self.score=0
        self.qno=0
        self.questionlist=q_list
    def checkanswer(self,ask,answer):
        if ask.lower()==answer.lower():
            print('Awesome,you got it right')
            self.score+=1
        else:
            print('Oops! that is wrong answer.')
        print(f'the correct answer was {answer}')
        print(f'your current score is {self.score}/{self.qno}')
    def stillq(self):
        if self.qno<len(self.questionlist):
            return True
        

            

    def nextquestion(self):
        
        current=self.questionlist[self.qno]
        self.qno+=1
        
        ask=input(f"Q.{self.qno} {current.question } Type (True/False) ")
        self.checkanswer(ask,current.answer)
    
for i in questionlist:
    questiontext=i["question"]
    answertext=i["answer"]
    new=Questions(questiontext,answertext)
    questionbank.append(new)
quiz=Quiz(questionbank)
while quiz.stillq()==True:
    quiz.nextquestion()
print("you have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.qno}")
percent=int((quiz.score/quiz.qno)*100)
print(f'Your efficiency is {percent}%')
