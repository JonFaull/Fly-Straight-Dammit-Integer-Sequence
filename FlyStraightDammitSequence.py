from math import gcd
from matplotlib import pyplot as plt 


n = list(range(0, 1000)) #get list of integers (0 - 1000)
numbers = [1, 1] 

for i in n:
    
    if i >= 2:
        if gcd(int(numbers[-1]), i) == 1: #determine if gcd between two numbers is equal to one. 
            a_of_n = numbers[-1] + (i + 1) #create a of n value 
            numbers.append(a_of_n) #append to list 
        else:
        
            GreaterCommonDenom = gcd(int(numbers[-1]), i) 
            a_of_n = numbers[-1]/GreaterCommonDenom
            numbers.append(int(a_of_n))
    
plt.scatter(n, numbers) #graph 
plt.show()

print(n)   
print(numbers)

    
    
    
    

