#def fibonacci():
number = int(input('How many numbers of the Fibonacci sequence would you like to see?: '))
n1, n2 = 0, 1
sum = 0
if number <= 0:
    ('Please enter a number greater than 0: ')
else:
    for i in range (1, number):
        print(sum, end='')
        n1 = n2
        n2 = sum
        sum = n1 + n2

#a = 1
#while a == 1:
    #fibonacci()
