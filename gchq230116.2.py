# Given one of Matsuo Basho’s winter haiku and ten of his summer haiku, returns the number of string combinations for the winter haiku and average for the summer haiku. Based on these combinations the strings are analysed for common strings used in the winter and collection of summer haiku, then computes various probabilities of finding the strings in each.

haikuSierra_0 = "resemble\nthe mind of a traveler\nthe flower of chinquapin"
haikuSierra_1 = "from the clean fall\nyou dipped up water\nfor the tokoroten\n"
haikuSierra_2 = "the sound of trudging horses\ni found myself in the paint\nit's summer fields\n"
haikuSierra_3 = "wishing you were here\nwho feel sure of growing a gurad\ni enjoy the cool of the evening\n"
haikuSierra_4 = "the hydrangeas\nand the thicket is for the small garden\nanother tatami room\n"
haikuSierra_5 = "even a woodpecker\nwouldn't crack the tea hut\nin the summer grove\n"
haikuSierra_6 = "their own fire\nare on the trees the fireflies\naround the house with flowers\n"
haikuSierra_7 = "in the early summer rain\ni will see the floating nests\nof the little grebes\n"
haikuSierra_8 = "the crests of the cloud\ncrumble frequently\nthe moon mountain\n"
haikuSierra_9 = "thick and dull\nthe chinaberries are in the rain\nand the hazy weather\n"
haikuSierra_10 = "the hot sun was\nset into the sea\nby the mogami river\n"
#basho's summer haiku

haiku = "the snow and snow\nthis evening would have\nthe great moon of december\n"
#basho's winter haiku

vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

haikuSierra = [haikuSierra_0, haikuSierra_1, haikuSierra_2, haikuSierra_3, haikuSierra_4, haikuSierra_5, haikuSierra_6, haikuSierra_7, haikuSierra_8, haikuSierra_9, haikuSierra_10]

c_alpha = 0
c_bravo = 0

index_0_0 = 0
index_0_1 = 0

while index_0_0 < len(haiku):
    index_0_1 = index_0_0 + 2
    while index_0_1 < len(haiku):
        c_alpha += 1
        index_0_1 += 2
    index_0_0 += 1

index = 0
index_0_0 = 0
index_0_1 = 0

while index < len(haikuSierra):
    index_0_0 = 0
    while index_0_0 < len(haikuSierra[index]):
        index_0_1 = index_0_0 + 2
        while index_0_1 < len(haikuSierra[index]):
            c_bravo += 1
            index_0_1 += 2
        index_0_0 += 1
    index += 1
    
c_bravo /= len(haikuSierra)
    
index = 0
index_0_0 = 0
index_0_1 = 0
index_1_0 = 0
index_1_1 = 0

stringsIntersect = []

while index < len(haikuSierra):
    index_0_0 = 0
    print "haiku_" + str(index)
    while index_0_0 < len(haikuSierra[index]):
        index_0_1 = index_0_0 + 2
        while index_0_1 < len(haikuSierra[index]):
            index_1_0 = 0
            while index_1_0 < len(haiku):
                index_1_1 = index_1_0 + 2
                while index_1_1 < len(haiku):
                    if haikuSierra[index][index_0_0:index_0_1] == haiku[index_1_0:index_1_1]:
                        stringsIntersect.append(haiku[index_1_0:index_1_1])
                    index_1_1 += 2
                index_1_0 += 1
            index_0_1 += 2
        index_0_0 += 1
    index += 1
    
index = 0
index_0_0 = 0

print stringsIntersect

 
P_BA = float(len(stringsIntersect))/float(c_alpha)
P_A = float(c_alpha)/float(c_alpha + c_bravo)
P_B = float(c_bravo)/float(c_alpha + c_bravo)

print "winter haiku combinations = " + str(c_alpha)
print "#####"
print "avg summer haiku combinations = " + str(c_bravo)
print "#####"
print "common strings = " + str(len(stringsIntersect))
print "#####"
print "P(summer|winter) = " + str(P_BA)
print "#####"
print "P(winter) = " + str(P_A)
print "#####"
print "P(summer) = " + str(P_B)
print "#####"
print "P(winter|summer) = " + str((P_BA * P_A)/P_B)

