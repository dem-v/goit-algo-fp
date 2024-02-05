import networkx as nx
import matplotlib.pyplot as plt


class RealLifeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.apices = [i for i in range(0, 15)]
        self.ribs = {(0, 1): 20, (1, 2): 20, (0, 3): 35
            , (2, 4): 10, (3, 4): 10, (4, 5): 20
            , (5, 6): 20, (4, 10): 35, (10, 6): 15
            , (4, 7): 20, (5, 8): 20, (6, 9): 30
            , (9, 11): 15, (11, 12): 10, (7, 12): 10
            , (8, 13): 10, (12, 13): 10, (13, 14): 40}

        self.graph.add_nodes_from(self.apices)
        for i, v in self.ribs.items():
            self.graph.add_edge(i[0], i[1], weight=v)

    def get_graph(self):
        return self.graph

    def get_neighbors_dict(self):
        return {i: [j for j in self.graph[i]] for i in self.graph}

    def get_neighbors_dict_with_weights(self):
        return {i: {j: self.graph[i][j]['weight'] for j in self.graph[i]} for i in self.graph}

    def draw(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()

    def describe(self):
        num_nodes = self.graph.number_of_nodes()  # 4
        num_edges = self.graph.number_of_edges()  # 4
        print(
            f"Даний граф складається з {num_nodes} вершин і {num_edges} ребер.\n")
        print(
            f"Граф має значення центральності {nx.degree_centrality(self.graph)}, близкості {nx.closeness_centrality(self.graph)}', посередницвта {nx.betweenness_centrality(self.graph)}")


if __name__ == "__main__":
    graph = RealLifeGraph()
    graph.draw()
    graph.describe()
