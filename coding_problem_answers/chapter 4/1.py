import unittest


def find_route(a, b):
    path = None
    queue = Queue()
    node = a
    node.shortest_path = [node]
    visited = [node]
    while node:
        for adjacent in node.adjacent:
            if not adjacent.shortest_path:
                adjacent.shortest_path = node.shortest_path + [adjacent]
                if adjacent == b:
                    path = node.shortest_path + [adjacent]
                
                    break
                queue.push(adjacent)
                visited.append(adjacent)
        node = queue.remove()
    for nodes in visited:
        nodes.shortest_path = None
    return path
    


class Node():
    def __init__(self, data, adjancency_list = None):
        self.data = data
        self.adjacent = adjancency_list or []
        self.shortest_path = None
    
    def add_edge_to(self, node):
        self.adjacent += [node]
    
    def __str__(self):
        return self.data

class Queue():
    def __init__(self):
        self.queue = []
    
    def push(self, data):
        self.queue.append(data)
    
    def remove(self):
        if not len(self.queue):
            return None
        item = self.queue[0]
        del self.queue[0]
        return item



def str_for(path):
    if not path: 
        return str(path)
    return ''.join([str(n) for n in path])

class Test(unittest.TestCase):
  def test_find_route(self):
    node_j = Node('J')
    node_i = Node('I')
    node_h = Node('H')
    node_d = Node('D')
    node_f = Node('F', [node_i])
    node_b = Node('B', [node_j])
    node_g = Node('G', [node_d, node_h])
    node_c = Node('C', [node_g])
    node_a = Node('A', [node_b, node_c, node_d])
    node_e = Node('E', [node_f, node_a])
    node_d.add_edge_to(node_a)
    self.assertEqual(str_for(find_route(node_a, node_i)), 'None')
    self.assertEqual(str_for(find_route(node_a, node_j)), 'ABJ')
    node_h.add_edge_to(node_i)
    self.assertEqual(str_for(find_route(node_a, node_i)), 'ACGHI')

if __name__ == "__main__":
    unittest.main()


    
    
        






