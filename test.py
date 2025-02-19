import heapq

class HeroNode:
    def __init__(self, name, lane, role, cost=0, heuristic=0):
        self.name = name
        self.lane = lane
        self.role = role
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

    def __lt__(self, other):
        return self.total_cost < other.total_cost

heroes = [
    HeroNode("Alucard", "Exp Lane", "Fighter"),
    HeroNode("Esmeralda", "Exp Lane", "Tank/Fighter"),
    HeroNode("Layla", "Gold Lane", "Marksman"),
    HeroNode("Claude", "Gold Lane", "Marksman"),
    HeroNode("Gusion", "Mid Lane", "Assassin"),
    HeroNode("Nana", "Mid Lane", "Support"),
    HeroNode("Selena", "Mid Lane", "Assassin/Support"),
    HeroNode("Tigreal", "Roam", "Tank")
]

connections = {
    "Alucard": ["Esmeralda"],
    "Layla": ["Claude"],
    "Gusion": ["Nana", "Selena"],
    "Tigreal": ["Alucard", "Layla"],
    "Nana": ["Gusion"],
    "Esmeralda": ["Tigreal"],
    "Claude": ["Layla"],
    "Selena": ["Gusion"]
}

heuristic_estimates = {
    "Alucard": 5,
    "Layla": 3,
    "Gusion": 2,
    "Tigreal": 4,
    "Nana": 1,
    "Esmeralda": 6,
    "Claude": 3,
    "Selena": 2
}

def astar_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_cost = {hero.name: float('inf') for hero in heroes}
    g_cost[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from.get(current, None)
            return path[::-1]

        for neighbor_name in connections.get(current, []):
            tentative_g_cost = g_cost[current] + 1

            if tentative_g_cost < g_cost[neighbor_name]:
                g_cost[neighbor_name] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic_estimates[neighbor_name]
                heapq.heappush(open_list, (f_cost, neighbor_name))
                came_from[neighbor_name] = current

    return None

start_hero = input("Masukkan nama hero awal: ").strip()
goal_hero = input("Masukkan nama hero tujuan: ").strip()

result_path = astar_search(start_hero, goal_hero)

if result_path:
    print("Path ditemukan:")
    for step in result_path:
        hero = next((h for h in heroes if h.name == step), None)
        print(f"{hero.name} -> Lane: {hero.lane}, Role: {hero.role}")
else:
    print("Path tidak ditemukan")
