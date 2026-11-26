def n_gram(sequence, n):
    result = []

    for i in range(len(sequence) - n + 1):
        result.append(sequence[i:i+n])

    return result


sentence = "I am an NLPer"

tri_gram = n_gram(sentence.replace(" ", ""), 3)

words = sentence.split()
bi_gram = n_gram(words, 2)

print("文字tri-gram:")
print(tri_gram)
print("単語bi-gram:")
print(bi_gram)