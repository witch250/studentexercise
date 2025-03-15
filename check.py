
def ReadQuestions(txtpath): #返回一个列表元素能用逆波兰式处理的列表
    try:
        with open(txtpath,"r",encoding='UTF-8') as txt:
            Q=txt.readlines()
            L=[]
            indexnumber=0
            for line in Q:
                indexnumber+=1
                line=line.strip()
                line=line.replace('%d. '%indexnumber,'')
                line=line.replace('×','*')
                line=line.replace('÷','/')
                line=line.replace('\'','+')
                S=[]
                flag=False
                i=0
                for ch in line:
                    if i!=len(line)-1 and i!=len(line)-2 and line[i+1].isdecimal() and (line[i+2].isdecimal() or line[i+2]=='+'):
                        flag=True
                        S.append('(')
                    elif(ch==' ' or ch==')')and flag==True:
                        flag=False
                        S.append(')')
                    S.append(ch)
                    i+=1
                if(flag==True):
                    S.append(')')
                string=''
                for ch in S:
                    string+=ch
                L.append(string)
        return L
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    except MemoryError:
        raise MemoryError("内存溢出")
    except PermissionError:
        raise PermissionError("不允许访问文件")
    except OSError:
        raise OSError("请检查斜杠")

def ReadAnswers(txtpath):
    try:
        with open(txtpath,"r",encoding='UTF-8') as txt:
            Q=txt.readlines()
            L=[]
            indexnumber=0
            for line in Q:
                indexnumber+=1
                line=line.strip()
                line=line.replace('%d. '%indexnumber,'')
                flag=False
                for ch in line:
                    if(ch=='\''):
                        flag=True
                line=line.replace('\'','+')
                if(flag==True):
                    line='C'+line
                L.append(line)
        return L
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    except MemoryError:
        raise MemoryError("内存溢出")
    except PermissionError:
        raise PermissionError("不允许访问文件")
    except OSError:
        raise OSError("请检查斜杠")
    
def Check(Results,Answers):
    num=0
    if len(Results)>len(Answers):
        num=len(Answers)
    else:
        num=len(Results)
    Correct=[]
    Wrong=[]
    i=1
    for i in range(0,num):
        if Results[i]==Answers[i]:
            Correct.append(i+1)
        else:
            Wrong.append(i+1)
    i+=1
    while i<len(Results):
        Wrong.append(i+1)
        i+=1
    return Correct,Wrong

def WriteCheck(txtpath,Results,Answers):
    try:
        with open(txtpath,'w',encoding='utf-8') as f:
            Correct,Wrong=Check(Results,Answers)
            if(Correct==[] and Wrong==[]):
                f.write("April Fool's Day!!!!!")
            else:
                i=0
                f.write("Correct:%d"%len(Correct))
                f.write('(')
                for elem in Correct:
                    f.write(str(elem))
                    i+=1
                    if(i<len(Correct)):
                        f.write(',')
                f.write(')\n')
                i=0
                f.write("Wrong:%d"%len(Wrong))
                f.write('(')
                for elem in Wrong:
                    f.write(str(elem))
                    i+=1
                    if(i<len(Wrong)):
                        f.write(',')
                f.write(')')
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    except PermissionError:
        raise PermissionError("不允许访问文件")