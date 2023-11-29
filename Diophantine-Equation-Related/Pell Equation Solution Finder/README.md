# Pell Equation Solution Finder

## What it does:
Given some integer $d$ and a maximum number of iterations $max$, this algorithm determines integer solutions $(x,y)$ to a Pell equation of the form $x^2 - dy^2 =2$ 

## Sample application: 
Find some integer solutions to the Pell equation $x^2-34y^2=2$.

### Solution: 
```
print(pell_equation_1(34,2000000))

TERMINAL OUTPUTS:
Maximum iterations: 2000000
[(6, 1), (414, 71), (28974, 4969), (2027766, 347759)]
```
