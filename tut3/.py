# RECURSION AND ITERATION 
#Q1
def fact(n):
    if n <= 1: 
        return 1 
    else: 
        return n * fact(n-1)

def sum_even_factorials(n): 
    if n < 0:        #practise to put base case alw first in a recursive call 
        return 0 
    elif n % 2 == 0: 
        return fact(n) + sum_even_factorials(n-2) #thats why fact(n) must be added before, so py knows what to do 
    else:
        return sum_even_factorials(n-1)

  #QNS 3
def star_wars_function(num_enemy_ships):
    if num_enemy_ships == 0: 
        return ""          # base case must return a string
    if num_enemy_ships % 2 == 0:
        return '*--' + star_wars_function(num_enemy_ships - 1)
    else:  
        return '*-' + star_wars_function(num_enemy_ships - 1)

#QNS 4 
def compute_total(amount, m):
    for month in range(1, m + 1): #remember, range is inconclusive of m+1
        rate = 0.02
        if month % 4 == 0:
            rate = 0.03
        if amount > 50000:
            rate += 0.0005
        amount = amount * (1 + rate / 12)   #not using compounded interest formula but iteratively, each month’s interest is added for the next month
    return round(amount, 2) #round to 2 dp 
 #wrong ans    
def compute_total(amount, m):
    i = 0.02
    if amount > 5000:
        i += 0.0005
    if m % 4 == 0:
        i = 0.03
     amount *= (1 + i/12) ** m #cannot use this formula since it assumes constant interest rate for all months, however thats not the case since there are exceptions for different months/amt>50000
    return round(amount,2) 


