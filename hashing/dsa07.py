

n = [2,3,5,7,8,2,14,4,7,3,2,6,8,4,3,5,0,6,4,2]  #checking this number n in m if yes so increase hash list index 
m = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
hash_list=[0] * 11


# constraints The pre-Store List not be exceed 10 values
def hashing02():
    
    for num_to_chk in n:
        for num_to_match in m:
            if num_to_chk == num_to_match:
                hash_list[num_to_chk] += 1
                
    print(hash_list)

    
    
    
hashing02()
