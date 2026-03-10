import matplotlib.pyplot as plt


def heuristicValue(start, end):
    # Using Manhattan distance
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def pathFinder(graph, start, end):
    openList = [start]  # Hold nodes that need to be evaluated
    closedList = []  # Hold nodes that should not be evaluated
    cameFrom = {}  # Hold information about previous nodes

    gScores = {node: float("inf") for node in graph}
    gScores[start] = 0

    fScores = {node: float("inf") for node in graph}
    fScores[start] = heuristicValue(start, end)  # Initial f-score based on heuristic

    while openList:
        current = min(openList, key=lambda node: fScores[node])

        if current == end:
            path = []
            while current in cameFrom:
                path.append(current)
                current = cameFrom[current]
            path.append(start)
            return path[::-1]

        openList.remove(current)
        closedList.append(current)

        for neighbour in graph[current]:
            if neighbour in closedList:
                continue

            tentative_gScore = (
                gScores[current] + 1
            )  # Assuming cost of moving to adjacent block is always 1

            # find the neighbour with the minimum g score to move to
            if tentative_gScore < gScores[neighbour]:
                cameFrom[neighbour] = current
                gScores[neighbour] = tentative_gScore
                fScores[neighbour] = tentative_gScore + heuristicValue(neighbour, end)

                if neighbour not in openList:
                    openList.append(neighbour)

    return None  # No path found


def main():
    # Define the graph
    graph = {
        (0, 0): [(1, 0)],
        (0, 2): [(1, 2), (0, 3)],
        (0, 3): [(0, 2), (0, 4)],
        (0, 4): [(1, 4), (0, 3), (0, 5)],
        (0, 5): [(1, 5), (0, 4)],
        (0, 7): [(0, 8)],
        (0, 8): [(1, 8), (0, 7), (0, 9)],
        (0, 9): [(1, 9), (0, 8)],
        (1, 0): [(0, 0), (2, 0), (1, 1)],
        (1, 1): [(2, 1), (1, 0), (1, 2)],
        (1, 2): [(0, 2), (2, 2), (1, 1)],
        (1, 4): [(0, 4), (2, 4), (1, 5)],
        (1, 5): [(0, 5), (2, 5), (1, 4), (1, 6)],
        (1, 6): [(1, 5)],
        (1, 8): [(0, 8), (1, 9)],
        (1, 9): [(0, 9), (2, 9), (1, 8)],
        (2, 0): [(1, 0), (2, 1)],
        (2, 1): [(1, 1), (2, 0), (2, 2)],
        (2, 2): [(1, 2), (3, 2), (2, 1)],
        (2, 4): [(1, 4), (3, 4), (2, 5)],
        (2, 5): [(1, 5), (2, 4)],
        (2, 7): [],
        (2, 9): [(1, 9), (3, 9)],
        (3, 2): [(2, 2), (4, 2)],
        (3, 4): [(2, 4), (4, 4)],
        (3, 9): [(2, 9)],
        (4, 0): [(5, 0), (4, 1)],
        (4, 1): [(4, 0), (4, 2)],
        (4, 2): [(3, 2), (5, 2), (4, 1)],
        (4, 4): [(3, 4), (5, 4), (4, 5)],
        (4, 5): [(5, 5), (4, 4), (4, 6)],
        (4, 6): [(4, 5)],
        (4, 8): [],
        (5, 0): [(4, 0), (6, 0)],
        (5, 2): [(4, 2), (5, 3)],
        (5, 3): [(5, 2), (5, 4)],
        (5, 4): [(4, 4), (5, 3), (5, 5)],
        (5, 5): [(4, 5), (6, 5), (5, 4)],
        (5, 7): [],
        (6, 0): [(5, 0), (7, 0)],
        (6, 5): [(5, 5), (7, 5)],
        (6, 9): [(7, 9)],
        (7, 0): [(6, 0), (8, 0)],
        (7, 2): [(8, 2), (7, 3)],
        (7, 3): [(7, 2), (7, 4)],
        (7, 4): [(7, 3), (7, 5)],
        (7, 5): [(6, 5), (7, 4)],
        (7, 7): [(7, 8)],
        (7, 8): [(7, 7), (7, 9)],
        (7, 9): [(6, 9), (8, 9), (7, 8)],
        (8, 0): [(7, 0), (8, 1)],
        (8, 1): [(8, 0), (8, 2)],
        (8, 2): [(7, 2), (8, 1)],
        (8, 6): [],
        (8, 9): [(7, 9)],
    }

    # Define start and end nodes
    start = (0, 0)
    end = (3, 4)

    # Find the path using A* algorithm
    path = pathFinder(graph, start, end)

    # Extract x and y coordinates of nodes for plotting
    x_coords = [node[0] for node in graph.keys()]
    y_coords = [node[1] for node in graph.keys()]

    # Plot the graph
    plt.figure(figsize=(10, 8))
    plt.scatter(x_coords, y_coords, color="blue")
    for node, neighbours in graph.items():
        for neighbour in neighbours:
            plt.plot([node[0], neighbour[0]], [node[1], neighbour[1]], color="blue")

    # Plot the path
    if path:
        path_x = [node[0] for node in path]
        path_y = [node[1] for node in path]
        plt.plot(path_x, path_y, color="red", linewidth=2, label="Path")

    # Highlight start and end nodes
    plt.scatter(start[0], start[1], color="green", label="Start")
    plt.scatter(end[0], end[1], color="red", label="End")

    plt.title("Graph with A* Path Finding")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()

if __name__ == "__main__":
    main()
