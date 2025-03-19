from main import *
from fractioncalculation import *
from write import *
from calculator import *
from check import *
from diyhash import *
import os
def testreadquestion():
    Questions=ReadQuestions("Exercises.txt")
    #print(Questions)

def testreadquestion1():        #抛出找不到文件
    try:
        Questions=ReadQuestions("1")
    except:
        raise FileNotFoundError
    #print(Questions)

def testreadquestion2():        #抛出不允许访问
    try:
        Questions=ReadQuestions("c:")
    except:
        raise PermissionError
    #print(Questions)

def testreadquestion3():        
    try:
        Questions=ReadQuestions("breakingcontent.txt")
    except:
        pass
    print(Questions)

def testreadanswer():
    Answers=ReadAnswers("Answers.txt")
    #print(Answers)

def testreadanswer1():        #抛出找不到文件
    try:
        Answers=ReadAnswers("1")
    except:
        raise FileNotFoundError
    #print(Answers)

def testreadanswer2():        #抛出不允许访问
    try:
        Answers=ReadAnswers("c:")
    except:
        raise FileNotFoundError
    #print(Answers)

def testreadanswer3():        #抛出不允许访问
    try:
        Answers=ReadQuestions("breakingcontent.txt")
    except:
        pass
    print(Answers)

def testcheck():
    YourAnswers=ReadAnswers("YourAnswers.txt")
    Answers=ReadAnswers("Answers.txt")
    WriteCheck("Grade.txt",Answers,YourAnswers)

def testcheck1():
    YourAnswers=ReadAnswers("none.txt")
    Answers=ReadAnswers("none.txt")
    WriteCheck("Grade.txt",Answers,YourAnswers)

def testcheckmain():
    checkmain(['','','breakingcontent.txt','','breakingcontent.txt'])

def testcheckmain1():
    checkmain(['','','Exercises.txt','','YourAnswers.txt'])

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
    Q=['1/2','1/2','2/1']
    for q in Q:
        Question=ReversePolish(q)       #给出逆波兰式
        #print("结果")
        result,hash=GiveResult(Question)     #计算逆波兰式的值
        print("-----------")
        print(result)
        print(hash)
        
def testmain1():
    main(100,10)

def testmain2():    #预计引发raise RTooSmallError
    try:
        main(100,1)     #生成0
    except:
        raise RTooSmallError

def testmain3():
    main(100,2)

def testmain31():   #预计引发RTooSmallError，n太大
    try:
        main(1000,2)   
    except:
        raise RTooSmallError

def testmain4():
    main(100,3)

def testmain5():
    main(10000,10)

def testmain51():    #NTooBigError
    main(40000,10)
if __name__=='__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #testreadquestion3()
    #testreadanswer3()
    #testcheck()
    #testmain51()
    #testhash1()
    #testcheckmain()
    testcheckmain1()