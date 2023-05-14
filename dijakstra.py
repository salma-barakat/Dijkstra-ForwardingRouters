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
        self.INF = 1000000 # initial distance between nodes
        #initializing the graph matrix
        self.graph = [[0 for column in range(nodes)]  
                    for row in range(nodes)]
        
    def nearestNode(self, distArray, vistSet): 
        # Initilaize minimum distance for nearest node:
        min = self.INF
        # Search for nearest unvisited node:
        for v in range(self.nodes): 
            if distArray[v] < min and vistSet[v] == False: 
                min = distArray[v] 
                nearestNode_index = v 
        return nearestNode_index
    
    def getParent(self, nodeIndx, difference):
        min = 1000000
        parnt = 0
        for k in range(self.nodes):
            if self.graph[nodeIndx][k]<min:
                min = self.graph[nodeIndx][k]
                parnt = k
        return min, parnt
    
    def printPath(self, parent, j, difference):
        # Base Case : If j is source
        if parent[j] == -1 :
            print(chr(j+97+difference), end=' ')
            return
        self.printPath(parent , parent[j], difference)
        print(chr(j+97+difference), end=' ')

    def dijkstra(self, srcNode, difference):
        for i in range(self.nodes):
            #initialize the distances to infinity:
            self.distArray[i] = self.INF
            #set the visited nodes set to false for each node:
            self.vistSet[i] = False

        #initialize the first distance to 0 (between the first node and itself)
        self.distArray[srcNode] = 0

        #initialize a list to store the visited nodes at each iteration:
        visited_nodes = []
        #initialize a list to store the parent of each vertex in the shortest path tree:
        parent = [-1] * self.nodes
        print("Step  \tN' \tD(v),p(v) \tD(w),p(w) \tD(x),p(x) \tD(y),p(y) \tD(z),p(z) ")
        for i in range(self.nodes):
            # Pick the shortest distance unvisted node 
            # nearestNodeindx is equal to srcNode in first iteration 
            nearestNodeindx = self.nearestNode(self.distArray, self.vistSet) 
            # Put the shortest distance node in the visited nodes set
            self.vistSet[nearestNodeindx] = True
            # Add the visited node to the list
            nearestChar = nearestNodeindx+97+difference
            visited_nodes.append(chr(nearestChar))
            print(i,"    ",''.join(visited_nodes),"\t",end='')
            # Update distance only if the node is unvisited and the total weight of path from src to v 
            # through nearestNodeindx is smaller than current value of dist[v]
            
            for v in range(self.nodes): 
                if self.graph[nearestNodeindx][v] > 0 and self.vistSet[v] == False:
                    if self.distArray[v] > self.distArray[nearestNodeindx] + self.graph[nearestNodeindx][v]: 
                        self.distArray[v] = self.distArray[nearestNodeindx] + self.graph[nearestNodeindx][v]
                        # parent[v] = nearestNodeindx
                if v > 0: 
                    prnt = chr(nearestNodeindx+97+difference)
                    print(self.distArray[v],",",prnt,"\t\t ", end='')
                        #print("Destination \tLink")
                        # # for j in range(self.nodes): 
                        # print (chr(v+97+difference), "\t\t", end='')
                        # self.printPath(parent, v, difference)
            print()
            
            # # To print the distances of all nodes:
            # print("Node \tDistance \tPath")
            # for j in range(self.nodes): 
            #     print (chr(j+97+difference), "\t", self.distArray[j], "\t\t", end='')
            #     self.printPath(parent, j, difference)
            #     print()

            # To print the visited nodes at each iteration:
            
            
           # print("Visited nodes:", visited_nodes)

# Get the number of nodes and edges from user input
line1 = input("Enter the number of nodes and edges separated by comma:\n")
line1 = line1.split(",")
nNodes = int(line1[0])
nEdges = int(line1[1])

# Initializing a graph:
g = Graph(nNodes)
print("For each edge, enter the src_node, dest_node, weight:")
G = nx.Graph()
x = True
for i in range(nEdges):
    line = input()
    line = line.split(",")
    if x:
        difference = ord(line[0])-97
        x = False
    g.graph[ord(line[0])-97-difference][ord(line[1])-97-difference] = int(line[2])
    G.add_edge(line[0], line[1], weight=int(line[2]))

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

