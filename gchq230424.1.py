vocabulary = ["violin", "viola", "cello", "double bass"]
key = []

index = 0

while index < len(vocabulary):
    index_1 = 0
    
    word = ""
    
    while index_1 < len(vocabulary[index]):
        if vocabulary[index][index_1] == 'l' and not(index_1+1 == len(vocabulary[index])):
            if not(vocabulary[index][index_1+1] == vocabulary[index][index_1]):
                word += vocabulary[index][index_1:index_1+2]
                
                key.append(word)
        
        index_1 += 1
    index += 1
    
import time

alphabet = [["a",0],["b",1],["c",2],["d",3],["e",4],["f",5],["g",6],["h",7],["i",8],["j",9],["k",10],["l",11],["m",12],["n",13],["o",14],["p",15],["q",16],["r",17],["s",18],["t",19],["u",20],["v",21],["w",22],["x",23],["y",24],["z",25]]

index = 0
maxLen = 0

while index < len(vocabulary):
    if len(vocabulary[index]) > maxLen:
        maxLen = len(vocabulary[index])
    index += 1

vocabulary_1 = []

def seed():
    return str(int(time.clock()*1000000))

index = 0

while index < 100:
    index_1 = 0

    word = ""
    
    seed_1 = ""
    
    index_3 = 0
    
    while index_3 < len(str(maxLen)):
        seed_1 += seed()[len(seed())-1]
    
        index_4 = 0
        
        while index_4 < 10000:
            1+1
        
            index_4 += 1
    
        index_3 += 1

    while index_1 < (int(seed_1)%maxLen) + 2:

        digits = ""
    
        index_2 = 0
    
        while index_2 < len(str(alphabet[0][1])):
            digits += seed()[len(seed())-1]
            
            index_4 = 0
            
            while index_4 < 10000:
                1+1
                
                index_4 += 1
            
            index_2 += 1
    
        word += alphabet[(int(digits)%len(alphabet)) + 1][0]

        index_1 += 1

    index_5 = 0
    
    n = int(seed())%100
    
    while index_5 < n:
        vocabulary_1.append(word)
        
        if int(seed())%50 > 25:
            vocabulary_1.append(key[int(seed())%len(key)])
            
        if int(seed())%50 > 25:
            vocabulary_1.append(vocabulary[int(seed())%len(vocabulary)])
        
        index_5 += 1
    
    
    index += 1
    
print vocabulary
print key
print vocabulary_1

index = 0

p_a = 0
p_b = 0

sierra = 0

n = 0

while index < len(vocabulary_1):
    index_1 = 0
    
    while index_1 < len(vocabulary):
        if vocabulary_1[index] == vocabulary[index_1]:
            p_a += 1
        
        index_1 += 1
    
    index_1 = 0
    
    while index_1 < len(vocabulary_1[index]) - 1:
        index_2 = 0
        
        while index_2 < len(key):
            if vocabulary_1[index][index_1:index_1+2] == key[index_2]:
                p_b += 1
            index_2 += 1
        
        sierra += 1
        
        index_1 += 1
    
    index += 1

sierra = float(sierra + 1)/float(len(key[0]))
    
p_a = float(p_a) / float(len(vocabulary_1))
p_b = float(p_b)/float(sierra)

p_ba = float(1)/float(len(key))

print p_a
print p_b
print p_ba

# what is the probability that viola is in the array given that the syllable key is in the array elements?
#p(a|b) = p(b|a)p(b)/b(a)

print (p_ba*p_a) / p_b