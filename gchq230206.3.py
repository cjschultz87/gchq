vocab = ["index"]

alpha = ["madison", "saturn", "do", "nitrogen", "exodus"]
alpha_1 = []

index = 0

n = 1

while index < len(alpha):
    n *= len(alpha[index])
    index += 1
    
index = 0

while index < n:
    alpha_1.append(alpha[0][index%len(alpha[0])])
    index += 1
    
index = 1
index_2 = 0

while index < len(alpha):
    index_1 = 0
    
    n_1 = len(alpha_1)
    
    while index_1 < n_1:
        alpha_1[index_1] += alpha[index][index_1%len(alpha[index])]
        index_1 += 1
    
    index += 1

print alpha_1

index = 0

while index < len(alpha_1):
    if alpha_1[index] == vocab[0]:
        print vocab[0] + " found at " + str(index)
    index += 1