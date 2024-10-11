#########
###ex1###
#########

def countDigits(x):
    if (-10 < x < 10):
        return 1

    else:
        return 1 + countDigits(x / 10)

#########
###ex2###
#########

def findMax(lst):
    
    if (len(lst) == 0):
        return 0
    elif (len(lst) == 1):
        return lst[0]
    
    m = lst[len(lst) - 1]         #starting from last value

    if (m > lst[len(lst) - 2]):   #if last value greater than before last value
        lst.pop(len(lst) -2)      #drop before last value            
        findMax(lst)              #and repeat
        return lst[0]             #it will remain only one value on the first index
    else:                         #if last value lower than before last value
        lst.pop(len(lst) - 1)     #drop last value
        findMax(lst)              #and repeat
        return lst[0]             #it will remain only one value on the first index

#########
###ex3###
#########

def countTag(text,s):
    first_split = text.split('\n')    #to split the code by lines

    first_str = first_split.pop()    #to save the last value(last line) in first str and remove it from first split list 
    
    second_split = first_str.split('/') #to split the value by / and get 2 values 
    text = text.replace(first_str,'')   #to remove first str from text
    if ((str(second_split[1])) == (s + ">")): #if the second value is the string we are looking for
        return 1 + countTag(text,s)    #count 1 and repeat it
    else:
        return 0                       #if not found return 0
    
##########
##main####
##########

def displayMenu():

    choice = int(input("Please enter a choice: "))
    while (choice):
        if (choice == 1):
            a = int(input("Enter a number: "))
            print(countDigits(a))
        elif (choice == 2):
            n = int(input("Please enter the number of numbers: "))
            i = 1
            l1 = []
            while(i <= n):
                z = int(input("Enter the values of the list: "))
                l1.append(z)
                i += 1
            print(findMax(l1))
        elif (choice == 3):
            s1 = str(input("Please enter a code HTML: "))
            s2 = str(input("Please enter a tag to count: "))
            print(countTag(s1, s2))
        elif (choice == 4):
            break
        else:
            print("invalid choice")
        choice = int(input("Please enter your choiiiiiice: "))

displayMenu()