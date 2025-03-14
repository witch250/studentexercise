from readandwrite import *
from calculator import *

if __name__=='__main__':
    #Questions=CreateQuestions(10-1,5)  #创建0~(10-1)范围内的5条式子
    Questions=['9*9/(2*9)']
    print(Questions)
    Results=CalculateResults(Questions) #计算存储式子的列表
    print(Results)
        

