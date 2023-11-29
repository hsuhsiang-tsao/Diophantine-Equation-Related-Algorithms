from math import ceil, floor, sqrt 

def reduced_form(D,mode="Semi-reduced"):
    if not D%4==0 and not D%4==1 or D>=0:
        print("Invalid Input. Please ensure D is 0 or 1 (mod 4) and negative.")
        return
    upper_bound, output  = ceil(sqrt(-D/3)), []
    A = [x for x in range(1,upper_bound+1) if x <= upper_bound]
    B = [0] + A + [-a for a in A]
    for a in A:
        for b in B:
            c = (b**2-D)/(4*a)
            if c == floor(c) and abs(b)<=a<=c:
                c = int(c)
                output.append([a,b,c])
    if mode=="Reduced":
        output = [f for f in output if abs(f[1])!=f[0] and f[0]!=f[2] or f[1]>=0]
        #a = f[0]   b = f[1]    c = f[2]
    return output
