import matplotlib.pyplot as plot

def visualize_graph(graph):
    plot.figure(figsize=(8, 8))
    for node in graph:
        plot.plot(node[0], node[1], 'bo')  # plot nodes as blue circles
        for neighbor in graph[node]:
            plot.plot([node[0], neighbor[0]], [node[1], neighbor[1]], 'b')  # plot edges as blue lines

    plot.title('A* Pathfinding Visualization')
    plot.xlabel('X-coordinate')
    plot.ylabel('Y-coordinate')
    plot.grid(True)
    plot.axis('equal')
    plot.show()


def main():
    # Define the graph
    graph = {}

    # Define the grid
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    # Convert grid to graph
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                neighbors = []
                if i > 0 and grid[i - 1][j] == 1:
                    neighbors.append((i - 1, j))
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    neighbors.append((i + 1, j))
                if j > 0 and grid[i][j - 1] == 1:
                    neighbors.append((i, j - 1))
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    neighbors.append((i, j + 1))
                graph[(i, j)] = neighbors

    print(graph)

    # Visualize the graph
    visualize_graph(graph)

if __name__ == "__main__":
    main()