from main import *
from fractioncalculation import *
from write import *
from calculator import *
from check import *
import os
def testreadquestion():
    Questions=ReadQuestions("Exercises.txt")
    print(Questions)
def testreadanswer():
    Answers=ReadAnswers("Answers.txt")
    print(Answers)
def testcheck():
    YourAnswers=ReadAnswers("YourAnswers.txt")
    Answers=ReadAnswers("Answers.txt")
    WriteCheck("Grade.txt",Answers,YourAnswers)

def testmain():
    N=10000
    r=10
    Questions=[]
    Results=[]
    for i in range(0,N+1):
        q=CreateQuestion(r-1)
        print("生成式子")
        print(q)
        q=CutA(q)
        print("切除A")
        print(q)
        q=CutKuoHao(q)
        print("切除括号")
        print(q)
        print("完毕")

        print("逆波兰式")
        Question=ReversePolish(q)       #给出逆波兰式
        print("结果")
        result=GiveResult(Question)     #计算逆波兰式的值
        if result==-1:
            i-=1
            continue
        Questions.append(q)
        Results.append(result)
    print(Questions)
    print(Results)

if __name__=='__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #testreadquestion()
    #testreadanswer()
    testcheck()