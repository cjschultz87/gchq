# Instead of looking for every combination in a single array of characters the script aligns characters from possible permutations of all combinations for multiple arrays of varying lengths. In the example from gchq the input string is “index”, and the script computes every possible combination for the given arrays then searches these combinations for the input string.

vocab = ["index"]

alpha = ["madison", "saturn", "do", "nitrogen", "exodus"]
alpha_1 = []
alpha_2 = []
iota = []

index = 0
n = 1

while index < len(alpha):
    n *= len(alpha[index])
    
    index += 1

index = 0

while index < len(alpha[0]):
    index_1 = 0
    
    while index_1 < len(alpha[1]):
        alpha_1.append(alpha[0][index])
        index_1 += 1

    index += 1
    
index = 0

while index < len(alpha_1):
    alpha_1[index] += alpha[1][index % len(alpha[1])]
    index += 1
    
index = 0

n_1 = len(alpha_1)

while index < n_1:
    alpha_1.append(alpha_1[index])
    index += 1
    
index = 0

while index < len(alpha_1) / len(alpha[2]):
    alpha_1[index] += alpha[2][0]
    index += 1

while index < len(alpha_1):
    alpha_1[index] += alpha[2][1]
    index += 1


print alpha_1
