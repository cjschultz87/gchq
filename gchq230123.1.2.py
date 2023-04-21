# Work in progress, given an enumeration of characters from [0 n], lists the various combinations with replacement for an array of strings. (see gchq puzzle 10/04/23)

#strings = ["nom", "suet", "hurts", "fir", "sutra", "nus"]
strings = ["nom"]
days = ["monday", "tuesday", "thursday", "friday", "saturday", "sunday"]

combinations = []
A = []

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

    index_1 = 0
    
    bool = 0
    
    while bool == 0:
    
        index_1 = 0
        
        while index_1 < len(combinations[index]):
            index_2 = index_1 + 1
        
            while index_2 < len(combinations[index]):
            
                if combinations[index][index_1] == combinations[index][index_2]:
    
                    index_1_1 = 0
        
                    A = []
        
                    while index_1_1 < len(combinations[index][index_1]):
                        A.append(combinations[index][index_1][index_1_1])
                        index_1_1 += 1
        
                    combinations[index][index_1][0] = A[len(combinations[index][index_1]) - 1]
                    combinations[index][index_1][len(combinations[index][index_1]) - 1] = A[0]
                
                    
                
                    
                if combinations[index][index_1] == combinations[index][(index_2 + 1)%len(combinations[index])]:
                    index_1_1 = 0
                    
                    A = []
                    
                    while index_1_1 < len(combinations[index][index_1]):
                        A.append(combinations[index][index_1][index_1_1])
                        index_1_1 += 1
                        
                    index_1_1 = 0
                    
                    while index_1_1 < len(combinations[index][index_1]):
                        combinations[index][index_1][index_1_1] = A[(index_1_1 + 1)%len(A)]
                        index_1_1 += 1
                
                
                
                print combinations
            
                index_2 += 1
                
            
            index_1 += 1
    
    index += 1
    
print combinations
