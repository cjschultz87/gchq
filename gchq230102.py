# From the array [“fin”,”found”,”green”,”ice”,”jut”,”lap”,”mary”,”new”,”rut”], the combinations correspond to having the last letter of the first word and first letter of the second word given string pairs in the array [“fin”,”green”,”ice”,”jut”,”lap”,”mary”,”newfound”,”rut”]

array = ["fin","found","green","ice","jut","lap","mary","new","rut"]
locs = ["fin","green","ice","jut","lap","mary","newfound","rut"]
rStrs = []
strI0 = 0
strI1 = 0
strLen = 0
locsIndex = 0
L = 1
while locsIndex < len(locs):
    while strI0 < len(array):
        strLen = 0
        while strLen < len(array[strI0]):
            strLen += 1
            print strLen
        L = 1
        while L < len(locs[locsIndex]):
            strI1 = 0
            while strI1 < len(array):
                print locs[locsIndex][L-1]
                print locs[locsIndex][L]
                if array[strI0][strLen - 1] == locs[locsIndex][L-1]:
                    if array[strI1][0] == locs[locsIndex][L]:
                        str = array[strI0] + array[strI1]
                        rStrs.append(str)
                strI1 += 1
            L += 1
        L = 1
        strI0 += 1
    strI0 = 0
    locsIndex += 1
    
print rStrs
