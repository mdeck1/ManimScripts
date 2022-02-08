from manim import *

import networkx as nx


# class DrawTree(Scene):
#     def construct(self):
#         vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         edges = [
#             (1, 2),
#             (1, 3),
#             (2, 4),
#             (2, 5),
#             (3, 6),
#             (3, 7),
#             (4, 8),
#             (4, 9)]
#         g = Graph(vertices, edges, layout="circular", layout_scale=3,
#                   labels=True,
#                   # vertex_config={7: {"fill_color": RED}},
#                   # edge_config={(1, 7): {"stroke_color": RED},
#                   #              (2, 7): {"stroke_color": RED},
#                   #              (4, 7): {"stroke_color": RED}}
#                   )
#         self.add(g)


class Tree(Scene):
    def construct(self):
        # nx_graph = nx.Graph()
        #
        # nx_graph.add_node(1)

        nodes = [1]
        edges = []

        for index in range(2, 10):
            nodes = nodes + [index]  # nx_graph.add_node(index)
            edges = edges + [(int(index/2), index)]  # nx_graph.add_edge(int(index / 2), index)

        graph = Graph(nodes, edges, labels=True, root_vertex=1)  # , layout="circular", list(nx_graph.nodes), list(nx_graph.edges)

        self.play(Create(graph), run_time=10)
        # self.play(graph.animate.change_layout("tree"))
        # self.wait()
