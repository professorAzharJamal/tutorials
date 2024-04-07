import math

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

def minimax(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or not node.children:
        return node.value

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in node.children:
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

# Example usage
if __name__ == "__main__":
    # Example tree structure
    node1 = Node(3)
    node2 = Node(5)
    node3 = Node(6)
    node4 = Node(9)
    node5 = Node(1)
    node6 = Node(2)
    node7 = Node(0)
    node8 = Node(7)

    node1.children = [node2, node3, node4]
    node2.children = [node5, node6]
    node3.children = [node7, node8]

    # Calling the minimax function with alpha-beta pruning
    result = minimax(node1, 3, float('-inf'), float('inf'), True)
    print("Optimal value:", result)
