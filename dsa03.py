
# O (log10 (n))   due to loop of  //10



def arm_strong_num (num:int):
    orignal = num
    result=0
    length = len(str(num))    
    while num > 0:
        last_digit =  num %10
        result = (last_digit**length) + result
        num = num //10
    
    
    print("The Armstrong Value ->", result)

    if result == orignal:
        print("It's a Arm Strong number :", orignal, "==", result)
    else:
        print("It's not a Arm Strong number :", orignal, "!=", result)
    print("\n-----------")
            

arm_strong_num(153)
arm_strong_num(1634)
arm_strong_num(163)