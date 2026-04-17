sentence = "Functional programming in Python is very powerful and elegant"

words = sentence.split()

sorted_words = list(sorted(words, key=lambda word: len(word)))

result = sorted_words[-3:]

print(result)
