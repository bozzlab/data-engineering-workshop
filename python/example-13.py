n = int(input())
president = {}
for _ in range(n):
    key, val = input().split(" ") 
    president[key] = president[key] + int(val) if key in president else int(val)

for idx in sorted(president):
    print(idx, president[idx])
    
    
# num_votes = {}
# for _ in range(int(input())):
#     candidate, votes = input().split()
#     num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)

# for candidate, votes in sorted(num_votes.items()):
#     print(candidate, votes)
   
## Ref : https://snakify.org/en/lessons/dictionaries_dicts/problems/usa_elections/
