from main import *
from fractioncalculation import *
from write import *
from calculator import *
from check import *
from diyhash import *
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
def testhash():
    Q=['3+(2+1)','1+2+3','(1+2)+3','3+(1+2)','3+2+1','(3+2)+1']
    for q in Q:
        Question=ReversePolish(q)       #给出逆波兰式
        #print("结果")
        result,hash=GiveResult(Question)     #计算逆波兰式的值
        print("-----------")
        print(result)
        print(hash)

def testhash1():
    Q=['1/2','1/2']
    for q in Q:
        Question=ReversePolish(q)       #给出逆波兰式
        #print("结果")
        result,hash=GiveResult(Question)     #计算逆波兰式的值
        print("-----------")
        print(result)
        print(hash)
        
def testmain1():
    main(100,10)

def testmain2():
    main(100,1)

def testmain3():
    main(100,2)

def testmain4():
    main(100,3)

if __name__=='__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #testreadquestion()
    #testreadanswer()
    #testcheck()
    testmain4()
    #testhash1()