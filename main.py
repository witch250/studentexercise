from write import *
from calculator import *
from check import *
import sys
import os
from classerror import *
#py main.py -n 12 -r 10
#py main.py -e Exercises.txt -a YourAnswers.txt

def main(N,r):
    try:
        if(N<0):
            raise NTooSmallError("输入的n过小")
        Questions=[]
        Results=[]
        Hash=[]
        i=1
        while True:             #没有重复检测
            q=CreateQuestion(r-1)
            q=CutKuoHao(q)                  #仅简化第一个和最后一个括号
            showq=q                         #包含A,因为2'1/2中的'
            q=CutA(q)                       #去除分数标志A

            Question=ReversePolish(q)       #给出逆波兰式
            result,hash=GiveResult(Question)     #计算逆波兰式的值
            if result==-1:                  #结果不合法那就重新来一个
                continue
            if(r!=1):
                for j in range(0,i-1):
                    if(result==Results[j] and hash==Hash[j]):
                        continue
            i+=1
            Hash.append(hash)
            Questions.append(showq)
            Results.append(result)
            if(i==N+1):
                break
        WriteQuestions(Questions)
        WriteResults(Results)
    except MemoryError:
        raise MemoryError("内存溢出")
    except NameError:
        raise NameError("请确保输入是否正确")
    except RTooBigError:
        raise RTooBigError("给定的参数r过大")
    except RTooSmallError:
        raise RTooSmallError("给定的参数r过小")
    
def checkmain(put):
    try:
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
    except MemoryError:
        raise MemoryError("内存溢出")
    except NameError:
        raise NameError("请确保输入是否正确")
    except PermissionError:
        raise PermissionError("不允许访问文件")
    except OSError:
        raise OSError("请检查斜杠")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("文件类型错误")
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    
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
                        print("请输入大于0的数")
                    elif(int(put[4])>10):
                        print("-r 请输入1-10")
                    else:
                        N=int(put[2])
                        r=int(put[4])
                        main(N,r)
                elif put[1]=='-e' and put[3]=='-a':
                    checkmain(put)
                else:
                    pass
            except IndexError:
                raise IndexError("输入过少") 
        if flag==False: #脚本内参数
            N=10
            r=10             #r以内，不包括r
            exercisespath="Exercises.txt"
            youranswerspath="YourAnswers.txt"
            main(N,r)
    except PermissionError as e:
        print(e)
    except MemoryError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except IndexError as e:
        print(e)
    except NameError as e:
        print(e)
    except UnicodeDecodeError as e:
        print(e)
    except RTooBigError as e :
        print(e)
    except RTooSmallError as e:
        print (e)
    except NTooSmallError as e:
        print(e)
    os.system('pause')
