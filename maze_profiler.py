import time

# 0 = Open Path, 1 = Wall
MAZE = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0]
]

START = (0, 0)
GOAL = (5, 5)

# --- VISUALIZER FUNCTION ---
def print_maze_with_path(grid, path, title):
    print(f"=== {title} ===")
    for r in range(len(grid)):
        row_str = ""
        for c in range(len(grid[0])):
            if (r, c) == START:
                row_str += "S "      # S = Start
            elif (r, c) == GOAL:
                row_str += "G "      # G = Goal
            elif path and (r, c) in path:
                row_str += "* "      # * = The path taken
            elif grid[r][c] == 1:
                row_str += "█ "      # █ = Solid wall
            else:
                row_str += ". "      # . = Unvisited open space
        print(row_str)
    print(f"Step-by-Step Route: {path}\n")

# --- ALGORITHM LOGIC ---
def get_neighbors(position, grid):
    row, col = position
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
            neighbors.append((r, c))
    return neighbors

def solve_bfs(grid, start, goal):
    queue = [[start]]
    visited = {start}
    nodes_expanded = 0
    
    while queue:
        path = queue.pop(0)
        current = path[-1]
        nodes_expanded += 1
        
        if current == goal:
            return path, nodes_expanded
            
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
    return None, nodes_expanded

def solve_dfs(grid, start, goal):
    stack = [[start]]
    visited = {start}
    nodes_expanded = 0
    
    while stack:
        path = stack.pop()
        current = path[-1]
        nodes_expanded += 1
        
        if current == goal:
            return path, nodes_expanded
            
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
                
    return None, nodes_expanded

# --- PROFILING & EXECUTION ---
def run_profiling(iterations=1000):
    # 1. Profile BFS
    start_time = time.perf_counter()
    for _ in range(iterations):
        bfs_path, bfs_nodes = solve_bfs(MAZE, START, GOAL)
    end_time = time.perf_counter()
    bfs_avg_time_ms = ((end_time - start_time) * 1000) / iterations

    # 2. Profile DFS
    start_time = time.perf_counter()
    for _ in range(iterations):
        dfs_path, dfs_nodes = solve_dfs(MAZE, START, GOAL)
    end_time = time.perf_counter()
    dfs_avg_time_ms = ((end_time - start_time) * 1000) / iterations

    # 3. Print the Visual Maps
    print_maze_with_path(MAZE, bfs_path, "BFS PATH VISUALIZATION")
    print_maze_with_path(MAZE, dfs_path, "DFS PATH VISUALIZATION")

    # 4. Print the Data Table Numbers
    print("=== PERFORMANCE DATA ===")
    print(f"BFS: {bfs_avg_time_ms:.6f} ms | Nodes Expanded: {bfs_nodes} | Steps: {len(bfs_path)-1}")
    print(f"DFS: {dfs_avg_time_ms:.6f} ms | Nodes Expanded: {dfs_nodes} | Steps: {len(dfs_path)-1}")

if __name__ == "__main__":
    run_profiling(iterations=20000)
