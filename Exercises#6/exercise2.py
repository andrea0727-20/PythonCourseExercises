import math

def isNumberPrime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True   

def findPrimeNumber(limit):
     print(f"The numbers prime until the limit {limit} is: ")
     for i in range(2,limit + 1):
         if isNumberPrime(i):
             print(i, end = " ")

findPrimeNumber(60)