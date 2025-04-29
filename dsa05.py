# Store Frequency in Dictionary


# Method 01 
# TC => All dict operating O (log(N)) 
def method01(lst_num:list):
    dictionary = dict() | {}
    length_Of_list = len(lst_num)
    for i in range (0, length_Of_list):
        if lst_num[i] in dictionary:
            dictionary[lst_num[i]]+=1
        else:
            dictionary[lst_num[i]]=1
    print("Method 02 ->",dictionary.items())



method01([1,2,4,3,4,3,2,9,5,7,8,2,7,0,5,3,2,2,4,6,4])


# Method 02
# TC => All dict operating O (log(N)) 
def method02(lst_num:list):
    dictionary = dict() | {}
    length_Of_list = len(lst_num)
    for i in range(0,length_Of_list):
        dictionary[lst_num[i]]= dictionary.get(lst_num[i],0)+1
    print("Method 02 ->",dictionary.items())



method02([1,2,4,3,4,3,2,9,5,7,8,2,7,0,5,3,2,2,4,6,4])