# Magic Box Algorithm

## What it does:
Given a finite continued fraction of the form $[a_0, a_1, ..., a_m]$ and an integer n such that $m\geq n\geq 0$, this algorithm outputs a rational number $\frac{p}{q}$, in the form $(p,q)$, such that $\frac{p}{q} = [a_0, a_1, ..., a_n]$. 

## Sample application: 
Given the 12-th continued fraction convergent of $\pi$, $f=[3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14]$, evaluate its n-th continued fraction convergents, for $n=0,1,\dots, 12$.

### Solution
```
CODES:
f, n =   [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14], 0
while n < len(f):    
    print(magic_box(f,n))
    n+=1

TERMINAL OUTPUTS:
(3, 1)
(22, 7)
(333, 106)
(355, 113)
(103993, 33102)
(104348, 33215)
(208341, 66317)
(312689, 99532)
(833719, 265381)
(1146408, 364913)
(4272943, 1360120)
(5419351, 1725033)
(80143857, 25510582)
(104348, 33215)
