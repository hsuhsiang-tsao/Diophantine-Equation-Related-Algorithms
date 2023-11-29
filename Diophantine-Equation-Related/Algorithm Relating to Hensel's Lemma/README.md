# Algorithm Relating to Hensel's Lemma

## What it does:
Given some small odd prime number $p$, an integer $a$ such that $a$ (mod $p$) is a quadratic residue, and a natural number (precision level) $n$, this algorithm outputs some integer $b$ such that $b^2 \equiv a$ (mod $p^n$), utilizing Hensel’s Lemma. 

## Sample application: 
Given a prime number $p=7$ and an integer $a=2,$ determine some integers $b_n$ such that ${b_n}^2\equiv 2$ (mod 7^n) for $n=1,2,3,4,5$.


### Solution:
```
CODES:
bash(p=7,a=2,n=1)
bash(p=7,a=2,n=2)
bash(p=7,a=2,n=3)
bash(p=7,a=2,n=4)    
bash(p=7,a=2,n=5)

TERMINAL OUTPUTS:
b_1 = 10, where 10^2 ≡ 2 (mod 7^1)
b_2 = 59, where 59^2 ≡ 2 (mod 7^2)
b_3 = 108, where 108^2 ≡ 2 (mod 7^3)
b_4 = 2166, where 2166^2 ≡ 2 (mod 7^4)
b_5 = 4567, where 4567^2 ≡ 2 (mod 7^5)
```
