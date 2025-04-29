# Palindrome   O (log10 (n))   due to loop of  //10


def check_palindrome(num: int):
    original = num  
    result = 0
    while num > 0:
        last_digit = num % 10
        result = result * 10 + last_digit
        num = num // 10
    
    print("The Reverse Value ->", result)

    if result == original:
        print("It's a Palindrome:", original, "==", result)
    else:
        print("It's not a Palindrome:", original, "!=", result)

check_palindrome(12345)
check_palindrome(786687)
