from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + int(graph.distances[(min_node, edge)])
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

if __name__ == '__main__':
    mycases = []
    Case_Num = raw_input()
    if Case_Num != '0':
        for case in range(int(Case_Num)):
          
          graph = Graph()
          houses = []
          edges = []
          setup = raw_input()
          setupl = setup.split()
          setupl = list(setupl)
          
          if setupl[2] == setupl[3]:
            mycases.append('Case #'+str(case+1)+': 0')
          elif setupl[1] != '0':
              for numroads in range(int(setupl[1])):
                new = raw_input()
                new = new.split()
                new = list(new)
                if new[0] not in houses:
                  houses.extend(new[0])
                if new[1] not in houses:
                  houses.extend(new[1])

                edges.append((str(new[0]),str(new[1]),int(new[2])))

              for node in houses:
                graph.add_node(str(node))
              for node in edges:
                graph.add_edge(str(node[0]),str(node[1]),int(node[2]))
              s1 = min(setupl[2],setupl[3])
              s2 = max(setupl[2],setupl[3])
              mycases.append('Case #'+str(case+1)+': '+ str(shortest_path(graph, s1, s2)[0]))
          else:
            mycases.append('Case #'+str(case+1)+': unreachable')
        string = ''
        for line in mycases:
            string += line
            string += '\n'

        print string
