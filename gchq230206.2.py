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