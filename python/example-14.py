n = int(input())
word = {}
for _ in range(n):
    eng, latin = input().split(" - ")
    for idx in latin.split(", "):
        if idx in word:
            word[idx].append(eng)
        else:
            word[idx] = [eng]

print(len(word))
for key, val in sorted(word.items()):
    print(key, "-", ", ".join(val))
    
 
# from collections import defaultdict

# latin_to_english = defaultdict(list)
# for i in range(int(input())):
#     english_word, latin_translations_chunk = input().split(' - ')
#     latin_translations = latin_translations_chunk.split(', ')
#     for latin_word in latin_translations:
#         latin_to_english[latin_word].append(english_word)
    
# print(len(latin_to_english))
# for latin_word, english_translations in sorted(latin_to_english.items()):
#     print(latin_word + ' - ' + ', '.join(english_translations))

## Ref : https://snakify.org/en/lessons/dictionaries_dicts/problems/english_latin_dict/
