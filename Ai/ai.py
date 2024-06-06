import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def init(self, value, children=[]):
        self.value = value
        self.children = children

def alpha_beta(node, alpha, beta, is_maximizing, graph, pruned_nodes):
    if not node.children:
        return node.value
    
    if is_maximizing:
        best_value = float('-inf')
        for child in node.children:
            value = alpha_beta(child, alpha, beta, False, graph, pruned_nodes)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                pruned_nodes.append(child.value)  # Add pruned node to the list
                break
            graph.add_edge(node.value, child.value)  # Add edge for visualization
            pos = nx.spring_layout(graph)
            nx.draw(graph, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=2000)
            plt.text(0.1, 0.9, f'Max(Current Node {node.value}), Best Value {best_value}', fontsize=12, color='black', ha='left', va='top', transform=plt.gca().transAxes)  # Plot text at a static position
            plt.show()
        return best_value
    else:
        best_value = float('inf')
        for child in node.children:
            value = alpha_beta(child, alpha, beta, True, graph, pruned_nodes)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                pruned_nodes.append(child.value)  # Add pruned node to the list
                break
            graph.add_edge(node.value, child.value)  # Add edge for visualization
            pos = nx.spring_layout(graph)
            nx.draw(graph, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=2000)
            plt.text(0.1, 0.9, f'Min(Current Node {node.value}), Best Value {best_value}', fontsize=12, color='black', ha='left', va='top', transform=plt.gca().transAxes)  # Plot text at a static position
            plt.show()
        return best_value

# Construct the tree
node8 = Node(5)
node9 = Node(6)
node4 = Node('d',[node8, node9])
node10 = Node(7)
node11 = Node(4)
node12 = Node(5)
node5 = Node('e', [node10])
node6 = Node('f', [node11])
node13 = Node(6)
node7 = Node('g', [node12, node13])
node3 = Node('c', [node6, node7])
node2 = Node('b', [node4, node5])
node1 = Node('a', [node2, node3])

graph = nx.DiGraph()
pruned_nodes = []

# Run alpha-beta with visualization
print("\nAlpha-Beta Pruning:")
alpha_beta_result = alpha_beta(node1, float('-inf'), float('inf'), True, graph, pruned_nodes)
print("Alpha-Beta Result:", alpha_beta_result)

# Draw the graph for alpha-beta
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=2000)
plt.title('Alpha-Beta Pruning: Final Result')
plt.show()

# Print pruned nodes
print("Pruned Nodes:", pruned_nodes)