base = int(input('Enter Base: '))
pow = int(input('Enter Power: '))

def power(b,p):
    result=1
    neg = False
    if p==0:
        return 1
    elif p < 0:
        neg = True
        p = -1*p

    for i in range(p):
        result = result*b
    if neg:
        result = 1/result
    return result

print(f"{base} raise to power of {pow}:",power(base,pow))
        
        