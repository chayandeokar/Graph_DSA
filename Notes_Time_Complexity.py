def findBiggestNumber(ar):
    biggestNumber = ar[0]       #=> O(1)
    for index in range(1,len(ar)):  #=> O(n) O(n)
        if ar[index] > biggestNumber: #=> O(1) O(1)
            biggestNumber = ar[index] #=> O(1)
    print(biggestNumber)    #=> O(1)

#Time complexity/Runtime: O(1) + O(n) + O(1) => O(n)
ar = [3,6,7,8,2,9]
findBiggestNumber(ar)

# How to measure the codes using Big O?
'''
Rule 1: Any assignment statements and if statements that are executed once => O(1)
Rule 2: A simple "for" loop from 0 to n (with no internal loops) => O(n)
Rule 3: A nested loop of the same type => O(n2)
Rule 4: A loop, in which the controlling parameter is divided by two at each step => O(logN)
Rule 5: When dealing with multiple statements just add add them.



O(1) - Constant - Accessing a speicific element in array
ar = [1,4,6,3,9,2]
print(ar[1])

O(n) - Linear - Loop through array elements
ar = [1,4,6,3,9,2]
for i in ar:
    print(i)
# Linear time since it is visiting array elements at least one.

O(logN) - Logarithmic - Find an element in sorted array
ar = [1,4,6,3,9,2]
for i in range(0,len(ar),2):
    print(ar[i])
# logarithmic time since it is visiting only some elements

O(n2) => Quadratic - visiting array a every index in the array twice
ar = [1,4,6,3,9,2]
for i in ar:
    for j in ar:
        print(i,j)

O(2n) - Exponential - Double recurssion is Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)




'''
arr = [3,5,7,6,8,3]
arr1 = [13,15,27,16,8,73]
#program 1
for a in arr: 
    print(a)

for b in arr1:
    print(b)

#Runtime Add the runtimes: O(a+b)

#program 2
for a in arr:
    for b in arr1:
        print(a,b)

# Runtime: Multiply the runtimes: O(a*b)
