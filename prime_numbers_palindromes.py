#!/usr/bin/python3

import math

MIN_N = 10000
MAX_N = 100000

def search_for_prime_numbers(min_n=MIN_N, max_n=MAX_N):
    '''
    Finds prime numbers in the range from min to max
    '''
    # Write out all odd integers from min_n to max_n.
    list_prime_numbers = [i for i in range(min_n, max_n) if i % 2 != 0] 

    # Sort out the numbers from 3 to sqrt (max_n)
    for i in range(3, int(math.sqrt(max_n))):
    
    # Subtract numbers multiples of unpainted
        for j in range(i * 2, max_n, i):        
            if j in list_prime_numbers:
                list_prime_numbers.remove(j)
    return list_prime_numbers

def is_palindrom(number):
    '''
    Checks if the number is a palindrome
    '''
    num = str(number)
    num_reverse = num[::-1]
    if num == num_reverse:
        return True
    return False

def main():
    '''
    Finds the largest number of palindromes, 
    which is the product of two simple five-digit numbers, 
    as well as the factors themselves
    '''
    
    # We find prime numbers in the range from MIN_N to MAX_N
    list_prime_numbers = search_for_prime_numbers() 
    
    # Dictionary for the recording of palindromes
    palindroms_composition = {}
    
    # The index of the second factor
    number_2 = 0
    
    # Multiplying prime numbers to find palindromes
    for number_1 in range(len(list_prime_numbers)):        
        for number_2 in range(len(list_prime_numbers)):
            composition = list_prime_numbers[number_1] * list_prime_numbers[number_2]
           
            # If is a palindrome, we add it to the dictionary
            if is_palindrom(composition):
                palindroms_composition[composition] = ' = ' + str(list_prime_numbers[number_1]) + ' * ' + str(list_prime_numbers[number_2])
        number_2 += 1
    
    # Determine the largest number of palindrome
    max_palindrom = max(palindroms_composition.keys())

    print(max_palindrom, palindroms_composition[max_palindrom])
                    

if __name__ == "__main__":
    main()
