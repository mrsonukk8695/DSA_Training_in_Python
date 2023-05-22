class MyGraph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    def Mybfs(self,vertex):
        visited=[vertex]
        myqueue=[vertex]
        while myqueue:
            deVertiex=myqueue.pop()
            print(deVertiex)
            for adjacentVertex in self.gdict[deVertiex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    myqueue.append(adjacentVertex)
    def mydfs(self,vertex):
        visited=[vertex]
        mystack=[vertex]
        while mystack:
            popvertex=mystack.pop()
            print(popvertex)
            for adjecentVertex in self.gdict[popvertex]:
                if adjecentVertex not in visited:
                    visited.append(adjecentVertex)
                    mystack.append(adjecentVertex)

dict={"a":["b","c"],
    "b":["a","d","e"],
    "c":["a","e"],
    "d":["d","e","f"],
    "e":["d","f","c"],
    "f":[]
    }                    
gjob=MyGraph(dict)
gjob.Mybfs("a")
gjob.mydfs("e")