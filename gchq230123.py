#strings = ["nom", "suet", "hurts", "fir", "sutra", "nus"]
strings = ["nom", "suet"]
days = ["monday", "tuesday", "thursday", "friday", "saturday", "sunday"]

combinations = []
N = []

index = 0
index_1 = 0 
index_2 = 0
index_1_1 = 0


while index < len(strings):
    combinations.append([])
    
    index_1 = 0
    
    index_2 = 1
    
    factorial = 1
    
    while index_2 <= len(strings[index]):
        factorial *= index_2
        index_2 += 1

    while index_1 < factorial:
        combinations[index].append([])
        
        index_1_1 = 0
    
        while index_1_1 < len(strings[index]):
            combinations[index][index_1].append(index_1_1)
            index_1_1 += 1
            
        index_1 += 1

    index += 1
    
index = 0

while index < len(combinations):
    print str(len(combinations[index])) + " combinations for " + days[index]
    index += 1
    
print combinations
