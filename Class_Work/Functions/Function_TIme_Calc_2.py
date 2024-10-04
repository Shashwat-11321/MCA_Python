## Write a finction that takes one input parameter (n) and evaluate an expression a = n* 10 , for all values 0 to n 

import time
ns=[123456,3456743,45622145,1345636657]
def calc(n):
    for i in range(0,n):
        a = i* 10

def wrapper(func , n):
    start = time.time() * 100000

    func(n)
    end = time.time() * 100000

    print(f"For n = {n} \n Execution time is {end - start } micro sec")

for n in ns:
    wrapper(calc,n)