
from Import.unionfind.quickFind import QuickFindBalanced
from Import.Graph.datastruct.Stack import PilaArrayList as Stack
from random import randint
from Import.Graph.graph.Graph_AdjacencyList import GraphAdjacencyList

def makeGraph(n, bool):
    '''
    This function will create a graph with or without a cycle composed of n nodes, depending by the value of bool
    :param n: int
    :param bool: bool
    :return: graph
    '''

    if n == 0:
        raise ('Grafo vuoto riprovare con n > 0')

    graph = GraphAdjacencyList()
    nodes = []
    max_arc = n * randint(1,10) #number of edges after the first linking

    # inserting nodes
    for i in range(n):
        node = graph.addNode(i)
        nodes.append(node)

    # linking nodes
    for i in range(len(nodes) - 1):
        #insert an edge not oriented
        graph.insertEdgeNO(nodes[i].id, nodes[i + 1].id, nodes[i].id + nodes[i + 1].id)

    # inserting the cycle if bool
    if bool:
        if n < 3:#impossibile creare un grafo ciclico con 2 nodi
            pass
        elif n == 3:
            graph.insertEdgeNO(nodes[0].id,nodes[2].id,nodes[0].id + nodes[2].id)
        else:
            '''
            k = randint(0, len(nodes)-1)
            if k>=len(nodes)-2:
                h = k-2
            else:
                h = k+2

            graph.insertEdgeNO(nodes[k].id, nodes[h].id, nodes[k].id + nodes[h].id)
            '''
            for _ in range(0,max_arc):
                k = randint(0, len(nodes)-1)
                j= randint(0, len(nodes)-1)
                dif = nodes[k].id - nodes[j].id
                if (dif)>= -1 and (dif)<= 1 :
                    pass
                else:
                    graph.insertEdgeNO(nodes[k].id, nodes[j].id, nodes[k].id + nodes[j].id)
    return graph

def hasCycleUF(G):

    uf = QuickFindBalanced()

    edgeslist=G.trovaArchi()
    app_dict={}

    #viene inizializzata la struttura UnionFind 'traducendo' il grafo

    for node in G.trovaNodi():
        ufnode = uf.makeSet(node)
        app_dict[node] = ufnode

    #inizio della procedura descritta nello pseudocodice
    iterator = iter(edgeslist) #iterator per scandire tutti gli edge del grafo
    try:
        while True:
            arc = next(iterator)
            x = app_dict[arc[0]]
            y = app_dict[arc[1]]

            if uf.find(x) == uf.find(y):
                return True  # trovato ciclo
            else:
                uf.union(x.father, y.father)
    except StopIteration:
        pass
    return False  # nessun ciclo trovato

def hasCycleDFS(G):
    #viene scelto un nodo casuale e selezionato come vertice di partenza della visita
    a=randint(0,len(G.nodes)-1)
    rootId= G.nodes[a].id

    # stack initialization
    s = Stack()
    s.push(rootId)
    explored = {rootId}  # nodes already explored

    while not s.isEmpty():  # while there are nodes to explore ...
        node = s.pop()  # get the node from the stack

        k = 0 #usato per ovviare alla definizione di grafo non orientato mediante lista di adiacenza
        for adj_node in G.getAdj(node):
            if adj_node not in explored:
                s.push(adj_node)
                explored.add(adj_node)
            else:
                k += 1  #poichè non orientato ogni nodo avrà almeno il percorso di ritorno a un nodo esplorato

            if k > 1: #se a partire dallo stesso nodo vi sono più nodi in explored vuol dire che vi è un ciclo
                return True
    #completata la visita senza aver tovato cicli
    return False

#esempio di esecuzione

if __name__ == '__main__':
    print("\nALGORITHM WITH NO CYCLE")
    graph = makeGraph(200, 0)
    graph.print()
    print("\nResult from DFS algorithm:")
    print(hasCycleDFS(graph))
    print("\nResult from UF algorithm:")
    print(hasCycleUF(graph))

    print("\nALGORITHM WITH CYCLE")
    graph = makeGraph(200, 1)
    graph.print()
    print("\nResult from DFS algorithm:")
    print(hasCycleDFS(graph))
    print("\nResult from UF algorithm:")
    print(hasCycleUF(graph))