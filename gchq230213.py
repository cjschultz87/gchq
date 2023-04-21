import time

def binary(a,b):
    rStr = ""
    if a == 0:
        index = 0
        
        while index < b:
            rStr += "0"
            index += 1
    else:
        rStr = ""
        aPrime = a
        N = 0
        while 1 > 0:
            if aPrime == 0:
                break
            N += 1
            aPrime /= 2
    
        index = 0
        while index <= N:
            rN = a%2
            rStr = str(rN) + rStr
            a /= 2
            index += 1        
    
        if len(rStr) <= b:
            index = 0
            while index < b - (1 + N):
                rStr = "0" + rStr
                index += 1
        else:
            rStr = rStr[1:b+1]
    
    
    return rStr
    
def decimal(a):
    rVal = 0
    index = 0
    
    while index < len(a):
        rVal += int(a[index]) * pow(2,len(a) - (1+index))
        index += 1
    
    return rVal

kilo = "silver"

input = " abcdefghijklmnopqrstuvwxyz"

sBox = [["00",[]],["01",[]],["10",[]],["11",[]]]

index = 0

sBox_N1 = 8

while index < len(sBox):
    index_1 = 0
    while index_1 < sBox_N1:
        index_2 = 0
    
        sBox[index][1].append(int((time.clock()*1000000)%sBox_N1))
    
        if len(sBox[index][1]) > 1:
            while index_2 < len(sBox[index][1]) - 1 and index_2 < sBox_N1:
                if sBox[index][1][len(sBox[index][1]) - 1] == sBox[index][1][index_2]:
                    sBox[index][1].pop()
                    index_1 -= 1
                index_2 += 1
        
        index_1 += 1
    
    index += 1
    
print "sBox"
print sBox

enc = [[' ',0],['a',1],['b',2],['c',3],['d',4],['e',5],['f',6],['g',7],['h',8],['i',9],['j',10],['k',11],['l',12],['m',13],['n',14],['o',15],['p',16],['q',17],['r',18],['s',19],['t',20],['u',21],['v',22],['w',23],['x',24],['y',25],['z',26]]

sierra = []
sierraPrime = []

index = 0

while index < len(input):
    index_1 = 0
    while index_1 < len(enc):
        if enc[index_1][0] == input[index]:
            sierra.append(binary(enc[index_1][1],5))
            break
        index_1 += 1
    index += 1

print "binary of input string"    
print str(sierra)

index = 0

while index < len(sierra):
    index_1_0 = 0
    index_1_1 = 0
    
    firstlast = sierra[index][0] + sierra[index][len(sierra[index]) - 1]
    
    if firstlast == "00":
        index_1_0 = 0
        index_1_1 = 0
        
        while index_1_0 < len(sBox[index_1_1][1]):
            if binary(index_1_0,3) == sierra[index][1:len(sierra[index]) - 1]:
                break
            index_1_0 += 1
            
    if firstlast == "01":
        index_1_0 = 0
        index_1_1 = 1
        
        while index_1_0 < len(sBox[index_1_1][1]):
            if binary(index_1_0,3) == sierra[index][1:len(sierra[index]) - 1]:
                break
            index_1_0 += 1
            
    if firstlast == "10":
        index_1_0 = 0
        index_1_1 = 2
        
        while index_1_0 < len(sBox[index_1_1][1]):
            if binary(index_1_0,3) == sierra[index][1:len(sierra[index]) - 1]:
                break
            index_1_0 += 1
            
    if firstlast == "11":
        index_1_0 = 0
        index_1_1 = 3
        
        while index_1_0 < len(sBox[index_1_1][1]):
            if binary(index_1_0,3) == sierra[index][1:len(sierra[index]) - 1]:
                break
            index_1_0 += 1
            
    sierraPrime.append(binary(sBox[index_1_1][1][index_1_0],3))
    
    sierraStr = sierraPrime[index]
    
    if index_1_1 == 0:
        sierraStr = str(0) + sierraStr
        sierraStr = sierraStr + str(0)
    elif index_1_1 == 1:
        sierraStr = str(0) + sierraStr
        sierraStr = sierraStr + str(1)
    elif index_1_1 == 2:
        sierraStr = str(1) + sierraStr
        sierraStr = sierraStr + str(0)
    elif index_1_1 == 3:
        sierraStr = str(1) + sierraStr
        sierraStr = sierraStr + str(1)
    else:
        print "error"
        break
        
    sierraPrime[index] = sierraStr
    
    index += 1

print "binary of cypher text"
    
print str(sierraPrime)

index = 0

ct = ""

while index < len(sierraPrime):
    ct += str(decimal(sierraPrime[index])) + " "
    index += 1
    
print "cyphertext: " + ct


