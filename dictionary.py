def dictionary(lower, upper):
    mydic=dict()
    if not (isinstance(lower,int) and isinstance(upper,int)):
        raise valueError('invalid input, only intergers expected')
    for x in range(lower,upper):
        mydic[x]=x**2
    return mydic

if __name__ == '__main__':
    print(dictionary(2,15))
   
    