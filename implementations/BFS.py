
#most basic BFS implementation
#directed graph
class BFS_directed:

	def __init__(self):
		self.graph = {}
		self.size = 0

	#addedge(u, v) means add an edge from u to v. 
	def addEdge(self, u, v):
		if(u not in self.graph.keys()):
			self.graph[u] = []
			self.size += 1
		if(v not in self.graph.keys()):
			self.graph[v] = []
			self.size += 1
		self.graph[u].append(v)


	#s is the starting node
	def BFS(self, s):
		queue = []
		nodesdone = [0] * (self.size)

		queue.append(s)

		nodesdone[s] = 1

		while(queue):
			s = queue.pop(0)
			print(s, end=" ")
			for i in self.graph[s]:
				if (nodesdone[i] == 0):
					queue.append(i)
					nodesdone[i] = 1


g = BFS_directed()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(1)