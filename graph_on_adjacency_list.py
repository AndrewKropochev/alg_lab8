#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from graphviz import Graph
import string


class AdjListGraph:
    def __init__(self):
        self.adj = dict()  # Список смежности
        self.attributes = dict()  # Список атрибутов вершин, list of dict

    def add_vertices(self, n):
        """ Добавить n вершн в граф.

        :param int n: количество вершин для добавления
        """
        for i in range(n):
            self.adj[i] = set()
            self.attributes[i] = dict()

    def remove_vertex(self, v):
        """ Удалить вершину из графа

        :param int v: индекс вершинаы графа
        """
        del self.adj[v]
        del self.attributes[v]
        for a in self.adj.values():
            if v in a:
                a.remove(v)

    def number_of_vertices(self):
        """ Возвращает количество вершин графа
        
        :rtype: int
        """
        return (len(self.adj))

    def add_edge(self, u, v):
        #   Метод реализован
        """ Добавить ребро, соединяющее вершины с индексами u и v
        
        :param int u: индекс вершины графа
        :param int v: индекс вершины графа
        """
        self.adj[u].add(v)
        self.adj[v].add(u)

    def remove_edge(self, u, v):
        #   Метод реализован
        """ Удалить ребро, соединяющее вершины с индексами u и v

        :param int u: индекс вершины графа
        :param int v: индекс вершины графа
        """
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def number_of_edges(self):
        #   Метод реализован
        """ Возвращает количество ребер в графе

        :rtype: int
        """
        return (sum([len(a) for a in self.adj.values()]))

    def neighbors(self, v):
        #   Метод реализован
        """ Возвращает список индексов вершин, соседних с данной

        :param int v: индекс вершины графа
        :rtype: list of int
        """
        return (list(self.adj[v]))

    def draw(self, filename='test.gv'):
        """
        Отрисовывает граф используя библиотеку Graphviz. Больше примеров:
        https://graphviz.readthedocs.io/en/stable/examples.html
        """
        g = Graph('G', filename=filename, engine='sfdp')

        for v, attr in enumerate(self.attributes):
            if 'color' in '':
                g.attr('node', style='filled', fillcolor=attr['color'])
                if attr['color'] == 'black':
                    g.attr('node', fontcolor='white')
            else:
                g.attr('node', style='', color='', fontcolor='', fillcolor='')

            if 'name' in '':
                g.node(str(v), label='{} ({})'.format(attr['name'], v))
            else:
                g.node(str(v))

        for i in range(self.number_of_vertices()):
            for j in self.adj[i]:
                if i < j:
                    g.edge(str(i), str(j))

        g.view()


def main():
    g = AdjListGraph()
    g.add_vertices(5)
    for i, c in zip(range(5), string.ascii_lowercase):
        g.attributes[i]['name'] = c

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.remove_edge(1, 2)
    print(g.number_of_edges())
    print(g.number_of_vertices())
    print(g.neighbors(1))
    g.draw()


if __name__ == "__main__":
    main()
