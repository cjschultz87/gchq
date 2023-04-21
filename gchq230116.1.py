alpha = [['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z']]
haiku = "the snow and snow\nthis evening would have\nthe great moon of december\n"
print haiku
print " "
syllabary = ["the", "snow", "and", "this", "eve", "ning", "would", "have", "great", "moon", "of", "de", "cem", "ber"]
#Basho's winter haiku
index = 0
while index < len(alpha):
    alpha[index].append(index)
    index += 1
alphaBravo = 0
index = 0
index_1 = 0
index_2 = 0
index_3 = 0
index_4 = 0
index_5 = 0
syllabelN = 0
sierraNMax = 0
while index < len(haiku):
    if haiku[index] != "\n" and haiku[index] != " ":
        index_3 = 0
        while index_3 < len(syllabary):
            if syllabary[index_3] == haiku[index_4 : index + 1]:
                syllabelN += 1
                index_4 = index + 1
            index_3 += 1
        if sierraNMax < index - index_1:
            sierraNMax = index - index_1
    elif haiku[index] == "\n" or haiku[index] == " ":
        if haiku[index] == "\n":
            print "approximate avg characters per syllabel: " + str((index - index_5) / syllabelN)
            print "characters per line: " + str(index - index_5)
            print "syllabels per line: " + str(syllabelN)
            syllabelN = 0
            index_5 = index
            print " "
        index_1 = index
        index_4 = index + 1
    index += 1