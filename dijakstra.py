import networkx as nx
import matplotlib.pyplot as plt

class Graph(): 
    def __init__(self, nodes):
        #distance array initialization:
        self.distArray = [0 for i in range(nodes)]
        #visited nodes initialization:
        self.vistSet = [0 for i in range(nodes)]
        #initializing the number of nodes:
        self.nodes = nodes
        self.INF = float('inf') # initial distance between nodes
        #initializing the graph matrix
        self.graph = [[0 for column in range(nodes)]  
                    for row in range(nodes)]
        
    def nearestNextNode(self, distArray, vistSet): 
        # Initilaize minimum distance for nearest node:
        min = float('inf')
        # Search for nearest unvisited node:
        for v in range(self.nodes): 
            if distArray[v] < min and vistSet[v] == False: 
                min = distArray[v] 
                nearestNextNode_index = v 
        return nearestNextNode_index
    
    def getParent(self, nodeIndx, difference):
        min = float('inf')
        parnt = 0
        for k in range(self.nodes):
            if self.graph[nodeIndx][k]<min:
                min = self.graph[nodeIndx][k]
                parnt = k
        return min, parnt
    
    # def printPath(self, parent, j, difference):
    #     # Base Case : If j is source
    #     if parent[j] == -1 :
    #         print(chr(j+97+difference), end=' ')
    #         return
    #     self.printPath(parent , parent[j], difference)
    #     print(chr(j+97+difference), end=' ')

    def dijkstra(self, srcNode, difference):
        # to store the parent of each node, initialized with infinity:
        parent = [self.INF for i in range(self.nodes)] 
        for i in range(self.nodes):
            #initialize the distances to infinity:
            self.distArray[i] = self.INF
            #set the visited nodes to false for each node:
            self.vistSet[i] = False
        #initialize the first distance to 0 (between the first node and itself)
        self.distArray[srcNode] = 0

        #initialize a list to store the visited nodes at each iteration:
        visited_nodes = []
        print("Step  \tN' \tD(v),p(v) \tD(w),p(w) \tD(x),p(x) \tD(y),p(y) \tD(z),p(z) ")
        for i in range(self.nodes): # 6 steps
            # Pick the shortest distance next unvisted node 
            # nearestNextNodeindx is equal to srcNode in first iteration 
            nearestNextNodeindx = self.nearestNextNode(self.distArray, self.vistSet) 
            # Put the shortest distance node in the visited nodes set:
            self.vistSet[nearestNextNodeindx] = True
            # Add the visited node to the list
            nearestChar = nearestNextNodeindx+97+difference
            visited_nodes.append(chr(nearestChar))
            print(i,"    ",''.join(visited_nodes),"\t",end='')

            # Update distance only if the node is unvisited and the total weight of path from src to v 
            # through nearestNextNodeindx is smaller than current value of dist[v]
            for v in range(self.nodes): 
                if self.graph[nearestNextNodeindx][v] > 0:
                    if self.distArray[v] > self.distArray[nearestNextNodeindx] + self.graph[nearestNextNodeindx][v]: 
                        self.distArray[v] = self.distArray[nearestNextNodeindx] + self.graph[nearestNextNodeindx][v]
                        parent[v] = chr(nearestChar)
                if v > 0: 
                    print(self.distArray[v],",",parent[v],"\t\t ", end='')
            print()

#get input from text file:
with open('input.txt', 'r') as file:
    first = 1
    # Read each line of the file
    for line in file:
        line = line.split(",")
        if first:
            nNodes = int(line[0])
            nEdges = int(line[1])
            first = 0
            g = Graph(nNodes)
            G = nx.Graph()
            x = True
            continue
        if x:
            difference = ord(line[0])-97
            x = False
        g.graph[ord(line[0])-97-difference][ord(line[1])-97-difference] = int(line[2])
        G.add_edge(line[0], line[1], weight=int(line[2]))
        g.graph[ord(line[1])-97-difference][ord(line[0])-97-difference] = int(line[2])

# Close the file
file.close()

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
# Draw the edge labels on top of the graph
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# Draw the shortest path on top of the graph
nx.draw_networkx_edges(G, pos)

g.dijkstra(0, difference)
plt.show()

