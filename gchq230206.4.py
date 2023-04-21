# Instead of looking for every combination in a single array of characters the script aligns characters from possible permutations of all combinations for multiple arrays of varying lengths. In the example from gchq the input string is “index”, and the script computes every possible combination for the given arrays then searches these combinations for the input string.

vocab = ["index"]

alpha = ["madison", "saturn", "do", "nitrogen", "exodus"]
alpha_1 = []
nu = []

index = 0

n = 1

while index < len(alpha):
    n *= len(alpha[index])
    nu.append(n)
    index += 1
    
index = 0
index_1 = 0
n_1 = n / nu[0]

while index < n:
    alpha_1.append(alpha[0][index_1])
    if index > 0 and (index % n_1) == 0:
        index_1 += 1
    index += 1
    
index = n
index_1 = 0
index_2 = 0

while index < n * len(alpha):
    n_1 = n /nu[index_1]
    
    alpha_1[index % n] += alpha[index_1][index_2%len(alpha[index_1])]
    
    if index > 0 and index % n == 0:
        index_1 += 1
        index_2 = 0
    
    if index > 0 and (index - index_1 * n) % n_1 == 0:
        index_2 += 1
    
    index += 1

print alpha_1

index = 0
index_1 = 0

while index < len(alpha_1):
    index_1 = 0
    while index_1 < len(vocab):
        if alpha_1[index] == vocab[index_1]:
            print vocab[index_1] + " found at " + str(index) + "/" + str(n)
        index_1 += 1
    index += 1
