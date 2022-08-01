"""
1.gerenrate random to from 1 to 5 and assign it to the variable randomno
2.print random number
3.ask user to input the number between 1 to 5 and assign it with variable usernumber
4.convert it ot integer
5.declare one variable with name tries and assign it with value 1
6.use while loop to print wrong number until the usernumber is equal to randomnumber

8.in while loop ask user to input new  numer every time until the usernumber is not equal to randomnumber  

"""
import random #because we need to generate random number
randomno=random.randint(1,5)#use randint method from random class and assign it to the variable randomno
print("here is the random number", randomno)
usernumber=input("guess any number between 1 to 5 ")# ask user to input number between 1 to 5
usernumber=int(usernumber)#convert the user input to integer
tries=1#declare a variable with name tries and assign it with a value 1
while usernumber!=randomno:#only go in loop when two numbers are not equal
    print("wrong guess")
    usernumber=input("guess another number ")#ask user to guess another number when the first guess is notcorrect
    usernumber=int(usernumber)#convert it to integertries=tries+1
    tries=tries+1
print("no of tries user take to guess right no is  ",tries)
    
