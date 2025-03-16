import math
from othermath import GreatestCommonDivisor
#别问我为什么这么多行，有些是大概相通的
def TurnListToNumber(L):
    num=0
    n=1
    while L:
        num+=eval(L.pop())*n
        n=n*10
    return num

def SimpleFraction(num1,num2):
    r=GreatestCommonDivisor(num1,num2)
    num1=num1//r
    num2=num2//r
    return num1,num2

def DivideFraction(L):  #like['C','1','+','5','/','8']
    i=0
    flag=1
    add=[]
    up=[]
    down=[]
    while i<len(L):
        if(L[i]=='C' or L[i]=='+' or L[i]=='/'):
            if(L[i]=='+'):
                flag=2
            elif(L[i]=='/'):
                flag=3
            i+=1
            continue
        if(flag==1):
            add.append(L[i])
        elif(flag==2):
            up.append(L[i])
        elif(flag==3):
            down.append(L[i])
        del L[i]
    return L,add,up,down

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
        L1,add1,up1,down1=DivideFraction(L1)    #将列表元素分离为数字，带的整数，分子，分母
        L2,add2,up2,down2=DivideFraction(L2)
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
            UP,DOWN=SimpleFraction(UP,DOWN)     #化简分数
            L1.insert(3,str(DOWN))
            L1.insert(2,str(UP))
            L1.insert(1,str(ADD))
            string=''
            for elem in L1:
                string+=elem
    return string

def FractionSub(num1,num2): #传进来的分数最简,整数-分数，分数-分数，分数-整数
    if(num1.isdecimal()):       #整数减分数
        L2=[]
        for elem in num2:       #字符串转列表提取数字
            L2.append(elem)
        L2,add2,up2,down2=DivideFraction(L2)
        ADD2=TurnListToNumber(add2)
        UP2=TurnListToNumber(up2)
        DOWN2=TurnListToNumber(down2)
        UP=DOWN2-UP2
        DOWN=DOWN2
        ADD=eval(num1)-ADD2-1
        if(ADD<0):      #计算负数不仅错误，结果也是错的
            return -1
        L2.insert(3,str(DOWN))
        L2.insert(2,str(UP))
        L2.insert(1,str(ADD))
        string=''
        for elem in L2:
            string+=elem
        return string
    elif(num2.isdecimal()):     #分数-整数----------
        L=[]
        S=[]
        num=0   #整数部分结果
        for elem in num1:       #字符串转列表提取数字
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
        num-=eval(num2)         #相减
        if(num<0):      
            return -1
        L.insert(1,str(num))
        string=''               #转回字符串
        for i in L:
            string+=i
        return string
    else:                   #都是分数-----------------
        L1=[]
        L2=[]
        for elem in num1:
            L1.append(elem)
        for elem in num2:
            L2.append(elem)      
        L1,add1,up1,down1=DivideFraction(L1)    #将列表元素分离为数字，带的整数，分子，分母
        L2,add2,up2,down2=DivideFraction(L2)
        ADD1=TurnListToNumber(add1)
        UP1=TurnListToNumber(up1)
        DOWN1=TurnListToNumber(down1)
        ADD2=TurnListToNumber(add2)
        UP2=TurnListToNumber(up2)
        DOWN2=TurnListToNumber(down2)
        DOWN=math.lcm(DOWN1,DOWN2)      #最小公倍数
        UP1=int(UP1*(DOWN/DOWN1))       #分子放大
        UP2=int(UP2*(DOWN/DOWN2))
        UP=((UP1+DOWN)-UP2)%DOWN
        withadd=0
        if (UP1/DOWN1)-(UP2/DOWN2)<0:
            withadd=-1
        ADD=ADD1-ADD2+withadd
        if(ADD<0):      
            return -1
        if(UP==0):                   
            return str(ADD)
        else:                           #L1=C+/，所以往里插入
            UP,DOWN=SimpleFraction(UP,DOWN)     #化简分数
            L1.insert(3,str(DOWN))
            L1.insert(2,str(UP))
            L1.insert(1,str(ADD))
            string=''
            for elem in L1:
                string+=elem
        return string

def FractionMul(num1,num2):
    if num1.isdecimal():    #num2一定是分数
        pass
    elif num2.isdecimal():
        t=num2
        num2=num1
        num1=t
    if(num1=='0'):
        return '0'
    if num1.isdecimal():        #一个整数，一个分数
        L2=[]
        for elem in num2:       #字符串转列表提取数字
            L2.append(elem)
        L2,add2,up2,down2=DivideFraction(L2)
        ADD2=TurnListToNumber(add2)
        UP2=TurnListToNumber(up2)
        DOWN2=TurnListToNumber(down2)
        UP=UP2*eval(num1)
        DOWN=DOWN2
        withadd=0                       #分子大过分母则变为整数
        while UP>DOWN:
            UP-=DOWN
            withadd+=1
        ADD=ADD2*eval(num1)+withadd
        UP,DOWN=SimpleFraction(UP,DOWN)     #化简分数
        L2.insert(3,str(DOWN))
        L2.insert(2,str(UP))
        L2.insert(1,str(ADD))
        string=''
        for elem in L2:
            string+=elem
        return string
    else:                   #都是分数
        L1=[]
        L2=[]
        for elem in num1:
            L1.append(elem)
        for elem in num2:
            L2.append(elem)      
        L1,add1,up1,down1=DivideFraction(L1)    #将列表元素分离为数字，带的整数，分子，分母
        L2,add2,up2,down2=DivideFraction(L2)
        ADD1=TurnListToNumber(add1)
        UP1=TurnListToNumber(up1)
        DOWN1=TurnListToNumber(down1)
        ADD2=TurnListToNumber(add2)
        UP2=TurnListToNumber(up2)
        DOWN2=TurnListToNumber(down2)
        UP1+=ADD1*DOWN1
        UP2+=ADD2*DOWN2
        UP=UP1*UP2
        DOWN=DOWN1*DOWN2
        withadd=0                       #分子大过分母则变为整数
        while UP>DOWN:
            UP-=DOWN
            withadd+=1
        ADD=withadd
        if(UP==DOWN):
            return str(ADD+1)
        UP,DOWN=SimpleFraction(UP,DOWN)     #化简分数
        L2.insert(3,str(DOWN))
        L2.insert(2,str(UP))
        L2.insert(1,str(ADD))
        string=''
        for elem in L2:
            string+=elem
        return string

def FractionDiv(num1,num2):
    if(num1=='0'):
        return '0'
    if num1.isdecimal():
        num1='C'+num1+'+0/1'
    if num2.isdecimal():
        num2='C'+num2+'+0/1'
    L1=[]
    L2=[]
    for elem in num1:
        L1.append(elem)
    for elem in num2:
        L2.append(elem)      
    L1,add1,up1,down1=DivideFraction(L1)    #将列表元素分离为数字，带的整数，分子，分母
    L2,add2,up2,down2=DivideFraction(L2)
    ADD1=TurnListToNumber(add1)
    UP1=TurnListToNumber(up1)
    DOWN1=TurnListToNumber(down1)
    ADD2=TurnListToNumber(add2)
    UP2=TurnListToNumber(up2)
    DOWN2=TurnListToNumber(down2)
    UP1+=ADD1*DOWN1
    UP2+=ADD2*DOWN2
    DOWN=DOWN1*UP2
    UP=UP1*DOWN2
    withadd=0                       #分子大过分母则变为整数
    while UP>DOWN:
        UP-=DOWN
        withadd+=1
    ADD=withadd
    if(UP==DOWN):
        return str(ADD+1)
    UP,DOWN=SimpleFraction(UP,DOWN)     #化简分数
    L2.insert(3,str(DOWN))
    L2.insert(2,str(UP))
    L2.insert(1,str(ADD))
    string=''
    for elem in L2:
        string+=elem
    return string
