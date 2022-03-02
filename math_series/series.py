def FibRecursion(n):  
    if n == 0:  
       return 0  
    elif n== 1 : 
       return 1
    else:
       return(FibRecursion(n-1) + FibRecursion(n-2)) 



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






