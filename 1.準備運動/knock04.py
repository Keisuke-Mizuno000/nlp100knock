str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

result = {}

words = str.split()

for i in range(len(words)):
    words[i] = words[i].strip(",.")
    if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
        result[words[i][0]] = i + 1
    else:
        result[words[i][:2]] = i + 1

print(result)

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

result = {}

one = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = sentence.split()

for i in range(len(words)):
    words[i] = words[i].strip(",.")

    if i + 1 in one:
        result[words[i][:1]] = i + 1
    else:
        result[words[i][:2]] = i + 1

print(result)