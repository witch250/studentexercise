import random
from fractioncalculation import *
from othermath import GreatestCommonDivisor

def createnumber(a,b):
    return random.randint(a,b)  #包括a,b

def createsign():
    sign=['+','-','*','/']
    return random.choice(sign)

def createFenShu(a,b):
    string=''
    numUP=1
    numDOWN=1
    while numUP>=numDOWN or GreatestCommonDivisor(numDOWN,numUP)!=1:
        numUP=createnumber(1,b)
        numDOWN=createnumber(2,b)
    numADD=createnumber(1,b)
    string+='('+'A'+str(numADD)+'+'+str(numUP)+'/'+str(numDOWN)+')'
    return string

def CutA(Question):     #展示完了就删除A
    L=[]
    for i in Question:  
        if(i!='A'):
            L.append(i)
    string=''
    for i in L:
        string+=i
    return string

def CreateQuestion(r):    #r是最大数字
    count=createnumber(2,4)     #算式中项的个数
    string=''                   #将算式保存在字符串中
    sign='+'
    kuohao=0                    #括号个数
    flag=True                   #当前轮是否有'('生成
    for j in range(1,count+1):  #创建第一项到最后一项
        if( count!=2 and j!=count): #不在仅有两项时，以及最后一项生成左括号,两个左括号没法相邻
            if(createnumber(0,1)==1):   #50%
                string+='('
                kuohao+=1
                flag=True
        if r>1 and createnumber(0,3)==0:        #生成整数或者分数
            num=createFenShu(0,r)
        else:
            num=createnumber(0,r)
            if sign and sign=='/' and num==0:   #不要1/0
                if(r==1):
                    num=1
                else:
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
        Safe=[]
        L=[]
        pos=0
        for i in q:
            pos+=1
            if(i=='('or i==')'):
                if(i=='('):
                    Safe.append(False)
                    L.append(i)
                elif(i==')'):
                    for n in range(len(Safe)-1,-1,-1):
                        if(Safe[n]==False):
                            Safe[n]=True
                            break               
            if(pos==len(q)-1 and Safe[0]==False):
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
  
def ReversePolish(i):
    S=[]    #存放+-*/(
    L=[]    #存放数字+-*/,并且是结果
    for elem in i:
        if(elem==' '):
            pass
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
        else:       #处理+-*/
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
            elif elem=='+' or elem=='-' or elem=='*' or elem=='/':  #遇到符号，弹出两个数字计算后，再压入栈
                num1=S.pop()
                num2=S.pop()
                if num1.isdecimal() and num2.isdecimal():   #都只含数字
                    #仅对整数有效
                    num1=eval(num1)
                    num2=eval(num2)
                    if elem=='+':
                        num=num1+num2
                    elif elem=='-':
                        num=num2-num1
                        if(num<0):
                            return -1
                    elif elem=='*':
                        num=num1*num2
                    elif elem=='/':             #这一步可能产生分数
                        if(num1==0):            #4/(2-2)
                            return -1
                        if GreatestCommonDivisor(num1,num2)==num1:  #默认2>1
                            num=num2/num1
                            num=int(num) 
                        else:                   #无所谓
                            num=''
                            num3=0
                            num1,num2=SimpleFraction(num1,num2)
                            while num2>num1:
                                num2=num2-num1
                                num3+=1
                            num+='C'+str(num3)+'+'+str(num2)+'/'+(str(num1)) #0'2/3是允许的
                else:   #整数分数 分数分数
                    if elem=='+':
                        num=FractionAdd(num2,num1)
                    elif elem=='-':
                        num=FractionSub(num2,num1)
                        if(num==-1):
                            return -1
                    elif elem=='*':
                        num=FractionMul(num2,num1)
                    elif elem=='/':        
                        if(num1=='0'):        #1/2-(1/2-1/2)
                            return -1     
                        num=FractionDiv(num2,num1)
                S.append(str(num))  
    return(S[0])
