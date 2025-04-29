# Extraction of Digits Using Loops 
# Count Digit 
# Reverse a number 
# Check palindrome 
# Armstrong number 


# O (log10 (n))   due to loop of  //10

import math

def extraction_of_digits(num: int):
    n = num
    while n > 0:
        last_digit = n % 10
        print("Question ->")
        print("Last Latest Digit -> ",last_digit)
        n = n // 10 

extraction_of_digits(3762)

def count_of_digits(num: int):
    n = num
    count=0
    while n > 0:
        last_digit = n % 10
        count +=1
        n = n // 10 
    print("Question ->")
    print("The Count of this Digit is -> ", count)

count_of_digits(3762)

        

def count_of_digits_using_Log10(num: int):
    n = num
    logbase10 = math.log10(n)+1
    count = math.floor(logbase10)
    print("Question ->")
    print("The Count of this Digit using Log-Base-10 is -> ", count)

count_of_digits_using_Log10(3762)

        
        