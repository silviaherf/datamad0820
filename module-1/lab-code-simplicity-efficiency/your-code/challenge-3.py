"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""


from math import hypot

def hipotenusa():
    x = int(input("What is the maximal length of the triangle side? Enter a number: "))
    minim=5
    solution=0
    for hip in range(x,minim,-1):
        for b in range(x,(minim-1),-1):
            for a in range(x,(minim-2),-1):
                if type(hypot(b,a)==int) and hypot(b,a)<x and  (hypot(b,a)- int(hypot(b,a)))==0:                   
                    solution=int(hypot(b,a))
                    break
    return print(f"The longest side possible is {solution}")


def main():
     hipotenusa()

if __name__=="__main__":
    main()   

"""

def my_function(X):
    solutions = []
    for x in range(5, X):
        for y in range(4, X):
            for z in range(3, X):
                if (x*x==y*y+z*z):
                  solutions.append([x, y, z])
    m = 0
    for solution in solutions:
        if m < max(solution):
            m = max(solution)
    return m

X = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(my_function(int(X))))

"""
