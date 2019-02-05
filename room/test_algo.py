array = [1, 3, 5, 6, 8, 1]

output = []
for s in range(1, len(array)):
    for i in range(0, s):
        output.append([])