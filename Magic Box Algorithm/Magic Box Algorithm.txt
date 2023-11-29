#Given a continued fraction of the form [a_0, a_1, ..., a_m] and an integer n such that m>=n>=0, output p/q such that p/q = [a_0, a_1, ..., a_n] 
import math

def magic_box(List,n):
    if n> len(List)-1 or n<0:
        return f"Please ensure n is less than or equal to {len(List)-1} and greater than or equal to 0."
    if not(isinstance(List[0], int)) or not(isinstance(n, int)): 
        return "Please ensure a_0, n are integers."
    for _ in range(1,len(List)):
        if List[_] <=0 or not(isinstance(List[_], int)):
            return "Please ensure a_1,a_2,...,a_m are positive integers."
    h, k, i = [0,1], [1,0], 2
    while i <n+3:
        h_i, k_i = List[i-2]*h[i-1]+h[i-2], List[i-2]*k[i-1]+k[i-2]
        h.append(h_i)
        k.append(k_i)
        i+=1
    return (h[n+2],k[n+2])
