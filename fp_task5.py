from fp_task4 import Node, draw_tree, build_normal_tree
from collections import deque


def dfs_iterative(start_vertex, colors_list: list):
    colors_list = colors_list.copy()
    visited = set()
    colors_dic = {}
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            colors_dic[vertex.val] = colors_list.pop(0)
            # Додаємо сусідні вершини до стеку
            if vertex.left is not None:
                stack.extend([vertex.left])
            if vertex.right is not None:
                stack.extend([vertex.right])

    return visited, colors_dic


def bfs_iterative(root, colors_list: list):
    colors_list = colors_list.copy()
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([root])
    colors_dic = {}

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            colors_dic[vertex.val] = colors_list.pop(0)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            if vertex.left is not None:
                queue.extend({vertex.left} - visited)
            if vertex.right is not None:
                queue.extend({vertex.right} - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited, colors_dic


def recolor_tree(root: Node, colors_dic: dict):
    root.color = colors_dic[root.val] if root.val in colors_dic else '#008080'
    if root.left is not None:
        recolor_tree(root.left, colors_dic)
    if root.right is not None:
        recolor_tree(root.right, colors_dic)
    return root


if __name__ == "__main__":
    source_list = [0, 12, 5, 10, 1, 3, 4, 8]
    max_len = len(source_list)

    # Ініціалізація кольорів
    offset = 0x6060
    h = 0x000000
    colors = [f'#{(h + i * 0x100 + i):06x}' for i in range(0x60, 0xff + 1, (0xff + 1 - 0x60) // (max_len + 1))]

    root = build_normal_tree(source_list)
    visited, colors_dic = dfs_iterative(root, colors)
    print(visited)
    root = recolor_tree(root, colors_dic)
    draw_tree(root)

    visited, colors_dic = bfs_iterative(root, colors)
    print(visited)
    root = recolor_tree(root, colors_dic)
    draw_tree(root)
