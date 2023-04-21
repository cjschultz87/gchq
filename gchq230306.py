null = ["0"]

glyphs = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

states = ["alabama","alaska","arizona","arkansas","california","colorado","connecticut","delaware","florida","georgia","hawaii","idaho","illinois","indiana","iowa","kansas","kentucky","louisiana","maine","maryland","massachusettes","michigan","minnesota","mississippi","missouri","montana","nebraska","nevada","new hampshire","new jersey","new mexico","new york","north carolina","north dakota","ohio","oklahoma","oregon","pennsylvania","rhode island","south carolina","south dakota","tennessee","texas","utah","vermont","virginia","washington","west virginia","wisconsin","wyoming"]

groups = []

leadingletters = []

index = 1

n = 0

while index < len(states):
    if not(states[index][0] == states[index - 1][0]):
        n += 1
    index+= 1

index = 0
index_1 = 0

while index < n:
    leadingletters.append([])
    
    while index_1 < len(states):
        leadingletters[len(leadingletters)-1].append(states[index_1])
        
        if states[index_1][0] != states[(index_1 + 1)%50][0]:
            index_1 += 1
            break
        
        index_1 += 1
    
    groups.append(leadingletters[len(leadingletters)-1])
    
    index += 1
    
def mx(array):
    index = 1
    
    array_element = array[0]
    
    while index < len(array):
        if len(array_element) < len(array[index]):
            array_element = array[index]
            
        index += 1
    
    return array_element
    
index = 0

n = len(groups)

groups_ordered = []

while index < n:
    groups_ordered.append(mx(groups))
    groups.remove(mx(groups))
    
    index += 1
    
print groups_ordered