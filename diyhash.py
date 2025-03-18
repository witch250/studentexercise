from line_profiler import profile 
@profile
def diynumhash(num):
    return int(num)%61
@profile
def diystringhash(string):
    hash=0b0
    for elem in string:
        if elem.isdecimal():
            hash+=diynumhash(elem)
    return hash<<2
@profile
def diyhash(num1,num2,sign):
    if num1.isdecimal():
        i1=diynumhash(num1)
    else:
        i1=diystringhash(num1)
    if num2.isdecimal():
        i2=diynumhash(num2)
    else:
        i2=diystringhash(num2)
    if sign=='+':
        i=i1+i2<<3+0b11
    elif sign=='-':
        i=i1+i2<<3+0b111
    elif sign=='*':
        i=i1+i2<<3+0b1111
    elif sign=='/':
        i=i1+(i2<<5)+0b11111
    else:
        i=i1+(i2<<9)+0b11111
    return i

