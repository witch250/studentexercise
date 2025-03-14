from main import *
def FractionAdd(num1,num2): #传进来的分数最简
    if num1.isdecimal():    #num2一定是分数
        pass
    elif num2.isdecimal():
        t=num2
        num2=num1
        num1=t
    if num1=='0':
        return num2
    if(num1.isdecimal()):    #整数+分数
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
        while S:
            num+=eval(S.pop())*n
            n=n*10
        num+=eval(num1)         #相加
        L.insert(1,str(num))
        string=''               #转回字符串
        for i in L:
            string+=i
    else:               #都是分数   
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
        while i<len(L1):
            if(L1[i]=='C' or L1[i]=='+' or L1[i]=='/'):
                if(L1[i]=='+'):
                    flag=2
                elif(L1[i]=='/'):
                    flag==3
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
                    flag==3
                i+=1
                continue
            if(flag==1):
                add2.append(L2[i])
            elif(flag==2):
                up2.append(L2[i])
            elif(flag==3):
                down2.append(L2[i])
            del L2[i]
    return string