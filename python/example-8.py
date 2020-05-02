n = int(input())
base, pwr = 2, 1
while base <= n:
    base *= 2
    pwr += 1
print(pwr - 1, base//2)

## Ref : https://snakify.org/en/lessons/while_loop/problems/powers_of_two/
