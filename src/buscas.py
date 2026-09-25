import heapq
from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Ordem: Norte, Sul, Oeste, Leste

def get_neighbors(pos, grid):
    n = len(grid)
    r, c = pos
    neighbors = []
    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != "#":
            neighbors.append((nr, nc))
    return neighbors

def reconstruct_path(parent, target):
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parent.get(curr)
    return path[::-1]

def get_cost(path, grid):
    cost_map = {".": 1, "~": 4}
    return sum(cost_map[grid[r][c]] for r, c in path[1:])

def bfs(grid):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    nodes_expanded = 0
    max_frontier = 1

    while queue:
        max_frontier = max(max_frontier, len(queue))
        curr = queue.popleft()
        nodes_expanded += 1

        if curr == goal:
            path = reconstruct_path(parent, goal)
            return {"custo": get_cost(path, grid), "passos": len(path) - 1, "nos_expandidos": nodes_expanded, "fronteira_max": max_frontier}

        for nxt in get_neighbors(curr, grid):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = curr
                queue.append(nxt)
    return None

def dfs(grid):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)
    stack = [start]
    visited = set()
    parent = {start: None}
    nodes_expanded = 0
    max_frontier = 1

    while stack:
        max_frontier = max(max_frontier, len(stack))
        curr = stack.pop()
        
        if curr in visited:
            continue
        visited.add(curr)
        nodes_expanded += 1

        if curr == goal:
            path = reconstruct_path(parent, goal)
            return {"custo": get_cost(path, grid), "passos": len(path) - 1, "nos_expandidos": nodes_expanded, "fronteira_max": max_frontier}

        for nxt in reversed(get_neighbors(curr, grid)):
            if nxt not in visited:
                if nxt not in parent:
                    parent[nxt] = curr
                stack.append(nxt)
    return None

def ucs(grid):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)
    cost_map = {".": 1, "~": 4}
    pq = []
    counter = 0
    heapq.heappush(pq, (0, counter, start))
    cost_so_far = {start: 0}
    parent = {start: None}
    nodes_expanded = 0
    max_frontier = 1

    while pq:
        max_frontier = max(max_frontier, len(pq))
        current_cost, _, curr = heapq.heappop(pq)

        if curr == goal:
            path = reconstruct_path(parent, goal)
            return {"custo": current_cost, "passos": len(path) - 1, "nos_expandidos": nodes_expanded, "fronteira_max": max_frontier}

        nodes_expanded += 1

        for nxt in get_neighbors(curr, grid):
            new_cost = current_cost + cost_map[grid[nxt[0]][nxt[1]]]
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                parent[nxt] = curr
                counter += 1
                heapq.heappush(pq, (new_cost, counter, nxt))
    return None

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def a_star(grid, weight=1.0):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)
    cost_map = {".": 1, "~": 4}
    pq = []
    counter = 0
    h_start = weight * manhattan_distance(start, goal)
    heapq.heappush(pq, (0 + h_start, 0, counter, start))
    g_score = {start: 0}
    parent = {start: None}
    nodes_expanded = 0
    max_frontier = 1

    while pq:
        max_frontier = max(max_frontier, len(pq))
        f, g, _, curr = heapq.heappop(pq)

        if curr == goal:
            path = reconstruct_path(parent, goal)
            return {"custo": g, "passos": len(path) - 1, "nos_expandidos": nodes_expanded, "fronteira_max": max_frontier}

        nodes_expanded += 1

        for nxt in get_neighbors(curr, grid):
            tentative_g = g + cost_map[grid[nxt[0]][nxt[1]]]
            if nxt not in g_score or tentative_g < g_score[nxt]:
                g_score[nxt] = tentative_g
                parent[nxt] = curr
                h = weight * manhattan_distance(nxt, goal)
                counter += 1
                heapq.heappush(pq, (tentative_g + h, tentative_g, counter, nxt))
    return None