# // Given a positive integer num, return the sum of all odd Fibonacci numbers that are less than or equal to num.
# // The first two numbers in the Fibonacci sequence are 1 and 1. Every additional number in the sequence is the sum of the two previous numbers. The first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.
# // Test Cases:
# // fibOddAddition(4) // 5
# // fibOddAddition(13) // 23
# // fibOddAddition(1000)) // 1785
# // fibOddAddition(75025) // 135721

# check in fib seq if the num is even or odd. keep the odd num 
# check if the nums are less the the given input num -> add nums 

def function(num):

    fib = [1,1,2]

    # print(fib[-2])


    while fib[-1] <= num:

        newFibNumber = fib[-1] + fib[-2] 

        fib.append(newFibNumber)

    sum = 0

    # for fibNum in fib :
    #     if fibNum <= num and fibNum % 2 != 0:
    #         sum = sum + fibNum

    return [num*2 for num in fib if num % 2 != 0]

print (function(13))

# // fibOddAddition(4) // 5
# // fibOddAddition(13) // 23
# // fibOddAddition(1000)) // 1785
# // fibOddAddition(75025) // 135721