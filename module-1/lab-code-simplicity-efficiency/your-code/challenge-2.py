"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random


def RandomStringGenerator(l=12):
    lst=[]
    a=list(range(0,10))
    a+=[chr(x) for x in range(97,123)]
    lst=random.choices(a, k=l)
    print(lst)
    return lst
    

def BatchStringGenerator(n=2,a=8, b=12):
    a = int(input('Enter minimum string length: '))
    b = int(input('Enter maximum string length: '))
    n = int(input('How many random strings to generate? '))
    for i in range(0,n):
        lsts=[]
        length=random.choice(list(range(a,b)))
        lsts.append(RandomStringGenerator(length))
    return lsts
    
def main():
    BatchStringGenerator()



if __name__=="__main__":
    main()
    

"""
def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    p = 0
    s = ''
    while p<l:
        import random
        s += random.choice(a)
        p += 1
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(n):
        c = None
        if a < b:
            import random
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(c))
    return r

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))
    """