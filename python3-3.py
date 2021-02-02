#Comments
#This is my 3rd video for the day

'''
A lot of text
A lot of text
A lot of text
A lot of text
A lot of text
A lot of text
A lot of text
A lot of text
A lot of text ''' #Be cautious using these

#I can enable and disable code using comments.

#x = 'Hello World'
#print(x)

#-------------

#Booleans True or False (like a light switch)

#x = True #Notice this is case sensitive
#y = False #Notice this is case sensitive
#print(x, y)

#-------------

#Comparisons are the 'Building Block' of logic

x = input('Please enter in the first # here:') #Asking the user to unput an integer than is stored in the variable x.
y = input('Please enter in the second # here:')

#Intro to Logic (If Else)
'''
if x > y :
    print("X is larger than Y")

else :
    print("Y is larger than x")
'''


#Writing and Printing my first function
#Calling on the values stored in the above variables to compare them using logic (If Else) to print a statement.

def myFunction (x,y): #Defining a Function named 'myFunction' and giving it 2 Parameters (have to give the function 2 things)
    if x > y: #If my X Input (above) is greater than y, return the printed statement below.
        print('X is greater than Y')
    elif x == y:      #If x and Y are the same value, print the below statement.
        print('X and Y are the same!')
    else:     #If my X input (above) is NOT greater than y, return the 'else' statement below.
        print('X is NOT greater than Y')

myFunction(x, y)


name = input('Please tell me your name: ')
age = input('Please tell me your age: ')

print('My name is ' + name + ' and I am ' + str(age) + ' years old.')