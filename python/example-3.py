year = int(input())

if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
    print("LEAP")
else: 
    print("COMMON")
    
## Reference : https://snakify.org/en/lessons/if_then_else_conditions/problems/leap_year/
