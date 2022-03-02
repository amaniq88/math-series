"""
*****  fibonacci *******
is  function  have one parameter n. The function  return the nth value in the fibonacci series.
where fibonacci(0) == 0, fibonacci(1) = 1

***** lucas **********
is  function  have one parameter n. The function  return the nth value in the fibonacci series.
where lucas(0) == 2, lucas(1)  = 1

***** sum_series **********
is  function  have one parameter n and two parameter with default value (0,1).
 The function  return the nth value in the fibonacci series.
where sum_series(0) == first_default_value , sum_series(1)  = scond_default_value 
if the user not spesify any value it will use the deafult

"""
def fibonacci(n):  
    if n == 0:  
       return 0  
    elif n== 1 : 
       return 1
    else:
       return(fibonacci(n-1) + fibonacci(n-2)) 



def lucas(n):
    if n == 0:  
       return 2  
    elif n== 1 : 
       return 1
    else:
       return(lucas(n-1) + lucas(n-2))  

def sum_series(n, num= 0, nn= 1):
    if n == 0: 
       print(num) 
       return num  
    elif n== 1 :
       print(nn) 
       return nn
    else:
       return(sum_series(n-1 ,num , nn ) + sum_series(n-2 , num , nn)) 






