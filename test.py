import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2, cost):
        self.nodes[node1].append((node2, cost))
        self.nodes[node2].append((node1, cost))

    def heuristic(self, node, goal):
        return abs(ord(node[0]) - ord(goal[0]))  # Heuristik Sederhana Berdasarkan Karakter ASCII

    def astar(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {node: float('inf') for node in self.nodes}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.nodes}
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for neighbor, cost in self.nodes[current]:
                tentative_g_score = g_score[current] + cost
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        return None  # Jika tidak ada jalur

    def draw_graph(self, path=None):
        G = nx.Graph()
        for node in self.nodes:
            for neighbor, cost in self.nodes[node]:
                G.add_edge(node, neighbor, weight=cost)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        
        if path:
            edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
        
        plt.show()

# Contoh penggunaan
graph = Graph()
nodes = ['EXP Lane', 'Gold Lane', 'Mid Lane', 'Jungle', 'Base', 'Lord Pit', 'Enemy Base']
for node in nodes:
    graph.add_node(node)

graph.add_edge('Base', 'Mid Lane', 2)
graph.add_edge('Base', 'Jungle', 4)
graph.add_edge('Mid Lane', 'EXP Lane', 7)
graph.add_edge('Jungle', 'EXP Lane', 1)
graph.add_edge('EXP Lane', 'Gold Lane', 3)
graph.add_edge('Gold Lane', 'Lord Pit', 5)
graph.add_edge('Jungle', 'Lord Pit', 8)
graph.add_edge('Lord Pit', 'Enemy Base', 6)

hero = "Ling"
start = 'Base'
goal = 'Enemy Base'
path = graph.astar(start, goal)
print(f"{hero} bergerak melalui jalur terbaik:", path)

graph.draw_graph(path)
