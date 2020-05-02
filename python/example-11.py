n = int(input()) 
arr = [['.']*n for idx in range(n)]
for x in range(n):
    for y in range(n):
        if x == y:
            arr[x][y] = "*"
        elif y == n - 1 - x:
            arr[x][y] = "*"
        elif x == n // 2 or y == n // 2:
            arr[x][y] = "*"
        print(arr[x][y], end = " ")
    print(" ")
    
#n = int(input())
#arr = [['.'] * n for idx in range(n)]
#for idx in range(n):
#    arr[idx][idx] = '*'
#    arr[n // 2][idx] = '*'
#    arr[idx][n // 2] = '*'
#   arr[idx][n - idx - 1] = '*'
#for row in arr:
#    print(' '.join(row))

## Ref : https://snakify.org/en/lessons/two_dimensional_lists_arrays/problems/snowflake/
