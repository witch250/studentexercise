
def GreatestCommonDivisor(num1,num2): #最大公约数
    while num2!=0:
        r=num1%num2
        num1=num2
        num2=r
    return num1