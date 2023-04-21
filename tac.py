import time

# [[][][]]
# [[][][]]
# [[][][]]

# [[beta.R[0][0][0]],[beta.R[0][1][0]],[beta.R[0][2][0]]]
# [[beta.R[1][0][0]],[beta.R[1][1][0]],[beta.R[1][2][0]]]
# [[beta.R[2][0][0]],[beta.R[2][1][0]],[beta.R[2][2][0]]]

class cell:
    c00 = [0,[0,0,0]]
    e10 = [0,[0,0,0,0,0]]
    c20 = [0,[0,0,0]]
    e01 = [0,[0,0,0,0,0]]
    ce = [0,[0,0,0,0,0,0,0,0]]
    e21 = [0,[0,0,0,0,0]]
    c02 = [0,[0,0,0]]
    e12 = [0,[0,0,0,0,0]]
    c22 = [0,[0,0,0]]

class board:    
    r0 = [cell.c00,cell.e01,cell.c02]
    r1 = [cell.e10,cell.ce,cell.e12]
    r2 = [cell.c20,cell.e21,cell.c22]
    R = [r0,r1,r2]

beta = board

open = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

def boardReset():
    beta.R[0][0][0] = 0
    beta.R[0][1][0] = 0
    beta.R[0][2][0] = 0
    beta.R[1][0][0] = 0
    beta.R[1][1][0] = 0
    beta.R[1][2][0] = 0
    beta.R[2][0][0] = 0
    beta.R[2][1][0] = 0
    beta.R[2][2][0] = 0
    
    index = 0
    
    while index < len(open):
        open.pop()
        
    open.append([0,0])
    open.append([0,1])
    open.append([0,2])
    open.append([1,0])
    open.append([1,1])
    open.append([1,2])
    open.append([2,0])
    open.append([2,1])
    open.append([2,2])


def victory(a):
    print "victory: " + str(a)
    
    boardReset()
    
def statusQuo():
    print "status quo"
    
    boardReset()

def boardPrint():
    print "_|a  b  c"
    print "a" + str([beta.r0[0][0],beta.r0[1][0],beta.r0[2][0]])
    print "b" + str([beta.r1[0][0],beta.r1[1][0],beta.r1[2][0]])
    print "c" + str([beta.r2[0][0],beta.r2[1][0],beta.r2[2][0]])
    
def verPrint():
    print beta.r0
    print beta.r1
    print beta.r2
    
def betaNodes():
    beta.R[0][0][1] = [beta.R[0][1][0],beta.R[1][1][0],beta.R[1][0][0]]
    beta.R[0][1][1] = [beta.R[0][2][0],beta.R[1][2][0],beta.R[1][1][0],beta.R[1][0][0],beta.R[0][0][0]]
    beta.R[0][2][1] = [beta.R[0][1][0],beta.R[1][1][0],beta.R[1][2][0]]
    beta.R[1][0][1] = [beta.R[0][0][0],beta.R[0][1][0],beta.R[1][1][0],beta.R[2][1][0],beta.R[2][0][0]]
    beta.R[1][1][1] = [beta.R[0][2][0],beta.R[1][2][0],beta.R[2][2][0],beta.R[2][1][0],beta.R[2][0][0],beta.R[1][0][0],beta.R[0][0][0],beta.R[0][1][0]]
    beta.R[1][2][1] = [beta.R[2][2][0],beta.R[2][1][0],beta.R[1][1][0],beta.R[0][1][0],beta.R[0][2][0]]
    beta.R[2][0][1] = [beta.R[1][0][0],beta.R[1][1][0],beta.R[2][1][0]]
    beta.R[2][1][1] = [beta.R[2][0][0],beta.R[1][0][0],beta.R[1][1][0],beta.R[1][2][0],beta.R[2][2][0]]
    beta.R[2][2][1] = [beta.R[2][1][0],beta.R[1][1][0],beta.R[1][2][0]]

rc = ["a","b","c"]
RC = [0,0]


bool = 1

while bool == 1:

    plMove = 1
    
    while plMove == 1:
    
        boardPrint()
    
        print ">cell: \"row,column\""
        print ">exit: \"e\""
        print ">help: \"h\""


        inputVal = "NULL"

        try:
            inputVal = input()
        except:
            pass

        if str(inputVal) == 'e':
            quit()
        elif str(inputVal) == 'v':
            verPrint()
        elif str(inputVal) == 'h':
            print "entries must be in quotations"
            print "enter the row followed by the column"
            print "the rows and columns are labelled a,b,c"
            print "your pieces are 1, the oponent's are 2"
            print "try to get three in a row"
        else:
            if (str(inputVal)[0] == "a" or str(inputVal)[0] == "b" or str(inputVal)[0] == "c") and (str(inputVal)[2] == "a" or str(inputVal)[2] == "b" or str(inputVal)[2] == "c"):
                index = 0
            
                while index < len(rc):
                    if str(inputVal)[0] == rc[index]:
                        RC[0] = index
                    if str(inputVal)[2] == rc[index]:
                        RC[1] = index
                    index += 1
                
                if RC[0] == 0:
                    if beta.R[0][RC[1]][0] == 0:
                        beta.R[0][RC[1]][0] = 1
                        open.remove([0,RC[1]])
                        plMove = 0
                elif RC[0] == 1:
                    if beta.R[1][RC[1]][0] == 0:
                        beta.R[1][RC[1]][0] = 1
                        open.remove([1,RC[1]])
                        plMove = 0
                elif RC[0] == 2:
                    if beta.R[2][RC[1]][0] == 0:
                        beta.R[2][RC[1]][0] = 1
                        open.remove([2,RC[1]])
                        plMove = 0
                else:
                    print "invalid entry"
                    
                
            else:
                print "invalid input"
                quit()

    index = 0
    
    opMove = 1

    while opMove == 1:
        index = 0
        
        while index < len(beta.R):
            index_1_0 = 0
            
            probability_0 = int((time.clock() * 1000000) % 10)
            probability_1 = int((time.clock() * 1000000) % 10)
            
            while index_1_0 < len(beta.R[0]):
                if beta.R[index][index_1_0][0] > 0 and beta.R[index][index_1_0][0] == beta.R[index][index_1_0 - 2][0]:
                    probability_1 = int((time.clock() * 1000000) % 10)
                     
                    if probability_1 > probability_0:
                        RC[0] = index
                        RC[1] = index_1_0 - 1

                elif beta.R[index][index_1_0][0] > 0 and beta.R[index][index_1_0][0] == beta.R[index - 2][index_1_0][0]:
                    probability_0 = probability_1
                    probability_1 = int((time.clock() * 1000000) % 10)
                     
                    if probability_1 > probability_0:
                        RC[0] = index - 1
                        RC[1] = index_1_0    

                elif beta.R[index][index_1_0][0] > 0 and beta.R[index][index_1_0][0] == beta.R[index - 2][index_1_0 - 2][0]:
                    probability_0 = probability_1
                    probability_1 = int((time.clock() * 1000000) % 10)
                     
                    if probability_1 > probability_0:
                        RC[0] = index - 1
                        RC[1] = index_1_0 - 1

                elif beta.R[index][index_1_0][0] > 0 and beta.R[index][index_1_0][0] == beta.R[(index + 2) % 2][(index_1_0 + 2) % 2][0]:
                    probability_0 = probability_1
                    probability_1 = int((time.clock() * 1000000) % 10)
                     
                    if probability_1 > probability_0:
                        RC[0] = (index + 1) % 2
                        RC[1] = (index_1_0 + 1) % 2

                else:
                    index_1_1 = int((time.clock() * 1000000) % len(open))
                    RC[0] = open[index_1_1][0]
                    RC[1] = open[index_1_1][1]
                index_1_0 += 1
            index += 1
    
        if RC[0] == 0:
            if beta.R[0][RC[1]][0] == 0:
                beta.R[0][RC[1]][0] = 2
                open.remove([open[index_1_1][0],open[index_1_1][1]])
                opMove = 0
        elif RC[0] == 1:
            if beta.R[1][RC[1]][0] == 0:
                beta.R[1][RC[1]][0] = 2
                open.remove([open[index_1_1][0],open[index_1_1][1]])
                opMove = 0
        elif RC[0] == 2:
            if beta.R[2][RC[1]][0] == 0:
                beta.R[2][RC[1]][0] = 2
                open.remove([open[index_1_1][0],open[index_1_1][1]])
                opMove = 0
    
    index = 0
    
    while index < len(beta.R):
        index_1_0 = 0
        
        while index_1_0 < len(beta.R[0]):
            if (beta.R[index][index_1_0][0] > 0 and beta.R[index][index_1_0][0] == beta.R[index][index_1_0 - 1][0] and beta.R[index][index_1_0 - 2][0] == beta.R[index][index_1_0 - 1][0]) or (beta.R[index][index_1_0][0] > 0 and beta.R[index][index_1_0][0] == beta.R[index - 1][index_1_0][0] and beta.R[index - 2][index_1_0][0] == beta.R[index - 1][index_1_0][0]) or (beta.R[index][index_1_0][0] > 0 and beta.R[index][index_1_0][0] == beta.R[index - 1][index_1_0 - 1][0] and beta.R[index - 2][index_1_0 - 2][0] == beta.R[index - 1][index_1_0 - 1][0]):
                victory(beta.R[index][index_1_0][0])
            index_1_0 += 1
        index += 1
    
    if len(open) == 0:
        statusQuo()
