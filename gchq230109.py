alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ascii = []
intI = 0
while intI < 25:
    ascii.append([])
    ascii[intI].append(alphabet[intI])
    ascii[intI].append(intI + 65)
    intI += 1
print ascii
array = ["GALAXY","LAND","NATION","ODYSSEY","WORLD"]
asciiArray = []
intI = 0
while intI < len(array):
    asciiArray.append([])
    asciiArray[intI].append(array[intI])
    asciiArray[intI].append([])
    intI1 = 0
    while intI1 < len(array[intI]):
        intI2 = 0
        while intI2 < len(ascii):
            if array[intI][intI1] == ascii[intI2][0]:
                asciiArray[intI][1].append(ascii[intI2][1])
            intI2 += 1
        intI1 += 1
    intI += 1
print asciiArray 
asciiSum = []
intI = 0
while intI < len(asciiArray):
    intI1 = 0
    intSig = 0
    while intI1 < len(asciiArray[intI][1]):
        intSig += asciiArray[intI][1][intI1]
        intI1 += 1
    asciiSum.append(intSig/len(asciiArray[intI][0]))
    intI += 1
print asciiSum