import random

def shuffle_word(word):
    if len(word) <= 4:
        return word

    middle = list(word[1:-1])
    random.shuffle(middle)

    return word[0] + ''.join(middle) + word[-1]


text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = text.split()

result = []

for word in words:
    result.append(shuffle_word(word))

print(' '.join(result))