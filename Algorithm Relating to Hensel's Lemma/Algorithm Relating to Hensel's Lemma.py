def bash(p,a,n):
    _, epsion = 0,1
    while True: 
        if (_**2-a) % p == 0: #Determining b_1
            L=[_]
            break
        _+=1
    for j in range(1,n+1):
        B_j = L[j-1]  #b_{j-1}
        while True:
            numerator = (2*B_j*epsion) - a + (B_j**2)
            if numerator % p**j==0:
                b_j = B_j + epsion
                L.append(b_j)
                break
            epsion+=1
    print(f"b_{n} = {L[n]}, where {L[n]}^2 ≡ {a} (mod {p}^{n})")
