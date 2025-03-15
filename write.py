def WriteQuestions(Questions):
    try:
        with open("Exercises.txt",'w',encoding='utf-8') as f:
            i=1
            for elem in Questions:
                f.write("%d. "%i)
                i=i+1
                n=0
                flag=False
                for ch in elem:
            
                    if(n!=len(elem)-1 and elem[n+1]=='A'):
                        flag=True
                        n+=1
                        continue
                    if(elem[n]=='A'):
                        n+=1
                        continue
                    if(ch==')'and flag==True):
                        if(n!=len(elem)-1 and elem[n+1]!=')'):
                            f.write(' ')
                        n+=1
                        flag=False
                        continue
                    if(flag==True and ch=='+'):
                        n+=1
                        f.write('\'')
                        continue
                    if(flag==False and ch=='*'):
                        f.write('×')
                        f.write(' ')
                        n+=1
                        continue
                    if(flag==False and ch=='/'):
                        f.write('÷')
                        f.write(' ')
                        n+=1
                        continue
                    f.write(ch)
                    if(ch!='(' and ch!=')' and n!=len(elem)-1 and elem[n+1]!=')' and flag==False):
                        f.write(' ')
                    if(ch==')' and flag==False and n!=len(elem)-1 and elem[n+1]!=')'):
                        f.write(' ')
                    n+=1
                f.write('\n')
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    except PermissionError:
        raise PermissionError("不允许访问文件")
    #except Exception:
    #    raise Exception("发生错误")

def WriteResults(Results):
    try:
        with open("Answers.txt",'w',encoding='utf-8') as f:
            i=1
            for elem in Results:
                f.write("%d. "%i)
                i=i+1
                flag=False
                for ch in elem:
                    if(ch=='C'):
                        flag=True
                        continue
                    if(flag==True and ch=='+'):
                        f.write('\'')
                        continue
                    f.write(ch)
                f.write('\n')
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    except PermissionError:
        raise PermissionError("不允许访问文件")