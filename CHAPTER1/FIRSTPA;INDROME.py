def check(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True 
words = ["abc","car","ada","racecar","cool"]
for word in words:
    if check(word):
         print(word)
         break
print('') 
"""def first_palindromic_string(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""
words = ["abc", "car", "ada", "racecar", "cool"]
print(first_palindromic_string(words))"""  
