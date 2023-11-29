# Reduced Binary Quadratic Forms Finder

## What it does:
Given a negative integer D which is either $0$ (mod $4$) or $1$ (mod $4$), this algorithm outputs all semi-reduced or reduced binary quadratic forms $ax^2 + bxy + cy^2$ with discriminant D, in the form $[a, b, c]$.

## Sample application: 
Determine all reduced binary quadratic forms $ax^2 + bxy + cy^2$ with discriminant D=-167.

### Solution:
```
print(reduced_form(-167,"Reduced"))

TERMINAL OUTPUTS:
[[1, 1, 42], [2, 1, 21], [2, -1, 21],[3, 1, 14], [3, -1, 14], [4, 3, 11], 
[4, -3, 11], [6, 1, 7], [6, 5, 8], [6, -1, 7], [6, -5, 8]]

```
