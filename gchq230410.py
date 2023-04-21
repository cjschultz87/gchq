alphabet = [["a",0],["b",1],["c",2],["d",3],["e",4],["f",5],["g",6],["h",7],["i",8],["j",9],["k",10],["l",11],["m",12],["n",13],["o",14],["p",15],["q",16],["r",17],["s",18],["t",19],["u",20],["v",21],["w",22],["x",23],["y",24],["z",25]]

vocabulary_0 = ["garnet","iron","rigs","rogue","sore"]
vocabulary_1 = ["urban"]

index = 0

v0 = []

while index < len(vocabulary_0):
    index_1_0 = 0
    
    v0.append([])
    
    while index_1_0 < len(vocabulary_0[index]):
        index_1_1 = 0
        
        while index_1_1 < len(alphabet):
            if alphabet[index_1_1][0] == vocabulary_0[index][index_1_0]:
                v0[index].append(alphabet[index_1_1][1])
            
            index_1_1 += 1
        
        index_1_0 += 1
    
    index += 1

print "vocabulary"
print v0

def factorial(n):
    index = 1
    
    foxtrot = 1
    
    while index <= n:
        foxtrot *= 1 + (index-1)
        index += 1
        
    return foxtrot

november_0 = []
november_1 = []

index = 0

while index < len(vocabulary_0):
    november_0.append(factorial(len(vocabulary_0[index])))
    
    index += 1
    
index = 0

while index < len(vocabulary_1):
    november_1.append(factorial(len(vocabulary_1[index])))
    
    index += 1

print "number of permutations"    
print [november_0,november_1]

v0_p = []
v1_p = []
pm = []
pm_1 = []

index = 0

while index < len(vocabulary_0):
    
    v0_p.append([])
    
    pm.append([])
    pm_1.append([])
    
    ident = []
    
    index_2_0 = 0
    
    while index_2_0 < len(vocabulary_0[index]):
        ident.append([])
        
        index_2_1 = 0
        
        while index_2_1 < len(vocabulary_0[index]):
            if index_2_1 == index_2_0:
                ident[index_2_0].append(1)
            else:
                ident[index_2_0].append(0)
            
            index_2_1 += 1
        
        index_2_0 += 1
    
    pm[index].append(ident)
    pm_1[index].append(vocabulary_0[index])

    index_5 = 1
    
    iota = []
    
    while index_5 < len(pm[index][0]):
        iota.append(factorial(index_5))
        
        index_5 += 1

    print iota
    
    iota_1 = []
    
    index_5 = 1
    
    while index_5 < len(pm[index][0]):
        iota_1.append(index_5)
        
        index_5 += 1

    index_3_0 = 1
    
    bravo = 0
    
    while bravo == 0:
        print pm[index][index_3_0-1]
        
        print index_3_0
        
        pq = []
        
        index_4 = 0
        
        n_index = 1
        
        while index_4 < len(iota):
            if index_3_0 > 0 and index_3_0 % iota[index_4] == 0:
                n_index = iota_1[index_4]
            index_4 += 1
        
        #n_index = iota[index_3_0 % iota[(index_3_0 + index_4_1) % (len(iota)-1)]]
        print n_index
            
        index_3_1 = 0
            
        while index_3_1 < len(pm[index][0]):
            if index_3_1 == 0:
                pq.append(pm[index][index_3_0-1][n_index])
            elif index_3_1 == n_index:
                pq.append(pm[index][index_3_0-1][0])
            else:
                pq.append(pm[index][index_3_0-1][index_3_1])
                
            index_3_1 += 1
        
        pm[index].append(pq)
        
        index_3_0 += 1
        
        
        if index_3_0 > november_0[index]:
            bravo = 1
    
    while index_3_0 < november_0[index] and 1>2:
        
        index_3_1 = 0
        
        pq = []
        
        iota_index = 0
        
        while iota_index < len(iota):
            
            iota_index += 1
        
        #123 ident
        #213 r01
        
        #312 r02
        #132 r01
        
        #231 r02
        #321 r01
        
        #1234 ident
        #2134 r01
        #3124 r02
        #1324 r01
        #2314 r02
        #3214 r01
        
        #4213 r03
        #2413 r01
        #1423 r02
        #4123 r01
        #2143 r02
        #1243 r01
        
        #3241
        #2341
        #4321
        #3421
        #2431
        #4231
        
        #123 1 ident
        #213
        
        #312 2 1,2 r02
        #132
        
        #321 3 2,1 r12
        #231
        
        #1234 1 ident
        
        #4213 2 1,6 r03
        
        #1342 3 2,6 r13
        #3142
        #4132
        #1432
        #3412
        #4312
        
        #2341 4 3,1 r03
        #3241
        #4231
        #2431
        #3421
        #4321
        
        
        pq_sierra = ""
        
        pm[index].append(pq)
        
        index_4 = 0
        
        while index_4 < len(pq):
            index_4_1 = 0
            
            while index_4_1 < len(pq[index_4]):
                if pq[index_4][index_4_1] == 1:
                    pq_sierra += str(alphabet[v0[index][index_4_1]][0])
                
                index_4_1 += 1
            
            index_4 += 1
        
        pm_1[index].append(pq_sierra)

        index_3_0 += 1

    
    index += 1
    
index = 4

while index < len(pm):
    index_1 = 0
    while index_1 < len(pm[index]):
        index_1_1 = index_1 + 1
        
        while index_1_1 < len(pm[index]):
            if pm[index][index_1] == pm[index][index_1_1]:
                #print pm_1[index][index_1]
                print pm[index][index_1]
                
                print str(index_1)+";"+str(index_1_1)
                
            index_1_1 += 1
        
        index_1 += 1
    
    index += 1
    


