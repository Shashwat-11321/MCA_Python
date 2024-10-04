## Write a finction that takes one input parameter (n) and evaluate an expression a = n* 10 , for all values 0 to n 

import time

def calc(n):
    for i in range(0,n):
        a = i* 10

n = int(input("Enter a numer"))

# estimate executing time of this function for n 
start_time=time.time() * 1000

print(calc(n))
end_time = time.time() * 1000


print(f"For n ={n} \n execution tme is {end_time - start_time}")
