import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, key, color="#008080"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла
        self.text_color = 'black' if lighter_than_median(color) else 'white'

    def __str__(self):
        return str(self.val)


def lighter_than_median(hex_color):
    r = 0.2126 * int(hex_color[1:3], 16)
    g = 0.7152 * int(hex_color[3:5], 16)
    b = 0.0722 * int(hex_color[5:7], 16)

    return r+g+b > 135


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = colors if colors else [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Додавання вузла до купи
def convert_heap_to_tree_representation(heap):
    root = Node(heapq.heappop(heap))
    q = deque()
    q.append(root)
    while q:
        curr_node = q.popleft()
        curr_node.left = Node(heapq.heappop(heap))
        q.append(curr_node.left)
        if len(heap) == 0:
            break
        curr_node.right = Node(heapq.heappop(heap))
        q.append(curr_node.right)
        if len(heap) == 0:
            break

    return root


# Створення купи

def build_normal_tree(source_list=None):
    if source_list is None:
        # Створення дерева
        root = Node(0)
        root.left = Node(12)
        root.left.left = Node(5)
        root.left.right = Node(10)
        root.right = Node(1)
        root.right.left = Node(3)
        root.right.right = Node(4)
        root.left.left.left = Node(8)
        return root
    else:
        if len(source_list) == 0:
            return None

        deq = deque()
        root = Node(source_list.pop(0))
        deq.append(root)

        while deq:
            curr_node = deq.popleft()
            if len(source_list) == 0:
                break
            curr_node.left = Node(source_list.pop(0))
            deq.append(curr_node.left)
            if len(source_list) == 0:
                break
            curr_node.right = Node(source_list.pop(0))
            deq.append(curr_node.right)
            if len(source_list) == 0:
                break
        return root


if __name__ == "__main__":
    # Відображення дерева
    root = build_normal_tree()
    draw_tree(root)

    # Відображення купи
    source_list = [0, 12, 5, 10, 1, 3, 4, 8]
    heapq.heapify(source_list)
    root = convert_heap_to_tree_representation(source_list)
    draw_tree(root)
