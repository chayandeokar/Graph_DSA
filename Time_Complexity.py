#Question1
    def foo(array):
        sum = 0   #=> O(1)
        product = 1   #=> O(1)
        for i in array:   #=> O(n)
            sum += i
        for i in array:   #=> O(n)
            product *= i
        print("Sum = "+str(sum)+", Product = "+str(product))   #=> O(1)
    
    ar1 = [1,2,3,4]
    foo(ar1)

Answer --> Total time complexity --> 0(n)


#Question2

def printPairs(array):
    for i in array:  #=> O(n)
        for j in array:  #=> O(n)
            print(str(i)+","+str(j))  #=> O(1)

Answer --> Total time complexity --> 0(n^2)


#Question3
def printUnorderedPairs(array):
    for i in range(0,len(array)): #=> O(n)
        for j in range(i+1,len(array)): #=> O(n)
            print(array[i] + "," + array[j]) #=> O(1)

Answer --> Total time complexity --> 0(n^2)


#Question4
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):  #=> O(n)
        for j in range(len(arrayB)): #=> O(m)
            if arrayA[i] < arrayB[j]: #=> O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j])) #=> O(1)

arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]

Answer --> Total time complexity --> 0(n^m)

#Question5
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)): #=> O(n)
        for j in range(len(arrayB)): #=> O(m)
            for k in range(0,100000): #=> O(100000)
                print(str(arrayA[i]) + "," + str(arrayB[j])) #=> O(1)

# printUnorderedPairss(arrayA,arrayB)

Answer --> Total time complexity -->  O(n * m * 100,000)


#Question6
def reverse(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse(arrayA)

Answer --> Total time complexity --> O(n) or O(n/2)


#Question7
def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

Answer --> Total time complexity --> 

#Question8
def allFib(n):
    for i in range(n):
        print(str(i)+":, " + str(fib(i)))

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

allFib(4)

Answer --> Total time complexity --> 


#Question10
def powersOf2(n):
    # print("n:"+str(n))
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(int(n/2))
        # print("prev:"+str(prev))
        print(prev)
        curr = prev*2
        print(curr)
        return curr

powersOf2(50)

Answer --> Total time complexity --> 
