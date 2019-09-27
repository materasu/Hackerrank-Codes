# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

firstInputLine = stdin.readline().split(' ')

n = int(firstInputLine[0])
q = int(firstInputLine[1])

parents = {}
subsetLengths = {}
subsetConnections = {}
subsetCount = 0

for i in range(1,n+1):
    parents[i] = -1
    
for i in range(q):
    queryLine = stdin.readline().split(' ')
    
    if(queryLine[0] == "M"):
        a = int(queryLine[1])
        b = int(queryLine[2])
        
        if((parents[a] == -1) and (parents[b] == -1)):
            parents[a] = subsetCount
            parents[b] = subsetCount
            subsetLengths[subsetCount] = 2
            subsetConnections[subsetCount] = subsetCount
            subsetCount = subsetCount + 1
        
        elif((parents[a] != -1) and (parents[b] == -1)):
            parents[b] = parents[a]
            subsetLengths[subsetConnections[parents[a]]] += 1
        
        elif((parents[a] == -1) and (parents[b] != -1)):
            parents[a] = parents[b]
            subsetLengths[subsetConnections[parents[b]]] += 1
        
        else:
            if(subsetConnections[parents[a]] != subsetConnections[parents[b]]):
                subsetLengths[subsetConnections[parents[a]]] += subsetLengths[subsetConnections[parents[b]]]
                subsetConnections[parents[b]] = subsetConnections[parents[a]]
    
    else:
        query = int(queryLine[1])
        
        # if(parents[query] == -1):
        #     print(1)
        # else:
        #     print(subsetLengths[subsetConnections[parents[int(queryLine[1])]]])

print("\n")    
print(parents)
print(subsetConnections)
print(subsetLengths)
