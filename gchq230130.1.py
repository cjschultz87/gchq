#Given a class of characters C the number of possible combinations of those characters for a string of length n is |C|^n. Each combination is computed and the entire array is searched for a match to the given input string (e.g. “pi” is combination eighty eight out of one hundred twenty one). Using a (logical) cascade allows the script to cycle through every permutation.

L_0 = ["a","b","c","d","e","f","g"]
L_1 = ["q","r","s","t"]
L_2 = ["v","w","x"]
L_3 = ["z"]
R_0 = ["h","i","j","k","l","m","n","o","p"]
R_1 = ["u"]
R_2 = ["y"]

L = [L_0,L_1,L_2,L_3]
Lambda = []

R = [R_0,R_1,R_2]
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
    
p = "pumpkin"
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
c_Pi_1 = []

while index < p_n:
    c_Pi.append(0)
    c_Pi_1.append(0)
    index += 1
    

index = 0
index_1 = 0
index_2 = 0
index_2_2 = 0
index_2_1 = 0
index_3_0 = 0
index_3_1 = 0
index_4_0 = 0
index_4_1 = 0

while index < len(Pi):
    print "combination: " + str(index + 1) + "/" + str(len(Pi))
    
    index_4_0 = 0
    index_4_1 = index_4_0 + 1
    ###
    #while index_4_0 < len(Pi) - 1:
    #    index_4_1 = index_4_0 + 1
    #    while index_4_1 < len(Pi):
    #        if (Pi[index_4_1] != []) and (Pi[index_4_0] == Pi[index_4_1]):
    #            index -= 1
    #            Pi.pop(index_4_1)
    #            Pi.append([])
    #            
    #        index_4_1 += 1
    #    index_4_0 += 1
    ###
    print c_Pi
    
    index_1 = 0
    
    while index_1 < len(c_Pi):
        Pi[index].append(Ro[c_Pi[index_1]])
        index_1 += 1

    index_2 = 0
    
    c_Pi[len(c_Pi) - 1] = (c_Pi[len(c_Pi) - 1] + 1) % len(Ro)
    
    if c_Pi[len(c_Pi) - 1] > 0:
        index_2_2 = 1
    
    index_2_1 = len(c_Pi) - 2
    
    while index_2_1 >= 0:
        if (index_2_2 > 0) and (c_Pi[index_2_1 + 1] % len(Ro) == 0):
            c_Pi[index_2_1] = (c_Pi[index_2_1] + 1) % len(Ro)
            c_Pi_1[index_2_1] = 1
            
        if not(c_Pi[index_2_1 + 1] % len(Ro) == 0 and c_Pi_1[index_2_1] == 1):
            break
        
        index_2_1 -= 1
    
    
    print Pi[index]
    
    index += 1

###    
#index = 0
#
#conflicts = 0
#
#while index < len(Pi) - 1:
#    index_1 = index + 1
#    
#    while index_1 < len(Pi):
#        if (Pi[index_1] != []) and (Pi[index] == Pi[index_1]):
#            conflicts += 1
#            
#            break
#            
#        index_1 += 1
#    index += 1
#
#print "conflicts: " + str(conflicts)
###

index = 0

P = []

while index < p_n:
    P.append(p[index])
    index += 1
    
print P
    
index = 0

while index < len(Pi):
    if P == Pi[index]:
        print "combination: " + str(index) + "/" + str(len(Pi))
    index += 1

print "|" +  p + "| = " + str(p_n)
    
print Lambda
print "|Lambda| = " + str(len(Lambda))
print "combinations = " + str(Lambda_c)

print Ro
print "|Ro| = " + str(len(Ro))
print "combinations = " + str(Ro_c)

