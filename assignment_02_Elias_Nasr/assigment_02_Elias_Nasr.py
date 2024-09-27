#ex1:#
######

x = int(input('Please enter a positif number: '))
while (x < 0):
    x = int(input('Reenter a positif number: '))
    
if (x == 0):
    print('factorial is: 0')
if (x > 0):
    while (i <= x):
        factorial = factorial * i
        i += 1
    print('factorial is: ',factorial)

#####
#ex2#
#####

def findDivisors(x):
    l1 = []
    i = x
    while (i > 0):
        if (x % i == 0):
            l1.append(int(x / i))
        i -= 1
    print(l1)

a = int(input("enter a number: "))
findDivisors(a)

#####
#ex3#
#####

s = input('Enter a string: ')
i = 1
while (i <= len(s)):
    print(s[len(s)-i], end = "")
    i += 1

#####
#ex4#
#####

def getEven(x):
    
    l1 = x.split()
    for i in range(len(l1)):
        l1[i] = int(l1[i])
    
    l2 = []

    for i in l1:
        if (i % 2 == 0):
            l2.append(i)
        
    print(l2)

y = input("Enter the list of numbers separated by a space: ")
getEven(y)

#####
#ex5#
#####

def checkPass(str):
    isStrong = False

    if (len(str) >= 8):
        for i in range(len(str)):
            if (str[i] == '#' or str[i] == '?' or str[i] == '!' or str[i] == '$'):
                for i in range(len(str)):
                    if (str[i].isupper()):
                        for i in range(len(str)):
                            if (str[i].islower()):
                                for i in str:
                                    if (i.isnumeric()):
                                        isStrong = True
                                        break
    if (isStrong):
        print("Strong password")
    else:
        print("Weak password")

str = input("Enter a password: ")
checkPass(str)

#####
#ex6#
#####

def checkValidity (s):
    isValid = True
    l1 = str.split('.')

    for i in range(len(l1)):
        l1[i] = int(l1[i])
        if (len(l1) != 4):
            isValid = False
        if (l1[i] < 0 or l1[i] > 255):
            isValid = False  
        if (int(l1[i][0]) == 0):
            isvalid = False
          
    if (isValid):
        print("valid")
    else:
        print("Invalid")

str = input("Enter an IPv4: ")
checkValidity(str)
