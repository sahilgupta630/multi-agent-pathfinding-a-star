import matplotlib.pyplot as plt


def heuristicValue(start, end):
    # Using Manhattan distance
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def visualizeMap(graph, starts, ends, paths):
    for node in graph:
        for neighbour in graph[node]:
            plt.plot(
                [node[0], neighbour[0]], [node[1], neighbour[1]], "black"
            )  # plot edges as blue lines

    for start in starts:
        plt.plot(start[0], start[1], "go")  # plot the start nodes as green circles

    for end in ends:
        plt.plot(end[0], end[1], "ro")  # plot the goal nodes as red circles

    if paths:
        # enumerating as we need the index as well
        for i, path in enumerate(paths):
            for agent_path in path:
                path_x = [node[0] for node in agent_path]
                path_y = [node[1] for node in agent_path]
                plt.plot(
                    path_x, path_y, label=f"Agent {i+1}"
                )  # plot the paths as red lines

    plt.title("Multi-Agent A* Pathfinding Visualization")
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.show()


def multiAgentPathFinder(graph, starts, ends):
    openLists = {
        start: [start] for start in starts
    }  # hold nodes that need to be evaluated for each agent
    closedLists = {
        start: [] for start in starts
    }  # hold nodes that should not be evaluated for each agent
    cameFrom = {
        start: {} for start in starts
    }  # hold information about previous nodes for each agent

    # initialize dicts for scores
    gScores = {start: {node: float("inf") for node in graph} for start in starts}
    fScores = {start: {node: float("inf") for node in graph} for start in starts}

    starts = tuple(starts)  # Convert starts to tuple
    ends = tuple(ends)  # Convert ends to tuple

    paths = [[] for _ in starts]  # Hold paths for each agent

    constraint_tree = {node: [] for node in graph}  # Initialize constraint tree

    for start in starts:
        gScores[start][start] = 0

        fScores[start][start] = heuristicValue(start, ends[starts.index(start)])
        # initial fScore is simply the heuristic as gScores are zero

    nextNodes = {
        start: start for start in starts
    }  # Hold next node to be evaluated for each agent

    # keep iterating until all the open lists are empty, any() returns true if the argument contains even a single truthy value
    while any(openLists.values()):

        for start in starts:
            minFScore = float("inf")
            nextNode = None

            # Find node with minimum f score for the current agent
            for element in openLists[start]:
                fScore = gScores[start][element] + heuristicValue(
                    element, ends[starts.index(start)]
                )
                if fScore <= minFScore:
                    minFScore = fScore
                    nextNode = element

            if nextNode is None:
                continue

            # Evaluate the next node
            openLists[start].remove(nextNode)
            closedLists[start].append(nextNode)

            if nextNode == ends[starts.index(start)]:
                # If the agent reached its destination, backtrack to find the path
                path = []
                while nextNode in cameFrom[start]:
                    path.append(nextNode)
                    nextNode = cameFrom[start][nextNode]
                path.append(start)
                path = tuple(
                    path[::-1]
                )  # Convert path to tuple of tuples with reversed path [::-1]
                paths[starts.index(start)].append(path)

            # Update scores and add neighbors to open list
            for neighbour in graph[nextNode]:
                if neighbour in closedLists[start]:
                    continue

                # compare tentative gScore to find the neighbour with the minimum g cost
                gScore = gScores[start][nextNode] + 1

                if gScore < gScores[start][neighbour]:

                    # add this node with lowest g cost to the open list and explore it in next iteration
                    cameFrom[start][neighbour] = nextNode
                    gScores[start][neighbour] = gScore
                    fScores[start][neighbour] = gScore + heuristicValue(
                        neighbour, ends[starts.index(start)]
                    )
                    if neighbour not in openLists[start]:
                        openLists[start].append(neighbour)

                    # Update constraint tree
                    constraint_tree[neighbour].append(nextNode)

            nextNodes[start] = (
                nextNode  # Update next node to be evaluated for the current agent
            )

        # Check for conflicts and resolve them
        # create an empty dictionary
        node_counts = {}

        for start in starts:
            # Add the number of agents on each node to this dictionary
            if nextNodes[start] not in node_counts:
                node_counts[nextNodes[start]] = 1
            else:
                node_counts[nextNodes[start]] += 1

        # if more than one agents are at the same node, its a conflict
        conflicted_nodes = [node for node, count in node_counts.items() if count > 1]

        for node in conflicted_nodes:
            agents_at_node = [start for start in starts if nextNodes[start] == node]
            for start in agents_at_node:
                if node in openLists[start]:  # Check if node is in the open list
                    # simply remove the node from the open list for the agent and run the pathfinder again to resolve the conflict
                    # this assumes waiting is not a possible option as given in the problem statement, so it changes the map itself
                    openLists[start].remove(node)
                    closedLists[start].append(node)

    # Print constraint tree
    print("Constraint Tree:")
    for node, constraints in constraint_tree.items():
        print(f"Node {node}: {constraints}")

    return paths


def main():
    # using a graph as the input map, where each value tells the node to which movement is possible from the key coordinate
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

    starts = [(0, 0), (1, 0)]  # Starting positions for each agent
    ends = [(8, 0), (4, 6)]

    paths = multiAgentPathFinder(graph, starts, ends)
    print(paths)

    visualizeMap(graph, starts, ends, paths)

if __name__ == "__main__":
    main()
