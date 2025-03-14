from main import *
import math
def TurnListToNumber(L):
    num=0
    n=1
    while L:
        num+=eval(L.pop())*n
        n=n*10
    return num

def FractionAdd(num1,num2): #传进来的分数最简
    if num1.isdecimal():    #num2一定是分数
        pass
    elif num2.isdecimal():
        t=num2
        num2=num1
        num1=t
    if num1=='0':
        return num2
    if(num1.isdecimal()):    #整数+分数----------------------------
        L=[]
        S=[]
        num=0   #整数部分结果
        n=1     #个十百千
        for elem in num2:       #字符串转列表提取数字
            L.append(elem)
        i=0
        while True:             
            if(L[i]=='+'):
                break
            if(L[i]=='C'):
                i+=1
                continue
            S.append(L[i])
            del L[i]
        num=TurnListToNumber(S)
        num+=eval(num1)         #相加
        L.insert(1,str(num))
        string=''               #转回字符串
        for i in L:
            string+=i
    else:               #都是分数----------------------------------- 
        L1=[]
        L2=[]
        for elem in num1:
            L1.append(elem)
        for elem in num2:
            L2.append(elem)
        i=0
        flag=1
        add1=[]
        up1=[]
        down1=[]
        while i<len(L1):            #将列表元素分离为数字，带的整数，分子，分母
            if(L1[i]=='C' or L1[i]=='+' or L1[i]=='/'):
                if(L1[i]=='+'):
                    flag=2
                elif(L1[i]=='/'):
                    flag=3
                i+=1
                continue
            if(flag==1):
                add1.append(L1[i])
            elif(flag==2):
                up1.append(L1[i])
            elif(flag==3):
                down1.append(L1[i])
            del L1[i]
        i=0
        flag=1
        add2=[]
        up2=[]
        down2=[]
        while i<len(L2):
            if(L2[i]=='C' or L2[i]=='+' or L2[i]=='/'):
                if(L2[i]=='+'):
                    flag=2
                elif(L2[i]=='/'):
                    flag=3
                i+=1
                continue
            if(flag==1):
                add2.append(L2[i])
            elif(flag==2):
                up2.append(L2[i])
            elif(flag==3):
                down2.append(L2[i])
            del L2[i]
        ADD1=TurnListToNumber(add1)
        UP1=TurnListToNumber(up1)
        DOWN1=TurnListToNumber(down1)
        ADD2=TurnListToNumber(add2)
        UP2=TurnListToNumber(up2)
        DOWN2=TurnListToNumber(down2)
        DOWN=math.lcm(DOWN1,DOWN2)      #最小公倍数
        UP1=int(UP1*(DOWN/DOWN1))       #分子放大
        UP2=int(UP2*(DOWN/DOWN2))
        UP=UP1+UP2
        withadd=0                       #分子大过分母则变为整数
        while UP>DOWN:
            UP-=DOWN
            withadd+=1
        ADD=ADD1+ADD2+withadd
        if(UP==DOWN):                   #如果1'2/2
            return str(ADD+1)
        else:                           #L1=C+/，所以往里插入
            L1.insert(3,str(DOWN))
            L1.insert(2,str(UP))
            L1.insert(1,str(ADD))
            string=''
            for elem in L1:
                string+=elem
    return string