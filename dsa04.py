
# Print all factor of a given number

# For Complete Loop
# TO  -> O(N) 
# SC -> O(k)  ->  k would be the number of factor in factror list 

# With optimize timing in looping 
from math import sqrt
import math
import time

def format_time(seconds: float) -> str:
    if seconds >= 1:
        return f"{seconds:.1f} sec"
    elif seconds >= 0.001:
        return f"{seconds * 1000:.1f} ms"
    else:
        return f"{seconds * 1_000_000:.1f} µs"

print("\n-----Solution Complete Loop to (num)--------")

def print_all_factor(num:int):
    n=num
    factor_list=[]
    start_time = time.perf_counter()
    for i in range(1,num+1):
        if(num % i==0):
            factor_list.append(i)
            # print(i)
    end_time=time.perf_counter()
    print(f"Factor List of {num} ",factor_list)
    print(f"Time Taken to Find solution of {num} ,{format_time(end_time - start_time)}")
    print("\n-------------")

    
    


print_all_factor(20)
print_all_factor(50)
print_all_factor(53)

print("\n ************")

print("\n-----Optimal Solution 1/2(num)--------")
# For Half Loop
# TO  => O(N/2) => O(N * 1/2)  => 1/2 negligible ~= apprx O(N)  
# SC -> O(k)  ->  k would be the number of factor in factror list 


def print_all_factor_optimize_to_half(num : int):
    n=num
    factor_list_optimize=[]
    start_time = time.perf_counter()

    for i in range(1,n//2 ):
        if(n % i ==0):
            factor_list_optimize.append(i)
    factor_list_optimize.append(num)
    end_time=time.perf_counter()
    print(f"Factor List with Optimize Half Loop algo of {num} ",factor_list_optimize)
    print(f"Time Taken to Find solution of {num} ,{format_time(end_time - start_time)}")
    print("\n-------------")

print_all_factor_optimize_to_half(20)
print_all_factor_optimize_to_half(50)
print_all_factor_optimize_to_half(53)
        
        
        
# Most Optimal solution for Finding Factor of a given number > U_multide Method
print("\n-----Most Optimal Solution SqRoot(num)--------")
# For Sqr-Root Loop
# TO  => Loop -> O(Sqrt(N)) AND Sorting -> O(N Log(N)) => O(Sqrt(N))+O(N log(N))   
# SC -> O(k)  ->  k would be the number of factor in factror list 


def u_multide(num:int):
    n = int(num)
    optimal_factor_list=[]
    start_time = time.perf_counter()

    for i in range(1 , math.floor(sqrt(n))+1):
        
        if n%i==0:
            
            divisible_digit = n//i
            optimal_factor_list.append(i)
            
            if n //i != i:
                optimal_factor_list.append(divisible_digit)
    end_time=time.perf_counter()

    print(f"Factor List with Optimize Half Loop algo of {num} ",sorted(optimal_factor_list))
    print(f"Time Taken to Find solution of {num} ,{format_time(end_time - start_time)}")
    print("\n-------------")

u_multide(36)
u_multide(20)
u_multide(50)
u_multide(53)
        