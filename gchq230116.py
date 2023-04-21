haiku = "Yki to yuki\nKoyoi shiwasu no\nMeigetsu ya"
haikuEn = "the snow and snow\nthis evening would have\nthe great moon of december"
#Basho's winter haiku

lines = 1

nL = "\n"

index = 0

while index < len(haiku):
    if haiku[index] == nL:
        lines += 1
        
    index += 1
        
if lines == 3:
    print "HAIKU"