alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

array = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

index = 0

while index < len(array):
    index_1 = 0
    
    sierra = ""
    
    while index_1 < len(array[index]):
        index_2 = 0
        
        while index_2 < len(alphabet):
            if array[index][index_1] == alphabet[index_2]:
                if len(str(index_2)) < 2:
                    sierra += "0"
                sierra += str(index_2)
            index_2 += 1
        index_1 += 1
        
    print sierra
    
    index += 1