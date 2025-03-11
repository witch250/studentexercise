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

def CreateQuestion(r,n):    #r是最大数字，n是算式数量，暂不考虑分数和括号
    count=createnumber(2,4)     #算式中项的个数
    string=''                   #将算式保存在字符串中
    sign='+'
    for j in range(1,count+1):  #创建第一项到最后一项
        num=createnumber(0,r)
        if sign and sign=='/' and num==0:
            num=createnumber(1,r)
        num=str(num)
        string+=num
        if(j==count):   #不要生成过多的符号
            break
        sign=createsign()
        string+=sign
    return string

def CreateQuestions(r,n):   #r是最大数字，n是算式数量
    Questions=[]
    for i in range(n):
        q=CreateQuestion(r,n)
        Questions.append(q)
    return Questions

def CalculateResult(Question):#Question是字符串
    listnum=[]
    listsign=[]
    for elem in Question:  #放数字，乘除号先算
        if(elem=='0' or elem=='1' or elem=='2' or elem=='3' or elem=='4' or elem=='5' or elem=='6' or elem=='7' or elem=='8' or elem=='9'):
            listnum.append(elem)
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
        if(elem=='('):
            Q=[]

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
        result=CalculateResult(i)
        Results.append(result)
    return Results

if __name__=='__main__':
    Questions=CreateQuestions(10-1,3)
    print(Questions)
    Results=CalculateResults(Questions)
    print(Results)
        

