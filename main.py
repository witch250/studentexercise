import random
def WriteQuestion():
    pass

def WriteResult():
    pass

def createnumber(a,b):
    return random.randint(a,b)  #包括a,b

def createsign():
    sign=['+','-','*','/']
    return random.choice(sign)

def CreateQuestion(r):    #r是最大数字,暂不考虑分数和括号
    count=createnumber(2,4)     #算式中项的个数
    string=''                   #将算式保存在字符串中
    sign='+'
    kuohao=0
    flag=True
    for j in range(1,count+1):  #创建第一项到最后一项
        if( count!=2 and j!=count): #不在首项前，仅有两项时，以及最后一项生成左括号
            if(createnumber(1,1)==1):
                string+='('
                kuohao+=1
                flag=True
        num=createnumber(0,r)
        if sign and sign=='/' and num==0:
            num=createnumber(1,r)
        num=str(num)
        string+=num
        if(kuohao!=0 and flag==False):
            if(createnumber(0,1)==1):
                string+=')'
                kuohao-=1

        if(j==count):   #不要生成过多的符号
            break
        sign=createsign()
        string+=sign
        flag=False
    while kuohao!=0:
        string+=')'
        kuohao-=1
    return string

def CutKuoHao(q):
    if(q[0]=='('):
        Q=[]
        string=''
        for i in q:
            Q.append(i)
        del Q[0]
        del Q[-1]
        for i in Q:
            string+=i
        q=string
    else:
        pass
    return q

def CreateQuestions(r,n):   #r是最大数字，n是算式数量
    Questions=[]
    for i in range(n):
        q=CreateQuestion(r)
        q=CutKuoHao(q)
        Questions.append(q)
    return Questions

def CalculateResult(Question,count):#Question是字符串,count循环该函数，记录当前应该是字符串中第几个元素
    listnum=[]
    listsign=[]
    for elem in Question:  #放数字，乘除号先算
        if(elem=='0' or elem=='1' or elem=='2' or elem=='3' or elem=='4' or elem=='5' or elem=='6' or elem=='7' or elem=='8' or elem=='9'):
            listnum.append(elem)
            count+=1
            if listsign:
                if(listsign[-1]=='*'):
                    num1=eval(listnum.pop())
                    num2=eval(listnum.pop())
                    del listsign[-1]
                    num=num1*num2
                    listnum.append(str(num))
                elif(listsign[-1]=='/'):
                    num1=eval(listnum.pop())
                    num2=eval(listnum.pop())
                    del listsign[-1]
                    num=num2/num1
                    listnum.append(str(num))
        if(elem=='+'or elem=='-' or elem=='*'or elem=='/'):
            listsign.append(elem)
            count+=1
        if(elem=='('):
            count+=1
            Q=[]
            for i in Question[count:]:
                Q.append(i)
                if(elem==')'):
                    count+=1
                    break
            result=CalculateResult(Q,count)
            listnum.append(result)

    flag=True
    while(len(listnum)!=1): #加减法
        if(flag==True):
            flag=False
            continue
        if(listsign[0]=='+'):
            listnum[0]=eval(listnum[0])
            listnum[1]=eval(listnum[1])
            listnum[0]+=listnum[1]
            listnum[0]=str(listnum[0])
            del listnum[1]
            del listsign[0]
        elif(listsign[0]=='-'):
            listnum[0]=eval(listnum[0])
            listnum[1]=eval(listnum[1])
            listnum[0]-=listnum[1]
            listnum[0]=str(listnum[0])
            del listnum[1]
            del listsign[0]
    #listnum[0]=eval(listnum[0])  #1个数字 '6'
    print(listnum)
    return listnum   

def CalculateResults(Questions):
    Results=[]
    for i in Questions:
        result=CalculateResult(i,0)
        Results.append(result)
    return Results

if __name__=='__main__':
    Questions=CreateQuestions(10-1,10)
    print(Questions)
    #Results=CalculateResults(Questions)
    #print(Results)
        

