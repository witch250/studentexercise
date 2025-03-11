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
    for i in range(n+1):
        count=createnumber(2,4)     #算式中项的个数
        string=''                   #将算式保存在字符串中
        for j in range(1,count+1):  #创建第一项到最后一项
            num=createnumber(0,r)
            num=str(num)
            string+=num
            if(j==count):
                break
            sign=createsign()
            string+=sign
        Question.append(string)
    return Question

if __name__=='__main__':
    Question=createquestion(10-1,3)
    print(Question)
        

