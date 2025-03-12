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
    count=createnumber(3,4)     #算式中项的个数
    string=''                   #将算式保存在字符串中
    sign='+'
    kuohao=0                    #括号个数
    flag=True                   #当前轮是否有'('生成
    for j in range(1,count+1):  #创建第一项到最后一项
        if( count!=2 and j!=count): #不在仅有两项时，以及最后一项生成左括号
            if(createnumber(0,1)==1):   #50%
                string+='('
                kuohao+=1
                flag=True
        num=createnumber(0,r)
        if sign and sign=='/' and num==0:   #不要1/0
            num=createnumber(1,r)
        num=str(num)
        string+=num
        if(kuohao!=0 and flag==False): #不要在生成'('的时候也生成')',否则(6)
            if(createnumber(0,1)==1):
                string+=')'
                kuohao-=1

        if(j==count):   #不要生成过多的符号
            break
        sign=createsign()
        string+=sign
        flag=False
    while kuohao!=0:    #补充')'
        string+=')'
        kuohao-=1
    return string

def CutKuoHao(q):   #删除首个括号，使它更加简洁
    if(q[0]=='('and q[-1]==')'):
        kuohao=0
        for i in q[-2::-1]: #从倒数第二开始，倒着每次进1
            if i=='(':  #说明如果我切了，末尾会剩下'('
                return q
            if i==')':
                Q=[]
                string=''
                for j in q:
                    Q.append(j)
                del Q[0]
                del Q[-1]
                for i in Q:
                    string+=i
                q=string
                break
    else:
        pass
    return q

def CreateQuestions(r,n):   #r是最大数字，n是算式数量
    Questions=[]
    for i in range(n):
        q=CreateQuestion(r)
        #print(q)
        q=CutKuoHao(q)
        #print(q)
        Questions.append(q)
    return Questions
  

def ReversePolish(i):
    S=[]    #存放+-*/(
    L=[]    #存放数字+-*/,并且是结果
    for elem in i:
        if(elem=='0' or elem=='1' or elem=='2' or elem=='3' or elem=='4' or elem=='5' or elem=='6' or elem=='7' or elem=='8' or elem=='9'):
            L.append(elem)
        elif(elem=='('):    
            S.append('(')
        elif(elem==')'):    #弹出所有，直到左括号为止，包括'('
            t=0
            while(t!='('):
                t=S.pop()
                if(t=='('):
                    break
                L.append(t)
        else:
            if S==[]:
                S.append(elem)
            elif S[-1]=='(':    
                S.append(elem)
            elif(elem=='+'or elem=='-'):
                while S and S[-1]!='(' :    #此 + or - 必须在下面
                    t=S.pop()
                    L.append(t)
                S.append(elem)
            elif(elem=='*'or elem=='/'):    # * or / 可以在 + or - 上面
                while S and S[-1]!='(' and S[-1]!='+' and S[-1]!='-':
                    t=S.pop()
                    L.append(t)
                S.append(elem)
    while S!=[]:    #弹出剩余
        elem=S.pop()
        if(elem=='('):
            pass
        else:
            L.append(elem)
    string=''   #转成字符串
    for i in L:
        string+=i+' '
    return string

def GiveResult(Question):   #字符串Q
    S=[]
    for elem in Question:
        if elem==' ':
            pass
        else:
            if elem=='0' or elem=='1' or elem=='2' or elem=='3' or elem=='4' or elem=='5' or elem=='6' or elem=='7' or elem=='8' or elem=='9':
                S.append(elem)
            elif elem=='+' or elem=='-' or elem=='*' or elem=='/':
                num1=S.pop()
                num2=S.pop()
                num1=eval(num1)
                num2=eval(num2)
                if elem=='+':
                    num=num1+num2
                if elem=='-':
                    num=num2-num1
                if elem=='*':
                    num=num1*num2
                if elem=='/':
                    num=num2/num1
                S.append(str(num))
    return(S[0])

               

def CalculateResults(Questions):
    Results=[]  
    for i in Questions:
        Question=ReversePolish(i)
        #print(Question)
        result=GiveResult(Question)
        Results.append(result)
        #print(result)
    return Results

if __name__=='__main__':
    Questions=CreateQuestions(10-1,10)
    
    print(Questions)
    Results=CalculateResults(Questions)
    print(Results)
        

