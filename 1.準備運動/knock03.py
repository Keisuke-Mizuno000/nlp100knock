str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

result = []

words = str.split()

result = [len(word.strip(",.")) for word in words]

print(result)

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

result = []

words = str.split()

for i in range(len(words)):
    words[i] = words[i].strip(",.")
    result += [len(words[i])]

print(result)