word = str(input()).split(" ")
for idx in word:
    print(idx.capitalize(), end =" ")
    
 ## Ref : https://snakify.org/en/lessons/functions/problems/capitalize/


# def capitalize(word):
#     first_letter_small = word[0]
#     first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
#     return first_letter_big + word[1:]

# source = input().split()
# res = []
# for word in source:
#     res.append(capitalize(word))
# print(' '.join(res))
