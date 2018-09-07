import math
import networkx as nx
import matplotlib.pyplot as plt

#For visual representation of the workspace
#calculate all egdes of the grid with edges along X-Y direction only
def edges(n,m):
	lists=[]
	M = [[0 for x in range(n*m)] for y in range(n*m)]
	for i in range(n*m):
		for j in range(n*m):
			if i==j:
				M[i][j]=10
			elif i-j==1 or j-i==1:
				if i==0 or j==0:
					M[i][j]=1
				elif (i%n==0 and i>j) or (j%n==0 and j>i):
					M[i][j]=10
				else:
					M[i][j]=1
			elif i-j==n or j-i==n:
				M[i][j]=1
			else:
				M[i][j]=10
	
		c=[M[i][j] for j in range(n*m)]
		#k=min(c)
		for j in range(n*m):
			if M[i][j] ==1:
			
				M[j][i]=10
				#print i,j
				lists.append((i,j))
	return lists

#represent the nodes and edges of path	
G = nx.Graph()

#Visual representation of the workspace  
H = nx.Graph() 

#add all nodes to the graph  
for i in range (198):
	a = int(i/9)+1
	b = int(i%9)+1
	G.add_node(i,pos=(a,b))

#this loop is for visual representation only
for i in range (10*23):
	c = int(i/10)+0.5
	d = int(i%10)+0.5
	H.add_node(i,pos=(c,d))

#add all the edges in the graph 
G.add_edges_from(edges(9,22))

#graph for visual representation 
H.add_edges_from(edges(10,23))

#heuristic function for minimizing number of turns 
def turn(i, j):
	return abs(i-j)

#the nodes to be covered.
node_list = [14,19,32,39,61,75,91,113,137,142,175]


#list with random numbers to initialize the process 
store_list = [12,2,232,432,453,223213,2,23,4,4,5,42,33,12,34,232,343,232,22,1,1,1,32,154,7675,86,34,5,3,6,3,6]

#list for the actual shortest path 
short_path = []
#list to sotre the shortest path
test_path = []

#Use brute force to scan from each source node the shortest path
source = 0

for i in range(11):
	store_list = [12,2,232,432,453,223213,2,23,4,4,5,42,33,12,34,232,343,232,22,1,1,1,32,154,7675,86,34,5,3,6,3,6]
	for node in node_list:
		#print len(store_list)

		#path list with random nmber of values for initial calculation
		path_list = [12,2,232,432,453,223213,2,23,4,4,5,42,33,12,34,232,343,232,22,1,1,1,32,154,7675,86,34,5,3,6,3,6]
		if node != source:
			path_list = nx.astar_path(G,source,node,turn)
		#print path_list , len(path_list)

		if len(path_list) < len(store_list):
			store_list = path_list
		
	#remove the source from pathlist
	try:
		node_list.remove(source)
	except ValueError:
		pass  # do nothing!

	#Source value changes to the previous target 
	source = store_list[-1]
	if i <10:
		store_list = store_list[:-1]


	test_path.extend(store_list)


#Create edgelist. This is list is also used to  visually represent the shortest path
edge_list = []
for i in range(len(test_path)-1):
	edge_list.append((test_path[i],test_path[i+1]))

print edge_list

nx.draw_networkx_nodes(G,pos=nx.get_node_attributes(G, 'pos'),nodelist=[14,19,32,39,61,75,91,113,137,142,175],node_color='g')

nx.draw_networkx_edges(G,pos=nx.get_node_attributes(G, 'pos'),edgelist=edge_list,edge_color='r',width=3)

nx.draw(G, nx.get_node_attributes(G, 'pos'),edgelist=[], with_labels=True, node_size=10,node_color='')

nx.draw(H, nx.get_node_attributes(H, 'pos'), with_labels=False,node_size=0,width=2)


plt.show()