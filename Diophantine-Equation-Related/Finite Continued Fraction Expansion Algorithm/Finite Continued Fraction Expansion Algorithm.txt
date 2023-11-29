from math import floor
def finite_CFE(q,n):
    A_n, a_n = [q], [floor(q)]
    for i in range(1,n+1):
        A_i = 1 / (A_n[i-1]-a_n[i-1])
        A_n.append(A_i)
        a_n.append(floor(A_i))
        i+=1
    return a_n
