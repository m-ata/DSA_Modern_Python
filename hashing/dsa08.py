
n = [1,2,3,5,7,8,2,14,4,7,3,2,6,8,4,3,5,0,6,4,2]  #checking this number n in m if yes so increase hash list index 
m = [1, 6, 11, 16,6, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
hash_list= dict()
# with dictionary 

def hashing03():
    
    for num in n:
        if num in m:
            hash_list[num] = hash_list.get(num,0)+1
    print(hash_list)
    
hashing03()