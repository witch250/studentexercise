from write import *
from calculator import *
from check import *
import sys
import os
#py main.py -n 12 -r 10
#py main.py -e Exercises.txt -a YourAnswers.txt
if __name__=='__main__':
    try:
        flag=False
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        put=sys.argv
        if len(put)>1: #调用cmd
            try:
                flag=True
                if put[1]=='' or put[2]=='' or put[3]=='' or put[4]=='':
                    pass
                elif put[1]=='-n' and put[3]=='-r':
                    if(int(put[2])<=1 or int(put[4])<=1):
                        print("-n 请输入大于0的数")
                    elif(int(put[4])>10):
                        print("-r 请输入1-10")
                    else:
                        N=int(put[2])
                        r=int(put[4])
                elif put[1]=='-e' and put[3]=='-a':
                    exercisespath=put[2]
                    youranswerspath=put[4]
                    Questions=ReadQuestions(exercisespath)
                    Answers=[]
                    for elem in Questions:
                        Question=ReversePolish(elem)       #给出逆波兰式
                        result=GiveResult(Question) 
                        Answers.append(result)
                    YourAnswers=ReadAnswers(youranswerspath)
                    #Answers=ReadAnswers("Answers.txt")
                    WriteCheck("Grade.txt",Answers,YourAnswers)
                    print("执行完毕")
                    os.system('pause')
                    sys.exit()
                else:
                    pass
            except IndexError:
                raise IndexError("输入过少") 
        if flag==False: #脚本内参数
            N=10
            r=10             #r以内，不包括r
            exercisespath="Exercises.txt"
            youranswerspath="YourAnswers.txt"
        Questions=[]
        Results=[]
        i=1
        while True:             #没有重复检测
            q=CreateQuestion(r-1)
            q=CutKuoHao(q)                  #仅简化第一个和最后一个括号
            showq=q                         #包含A,因为2'1/2中的'
            q=CutA(q)                       #去除分数标志A

            Question=ReversePolish(q)       #给出逆波兰式
            result=GiveResult(Question)     #计算逆波兰式的值
            if result==-1:                  #结果不合法那就重新来一个
                continue
            i+=1
            Questions.append(showq)
            Results.append(result)
            if(i==N+1):
                break
        WriteQuestions(Questions)
        WriteResults(Results)
    except PermissionError as e:
        print(e)
    except MemoryError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except IndexError as e:
        print(e)
    except NameError:
        print("输入有误")
    except UnicodeDecodeError as e:
        print(e)
    os.system('pause')
