def cos(a):
	cos = 1
	index = 0
	factorial = 1
	while index < 50:
		index_2 = 1
		factorial = 1
		while index_2 <= (index + 1) * 2:
			factorial *= index_2
			index_2 += 1

		cos += float(pow(-1,index+1) *pow(a,(index+1)*2))/float(factorial)
		index += 1
		
	return cos
    
def sin(a):
	sin = a
	index = 0
	factorial = 1
	while index < 50:
		index_2 = 1
		factorial = 1
		while index_2 <= (index + 1) * 2 + 1:
			factorial *= index_2
			index_2 += 1
            
		sin += float(pow(-1,index+1) *pow(a,(index+1)*2 + 1))/float(factorial)
		index += 1
		
	return sin

alphabet = [[" "," ",1],["a","alpha",2],["b","bravo",3],["c","charlie",4],["d","delta",5],["e,","echo",6],["f","foxtrot",7],["g","golf",8],["h","hotel",9],["i","india",10],["j","juliet",11],["k","kilo",12],["l","lima",13],["m","mike",14],["n","november",15],["o","oscar",16],["p","papa",17],["q","quebec",18],["r","romeo",19],["s","sierra",20],["t","tango",21],["u","unicorn",22],["v","victor",23],["w","whiskey",24],["x","xray",25],["y","yankee",26],["z","zulu",27]]

string = "nato phonetic alphabet"

key = "alphanumericone"
kappa = []

array = ["null"]

index = 0
index_1 = 1

while index < len(string):
    index_2 = 0
    
    while index_2 < len(alphabet):
        if string[index] == alphabet[index_2][0]:
            array.append(alphabet[index_2])
            
            index_1 += 1
        
        index_2 += 1
    
    index += 1
    
index = 0

n = 0

while index < len(key):
    index_2 = 0
    
    while index_2 < len(alphabet):
        if key[index] == alphabet[index_2][0]:
            kappa.append(alphabet[index_2][2])
        
        index_2 += 1
    index += 1

cipherText = []

index = 1

while index < len(array):
    x_0 = kappa[index%len(kappa)]*sin(array[index][2])
    x_1 = kappa[index%len(kappa)]*cos(array[index][2])
    y_0 = - kappa[index%len(kappa)]*sin(array[index][2])
    y_1 = kappa[index%len(kappa)]*cos(array[index][2])
    
    cipherText.append([])
    cipherText[index - 1].append(x_0)
    cipherText[index - 1].append(x_1)
    cipherText[index - 1].append(y_0)
    cipherText[index - 1].append(y_1)

    
    index += 1
    
print cipherText