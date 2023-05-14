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
        
    def nearestNextNode(self, distArray, vistSet): 
        # Initilaize minimum distance for nearest node:
        min = 1000000
        # Search for nearest unvisited node:
        for v in range(self.nodes): 
            if distArray[v] <= min and vistSet[v] == False: 
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

    def dijkstra(self, srcNode, difference):
        # to store the parent of each node, initialized with infinity:
        parent = [chr(difference+97) for i in range(self.nodes)] 
        for i in range(self.nodes):
            #initialize the distances to infinity:
            self.distArray[i] = 1000000
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
                    if self.distArray[v] == 1000000:
                        print("ꝏ ,",parent[v],"\t\t ", end='')
                    else:    
                        print(self.distArray[v],",",parent[v],"\t\t ", end='')
            print()

        print("-------------------------------------------")
        print("Destination\tLink")
        for b in range(1, len(visited_nodes)):
            print(visited_nodes[b], "\t\t(u,", end= '')
            prev = visited_nodes[b]
            predecessor = parent[b]
            # c = 0
            while(predecessor != 'u'):
                prev = predecessor
                predecessor = parent[ord(predecessor)-97-difference]

            print(prev,")")

        return parent,visited_nodes

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

parent,visited = g.dijkstra(0, difference)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
# Draw the edge labels on top of the graph
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_edges(G, pos)

plt.figure()

# draw shortest path only:
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos, labels={n: n for n in G.nodes()}, font_size=12, font_color="w", font_weight="bold")
for a in range(len(visited)):
    path = nx.dijkstra_path(G, visited[0], visited[a])
    nx.draw_networkx_edges(G, pos, edgelist=list(zip(path, path[1:])), edge_color='r', width=2)

plt.show()



