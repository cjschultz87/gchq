import sys

def decimal(strb):
    index = 0
    
    rVal = 0
    
    while index < len(strb):
        rVal += int(strb[index])*pow(10,len(strb)-(1+index))
        
        index += 1
    
    return rVal
    
def db(a):
    rVal = ""
    
    while a > 0:
        rVal += str(a%2)
        a /= 2
        
    rVal_prime = ""
    
    index = 0
    
    while index < len(rVal):
        rVal_prime += rVal[len(rVal)-(1+index)]
        
        index += 1
        
    return int(rVal_prime)
    
def sb(str):
    index = 0
    
    rVal = ""
    
    while index < len(str):
        index_1 = 0
    
        while index_1 < len(alphabet):
            if str[index] == alphabet[index_1][0]:
                rVal += alphabet[index_1][1]
                
            index_1 += 1
        
        index += 1
    
    return rVal


alphabet = [['a',"00001","alpha"],['b',"00010","bravo"],['c',"00011","charlie"],['d',"00100","delta"],['e',"00101","echo"],['f',"00110","foxtrot"],['g',"00111","golf"],['h',"01000","hotel"],['i',"01001","india"],['j',"01010","juliet"],['k',"01011","kilo"],['l',"01100","lima"],['m',"01101","mike"],['n',"01110","november"],['o',"01111","oscar"],['p',"10000","papa"],['q',"10001","quebec"],['r',"10010","romeo"],['s',"10011","sierra"],['t',"10100","tango"],['u',"10101","unicorn"],['v',"10110","victor"],['w',"10111","whiskey"],['x',"11000","xray"],['y',"11001","yankee"],['z',"11010","zulu"]]

address_space = []

index = 0
index_1 = 0

while index < decimal(alphabet[25][1]):
    if decimal(alphabet[index_1][1]) == index:
        address_space.append(alphabet[index_1][2])
        
        if index_1 < len(alphabet):
            index_1 += 1
        
    else:
        address_space.append('')
    
    index += 1

permutations = []

try:
    a = sys.stdin[0]
except:
    quit()

for element in sys.stdin:
    x = element[0]
    
    for letter in alphabet:
        if x == letter[0]:
            permutations.append(element[0:len(element)-1])

index = 0

while index < 2:
    permutations.pop(0)
    
    index += 1

for p in permutations:
    for p_1 in p:
        print sb(p_1)
        
        print address_space[int(sb(p_1))]
        
    index = 0
    
    print "\n"