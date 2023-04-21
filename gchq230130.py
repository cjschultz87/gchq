L_0 = ["a","b","c","d","e","f","g"]
L_1 = ["q","r","s","t"]
L_2 = ["v","w","x"]
L_3 = ["z"]
R_0 = ["h","i","j","k","l","m","n","o","p"]
R_1 = ["u"]
R_2 = ["y"]

L = [L_0,L_1,L_2,L_3]
Lambda = []

R = [R_1,R_2]
Ro = []

index = 0

while index < len(L):
    index_1 = 0
    
    while index_1 < len(L[index]):
        Lambda.append(L[index][index_1])
        
        index_1 += 1
    index += 1
    
index = 0

while index < len(R):
    index_1 = 0
    
    while index_1 < len(R[index]):
        Ro.append(R[index][index_1])
        
        index_1 += 1
    index += 1
    
p = "12"
p_n = len(p)

Pi = []

Lambda_c = pow(len(Lambda), p_n)
Ro_c = pow(len(Ro), p_n)

index = 0

while index < Ro_c:
    print "populating array: " + str(index) + "/" + str(Ro_c)
    Pi.append([])
    index += 1
    
index = 0
c_Pi = []

while index < p_n:
    c_Pi.append(0)
    index += 1

index = 0
index_2 = 0
index_2_1 = 0
index_3_0 = 0
index_3_1 = 0

while index < len(Pi):
    print "combination: " + str(index + 1) + "/" + str(len(Pi))
    
    print c_Pi
    
    index_1 = 0
    
    while index_1 < p_n:
        Pi[index].append(Ro[c_Pi[index_1]])
        
        index_1 += 1
 
    index_3_1 += 1
    
    if index_3_1 == len(Ro):
        index_3_1 = 0
        #c_Pi[index_3_0] = index_2
        index_3_0 += 1
        if index_3_0 == len(c_Pi):
            index_3_0 = 0
            index_2 += 1
            
    if c_Pi[index_3_0] == len(Ro) - 1:
        c_Pi[index_3_0] = index_2

        
    c_Pi[index_3_0] += 1
    
    print Pi[index]
    
    index += 1
    
index = 0

conflicts = 0

while index < len(Pi) - 1:
    index_1 = index + 1
    
    while index_1 < len(Pi):
        if Pi[index] == Pi[index_1]:
            conflicts += 1
            
            break
            
        index_1 += 1
    index += 1

print "conflicts: " + str(conflicts)

print "|" +  p + "| = " + str(p_n)
    
print Lambda
print "|Lambda| = " + str(len(Lambda))
print "combinations = " + str(Lambda_c)

print Ro
print "|Ro| = " + str(len(Ro))
print "combinations = " + str(Ro_c)

