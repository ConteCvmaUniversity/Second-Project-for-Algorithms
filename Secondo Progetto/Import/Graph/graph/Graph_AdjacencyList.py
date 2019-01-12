
from Import.Graph.graph.GraphB import GraphBase, Edge
from Import.Graph.list.DoubleLinkedList import ListaDoppiamenteCollegata as List


class GraphAdjacencyList(GraphBase):
    """
    A graph, implemented as an adjacency list.
    Each node u has a list containing its adjacent nodes, that is nodes v such
    that exists an edges (u,v).
    Let's define deg(v) = degree of vertex v, or t
    ---
    Memory Complexity: O(|V|+|E|)
    """

    def __init__(self):
        """
        Constructor.
        """
        super().__init__()
        self.adj = {}  # adjacency lists {nodeID:listOfAdjacentNodes}

    def numEdges(self):
        """
        Return the number of edges.
        :return: the number of edges.
        """
        return sum(len(adj_list) for adj_list in self.adj.values())

    def addNode(self, elem):
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :return: the create node.
        """
        newnode = super().addNode(elem)  # create a new node with the correct ID

        self.nodes[newnode.id] = newnode  # add the new node to the dictionary
        self.adj[newnode.id] = List()  # create the adjacency list for the new node

        return newnode

    def deleteNode(self, nodeId):
        """
        Remove the specified node.
        O(m)
        :param nodeId: the node ID (integer).
        :return: void.
        """
        try:
            self.nodes[nodeId]  # check if nodeId exists
        except KeyError:
            return   # node with nodeId not present

        # remove the node from the set of nodes, that is to remove the node
        # from the dictionary nodes
        del self.nodes[nodeId]

        # remove all edges starting from the node, that is to remove the
        # adjacency list for the node
        del self.adj[nodeId]

        # remove all edges pointing to the node, that is to remove the node
        # from all the adjacency lists
        for adj in self.adj.values():
            curr = adj.getFirstRecord()
            while curr is not None:
                if curr.elem == nodeId:
                    adj.deleteRecord(curr)
                curr = curr.next

    def deg(self, nodeId):
        """
        Return the node degree.
        :param nodeId: the node id.
        :return: the node degree.
        """
        if nodeId not in self.nodes:
            return 0
        else:
            return len(self.adj[nodeId])

    def getNode(self, id):
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
        """
        return None if id not in self.nodes else self.nodes[id]

    def getNodes(self):
        """
        Return the list of nodes.
        :return: the list of nodes.
        """
        return list(self.nodes.values())

    def insertEdge(self, tail, head, weight=None):
        """
        Add a new edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        :return: the created edge, if created; None, otherwise.
        """
        # if tail and head exist, add the entry into the adjacency list
        if tail in self.nodes and head in self.nodes:  # TODO overwrite if edge already exists
            self.adj[tail].addAsLast(head)

    def deleteEdge(self, tail, head):
        """
        Remove the specified edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: void.
        """
        # if tail and head exist, delete the edge
        if tail in self.nodes and head in self.nodes:
            curr = self.adj[tail].getFirstRecord()
            while curr is not None:
                if curr.elem == head:
                    self.adj[tail].deleteRecord(curr)
                    break
                curr = curr.next

    def getEdge(self, tail, head):
        """
        Return the node, if exists.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: the edge, if exists; None, otherwise.
        """
        if tail in self.nodes and head in self.nodes:
            curr = self.adj[tail].getFirstRecord()
            while curr is not None:
                if curr.elem == head:
                    return Edge(tail, head, None)
                curr = curr.next
        return None

    def getEdges(self):
        """
        Return the list of edges.
        :return: the list of edges.
        """
        edges = []
        for adj_item in self.adj.items():
            curr = adj_item[1].getFirstRecord()
            while curr is not None:
                edges.append(Edge(adj_item[0], curr.elem, None))
                curr = curr.next
        return edges

    def isAdj(self, tail, head):
        """
        Checks if two nodes ar adjacent.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: True, if the two nodes are adjacent; False, otherwise.
        """
        # if tail and head exist, look for the entry in the adjacency list
        if tail in self.nodes and head in self.nodes:
            curr = self.adj[tail].getFirstRecord()
            while curr is not None:
                nodeId = curr.elem
                if nodeId == head:
                    return True
                curr = curr.next

        # else, return False
        return False

    def getAdj(self, nodeId):
        """
        Return all nodes adjacent to the one specified.
        :param nodeId: the node id.
        :return: the list of nodes adjacent to the one specified.
        """
        result = []
        curr = self.adj[nodeId].getFirstRecord()
        while curr is not None:
            result.append(curr.elem)
            curr = curr.next
        return result

    def print(self):
        """
        Print the graph.
        :return: void.
        """
        # if the adjacency list is empty ...
        if self.isEmpty():
            print("Adjacency List: EMPTY")
            return

        # else ...
        print("Adjacency Lists:")
        for adj_item in self.adj.items():
            print("{}:{}".format(adj_item[0], adj_item[1]))

    #funzioni aggiunte alla classe
    def trovaNodi(self):
        #funzione che crea una lista contenente gli id dei nodi

        list=[]
        for nod in self.nodes.items():
            list.append(nod[0])
        return list

    def trovaArchi(self):
        # funzione che crea una lista di archi in formato (x.id,y.id)

        list=[]
        app_list=[]
        for adj_item in self.adj.items():
            curr = adj_item[1].getFirstRecord()
            while curr is not None:

                if curr.elem in app_list:
                    curr=curr.next
                else:
                    list.append((adj_item[0],curr.elem))
                    curr=curr.next
            app_list.append(adj_item[0])

        return list

    def insertEdgeNO(self, tail, head, weight=None):
        """
        Add a new edge not oriented.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        :return: the created edge, if created; None, otherwise.
        """
        # if tail and head exist, add the entry into the adjacency list
        if tail in self.nodes and head in self.nodes:  # TODO overwrite if edge already exists
            self.adj[tail].addAsLast(head)
            self.adj[head].addAsLast(tail)
