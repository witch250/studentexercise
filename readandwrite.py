def WriteQuestions(Questions):
    try:
        with open("Exercises.txt",'w',encoding='utf-8') as f:
            i=1
            f.write("打开文件")
            for elem in Questions:
                f.write("%d."%i)
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
                        n+=1
                        continue
                    f.write(ch)
                    n+=1
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    except PermissionError:
        raise PermissionError("不允许访问文件")
    #except Exception:
    #    raise Exception("发生错误")

def WriteResult():
    pass