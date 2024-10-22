


numbers = [12, 7, 19, 24, 5, 17, 28, 13]

def prime(number):
    primes=[]
    
    for num in number:
        if num > 1:
            flag = True
            for i in range(2,int(num**0.5)+1):
                if(num % i ==0):
                    flag=False
                    break
            if flag:
                primes.append(num)
    return primes

prime_num=prime(numbers)
print(prime_num)






