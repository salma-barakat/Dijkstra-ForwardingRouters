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
    

    def dijkstra(self, srcNode):
        for i in range(self.nodes):
            #initialize the distances to infinity:
            self.distArray[i] = self.INF
            #set the visited nodes set to false for each node:
            self.vistSet[i] = False

        #initialize the first distance to 0 (between the first node and itself)
        self.distArray[srcNode] = 0

        for i in range(self.nodes):
            # Pick the shortest distance unvisted node 
            # nearestNodeindx is equal to srcNode in first iteration 
            nearestNodeindx = self.nearestNode(self.distArray, self.vistSet) 
            # Put the shortest distance node in the visited nodes set
            self.vistSet[nearestNodeindx] = True

            # Update distance only if is the node is unvisited and the total weight of path from src to v 
            # through nearestNodeindx is smaller than current value of dist[v]
            for v in range(self.nodes): 
                if self.graph[nearestNodeindx][v] > 0 and self.vistSet[v] == False:
                    if self.distArray[v] > self.distArray[nearestNodeindx] + self.graph[nearestNodeindx][v]: 
                        self.distArray[v] = self.distArray[nearestNodeindx] + self.graph[nearestNodeindx][v]
        
        # To print the distances of all nodes:
        print ("Node \tDistance from 0")
        for i in range(self.nodes): 
            print (i, "\t", self.distArray[i])


# #Display our table
# ourGraph = Graph(7) 
# ourGraph.graph = 
 #          0  1  2  3  4  5  6
#       0 [[0, 2, 6, 0, 0, 0, 0], 
#       1  [2, 0, 0, 5, 0, 0, 0], 
#       2  [6, 6, 0, 8, 0, 0, 0], 
#       3  [0, 0, 8, 0, 10, 15, 0], 
#       4  [0, 0, 0, 10, 0, 6, 2], 
#       5  [0, 0, 0, 15, 6, 0, 6], 
#       6  [0, 0, 0, 0, 2, 6, 0],
#         ]; 
# ourGraph.dijkstra(0)

line1 = input("Enter the number of nodes and edges separated by comma:\n")
line1 = line1.split(",")
nNodes = int(line1[0])
nEdges = int(line1[1])
# Initializing a graph:
g = Graph(nNodes)
print("For each edge, enter the src_node, dest_node, weight:\n")
for i in range(nEdges):
    line = input()
    line = line.split(",")
    g.graph[int(line[0])][int(line[1])] = int(line[2])
g.dijkstra(0)
