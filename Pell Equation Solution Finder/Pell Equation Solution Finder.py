#Solving equations of the form x^2 - dy^2 =2
import math

def pell_equation_1(d,start=1,end=1000):
    _, sol = start, []
    while _ < end:
        x = math.sqrt((d*(_**2))+2)
        if x==int(x): sol.append((int(x),_))
        _+=1
    print(f"start: {start}; end: {end}")
    return sol
