from readandwrite import *
from calculator import *

if __name__=='__main__':

    N=10
    r=10
    Questions=[]
    Results=[]
    i=1
    while True:             #没有重复检测
        q=CreateQuestion(r-1)
        q=CutA(q)                       #去除分数标志A
        q=CutKuoHao(q)                  #仅简化第一个和最后一个括号

        Question=ReversePolish(q)       #给出逆波兰式
        result=GiveResult(Question)     #计算逆波兰式的值
        if result==-1:                  #结果不合法那就重新来一个
            continue
        i+=1
        Questions.append(q)
        Results.append(result)
        if(i==N+1):
            break
    print(Questions)
    print(Results)
    n=0
    for j in Questions:
        n+=1
        print("%d  %s"%(n,j))
    

