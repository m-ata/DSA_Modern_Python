

# TC -> O ( N  +  M)
# SC -> O(26) -> (1)

s = "abcdefklsjowjnsnkxz"
m = ['a', 'b', 'a', 'f', 'f', 'x', 'z', 'z', 'z']

hash_list_char= [0]*26
# Prestoring 

def hashing_char_02():
    for char in s :
        aschi_char = ord(char)  # giving asschi or char
        index = aschi_char -97   # all small alphabet from 97-122
        hash_list_char[index] +=1
    print(hash_list_char)
    
    for char in m:
        aschii_in_m =ord(char)
        index = aschii_in_m  - 97
        if char in hash_list_char:
            print(hash_list_char[index])
        
        
hashing_char_02()