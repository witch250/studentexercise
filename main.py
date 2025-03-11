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

def createquestion(r,n):    #r是最大数字，n是算式数量，暂不考虑分数和括号
    Question=[]             #将字符串放在列表中
    for i in range(n):
        count=createnumber(2,4)     #算式中项的个数
        string=''                   #将算式保存在字符串中
        sign='+'
        for j in range(1,count+1):  #创建第一项到最后一项
            num=createnumber(0,r)
            if sign and sign=='/' and num==0:
                num=createnumber(1,r)
            num=str(num)
            string+=num
            if(j==count):
                break
            sign=createsign()
            string+=sign
        Question.append(string)
    return Question

def CalculateResult(Question):
    Result=[]
    for i in Question:
        listnum=[]
        listsign=[]
        for elem in i:
            if(elem=='0' or elem=='1' or elem=='2' or elem=='3' or elem=='4' or elem=='5' or elem=='6' or elem=='7' or elem=='8' or elem=='9'):
                listnum.append(elem)
                if listsign:
                    if(listsign[-1]=='*'):
                        num1=int(listnum.pop())
                        num2=int(listnum.pop())
                        del listsign[-1]
                        num=num1*num2
                        listnum.append(num)
                    elif(listsign[-1]=='/'):
                        num1=int(listnum.pop())
                        num2=int(listnum.pop())
                        del listsign[-1]
                        num=num2/num1
                        listnum.append(num)
            if(elem=='+'or elem=='-' or elem=='*'or elem=='/'):
                listsign.append(elem)
        flag=True
        while(len(listnum)!=1):
            if(flag==True):
                flag=False
                continue
            if(listsign[0]=='+'):
                listnum[0]=float(listnum[0])
                listnum[1]=float(listnum[1])
                listnum[0]+=listnum[1]
                del listnum[1]
                del listsign[0]
            elif(listsign[0]=='-'):
                listnum[0]=float(listnum[0])
                listnum[1]=float(listnum[1])
                listnum[0]-=listnum[1]
                del listnum[1]
                del listsign[0]
        listnum[0]=float(listnum[0])
        print(listnum)
        Result.append(listnum)
    return Result     

if __name__=='__main__':
    Question=createquestion(10-1,3)
    print(Question)
    CalculateResult(Question)
        

