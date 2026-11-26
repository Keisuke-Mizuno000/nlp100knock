def n_gram(sequence, n):
    result = []

    for i in range(len(sequence) - n + 1):
        result.append(sequence[i:i+n])

    return result

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(n_gram(str1, 2))
Y = set(n_gram(str2, 2))


print("X =", X)
print("Y =", Y)
print("\n")

print("和集合 =", X | Y)
print("積集合 =", X & Y)
print("差集合 =", X - Y)

print("'se'はXに含まれるか:", "se" in X)
print("'se'はYに含まれるか:", "se" in Y)