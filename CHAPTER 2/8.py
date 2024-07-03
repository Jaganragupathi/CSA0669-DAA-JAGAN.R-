def substring_words(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break  
    return result
words = ["mass", "as", "hero", "superhero"]
output = substring_words(words)
print("Output:", output)
 
