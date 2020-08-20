#Example: 
"""
eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
"""
import os
import random

"""
#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square=[(n**2) for n in range(0,20)]
print(square)


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two=[(2**t) for t in range(0,50)]
print(power_of_two)



#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt=[(n**0.5) for n in range(0,100)]
print(sqrt)



#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list=[i for i in range(-10,1)]
print(my_list)



#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odd=[o for o in range(1,101) if not (o%2==0)]
print(odd)



#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven=[d for d in range(1,1000) if d%7==0]

print(divisible_by_seven)



#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience


teststring = 'Find all of the words in a string that are monosyllabic'
vowels=['a','e','i','o','u']
non_vowels=[nv for nv in teststring if nv not in vowels]
print(non_vowels)



#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results



sentence='The Quick Brown Fox Jumped Over The Lazy Dog'
enumerar=dict(enumerate(sentence))

capital_letters=[v for k,v in enumerar.items() if v.isupper()==True]
print(capital_letters)




#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

vowels_=['a','e','i','o','u',' ']
sentence='The quick brown fox jumped over the lazy dog'
consonants=[c for c in sentence if c not in vowels_]
print(consonants)



#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.


files=[os.listdir('/home/silviaherf/IH_DAFT/Bootcamp/datamad0820/')]
print(files)



#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results
#########CONTINUNAR

random_lists=[[r for r in random.choices(range(0,101), k=10)],[r for r in random.choices(range(0,101), k=10)],[r for r in random.choices(range(0,101), k=10)], [r for r in random.choices(range(0,101), k=10)]]
print(random_lists)





#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list=[i for l in list_of_lists for i in l]
print(flatten_list)

"""

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats=[[float(i) for l in list_of_lists[0] for i in l],[float(i) for l in list_of_lists[1] for i in l],[float(i) for l in list_of_lists[2] for i in l],[float(i) for l in list_of_lists[3] for i in l]]
print(floats)
"""

#14. Handle the exception thrown by the code below by using try and except blocks. 


for i in ['a','b','c']:
    print i**2


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

z = x/y




#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]
print(abc[3])


#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 




#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

f = open('testfile','r')
f.write('Test write this')




#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())




#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.




# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 




# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))


"""