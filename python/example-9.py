num_list = [int(idx) for idx in input().split(" ")]
get_unique = set(num_list)
print(max(get_unique), num_list.index(max(get_unique)))

## Ref : https://snakify.org/en/lessons/lists/problems/maximal_element/
