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
(8, 1)
(39, 5)
(164, 21)
(453, 58)
(1523, 195)
(5639, 722)
(29718, 3805)
(469849, 60158)
(2319527, 296985)
(9747957, 1248098)
(26924344, 3447309)
(90520989, 11590025)
