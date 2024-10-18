###########
####ex1####
###########

def enterTuple():
    x = int(input("Enter length: "))
    i = 0
    l1 = []
    while (i < x):
        y = input("Enter number: ")
        l1.append(y)
        i += 1
    tup1 = tuple(l1)
    return tup1

def sumTuples(tup1, tup2):
    if (len(tup1) != len(tup2)):
        print("Reenter tuples of same length")
        tup1 = enterTuple()
        tup2 = enterTuple()
    lst1 = list(tup1)
    lst2 = list(tup2)
    lst3 = []
    for i in range(len(lst1)):
        lst3.append(int(lst1[i]) + int(lst2[i]))
    tup3 = tuple(lst3)
    print(tup3)

##########
###ex2####
##########

def exportJSON(dict, n):
    with open ('n.json', 'w') as file:
        file.name == n
        content = dict
        print(file.name,"\n", content)

#########
###ex3###
#########

def importJSON(n):
    with open('n.json','r'):
        content = n.readlines()
        l1 = []
        l1.append() == content.split('\n')
        print(l1)

#########
##menu###
#########

def displayMenu():
    print("""1. Sum Tuples
2. Export JSON
3. Import JSON
4. Exit""")
    
    while (True):
        x = int(input("Please enter a choice: "))
        if (x == 1):
            tup1 = enterTuple()
            tup2 = enterTuple()
            sumTuples(tup1, tup2)
            displayMenu()

        elif(x == 2):
            x = int(input("enter number of elements: "))
            d = {}
            for i in range(x):
                key = input("enter key: ")
                value = input("enter value: ")
                d[key] = value
            m = input("enter name: ")
            exportJSON(d, m)
            displayMenu()

        elif(x == 3):
            a = input("Please enter name of JSON file: ")
            importJSON(a)
            displayMenu()

        elif (x == 4):
            break
        else:
            print("Invalid choice!")
            displayMenu()
        break

displayMenu()

###########
###prob2###
###########

# a. 1/6N + 8000N3 + 24 = 8000N3
# b. 1/6N3 
# c. 1/6N! + 200N4 = 1/6N!
# d. NlogN + 1000 = NlogN
# e. logN + N = N
# f. 1/2N(N-1) = 1/2N2
# g. N2 + 220NlogN2 + 3N + 9000 = 220NlogN2
# h. N! + 3N + 2N + N3 + N2 = N!
# from slowest to fastest: h/c/a/b/f/g/d/e