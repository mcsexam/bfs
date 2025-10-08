from collections import deque

graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6', '7'],
    '4': ['2', '8'],
    '5': ['2', '8'],
    '6': ['3', '8'],
    '7': ['3', '8'],
    '8': ['4', '5', '6', '7']
}

def bfs_path_finder(graph, start, goal):
    
    queue = deque([[start]])
    visited = {start}

    while queue:
        
        path = queue.popleft()
        current_node = path[-1]

        
        if current_node == goal:
            return path

        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                
                
                new_path = path + [neighbor]
                
                
                queue.append(new_path)

    
    return None

def main():
    start_node = '1'
    goal_node = '8'
    
    print("--- Breadth-First Search Path Finding (Shortest Path) ---")
    print(f"Start Node: {start_node}")
    print(f"Goal Node: {goal_node}")
    
    
    found_path = bfs_path_finder(graph, start_node, goal_node)

    if found_path:
        
        print("\nShortest Path Found:")
        print(" -> ".join(found_path))
    else:
        print(f"\nNo path found from {start_node} to {goal_node}.")

if __name__ == '__main__':
    main()
