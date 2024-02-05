from fp_task3_from_hw6_graphbase import RealLifeGraph
from fp_task3_PriorityQueue import PriorityQueue
import timeit


def dijkstra_previous(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


def dijkstra_heap(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = PriorityQueue()
    pq.enqueue(start, 0)

    while not pq.is_empty():
        # Видаляємо поточну вершину з множини невідвіданих
        current_vertex = pq.dequeue()

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            new_distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                pq.enqueue(neighbor, new_distance)

    return distances


if __name__ == "__main__":
    graph = RealLifeGraph()
    d_w = graph.get_neighbors_dict_with_weights()
    print(d_w)
    a = None
    print(
        f"Час виконання алгоритму Дейсктри з ДЗ 6: {timeit.timeit('global a; a = dijkstra_previous(graph.get_neighbors_dict_with_weights(), 0)', globals=globals(), number=1)}")
    print(f"Відстані до всіх вершин від 0, алгоритм Дейсктри з ДЗ 6: \n{a}")
    a_h = None
    print(
        f"Час виконання алгоритму Дейсктри з купою: {timeit.timeit('global a_h; a_h = dijkstra_heap(graph.get_neighbors_dict_with_weights(), 0)', globals=globals(), number=1)}")
    print(f"Відстані до всіх вершин від 0, алгоритм Дейсктри з купою: \n{a_h}")
