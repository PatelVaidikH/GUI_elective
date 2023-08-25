# While loop to generate first 10 integers
print('First 10 integers using while loop')
i = 1
while i<=10:
    print(i)
    i = i+1

# For loop to generate first 10 integers
print('First 10 integers using for loop')
for i in range(1,11):
    print(i)
    
# While loop to generate numbers with gap of 0.5
print('Numbers with gap of 0.5 using while loop')
i = 1
while i<=3:
    print(i)
    i = i+0.5

# While loop to generate all the multiples of 13 between 500 and 600
print('All the multiples of 13 between 500 and 600 using while loop')
i = 500
while i<=600:
    if i%13 == 0:
        print(i)
    i = i+1

# For loop to generate all the multiples of 13 between 500 and 600
print('All the multiples of 13 between 500 and 600 using for loop')
for i in range(500, 601):
    if i%13 == 0:
        print(i)
