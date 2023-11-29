# Finite Continued Fraction Expansion Algorithm

## What it does:
Given some approximation of an irrational number and a natural number $n$, this algorithm outputs a proxy of the $n-th$ finite continued fraction convergent of the given irrational number, up to some error dependent on the accuracy of the given approximation.

## Sample application: 
Determine a proxy for the fifth finite continued fraction convergent of $\pi$ using the approximation $3.14159$.

### Solution:
```
CODES:
print(finite_CFE(3.14159,5))

TERMINAL OUTPUTS:
[3, 7, 15, 1, 25, 1]
```
The above code outputs a proxy to the fifth finite continued fraction convergents of $\pi$, which evaluates to $\frac{9563}{3044}\approx 3.14159001$.
We note that the fifth convergent of $\pi$ is $[3, 7, 15, 1, 292, 1]$ and evaluates to $\frac{104348}{33215}\approx 3.14159265$. 
Here, the proxy has an absolute error of $2.64078082\times 10^{-6}$ and a percent error of $8.40586641\times 10^{-5}$, which is trivially small given the approximation 3.14159.
