class graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
                
    def getPath(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict.keys():
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                newPath=self.getPath(node,end,path)
            for p in newPath:
                paths.append(p)
        
        return paths

    def get_shortest_path(self,start,end,path=[]):
        path=path+[start]
        if start not in self.graph_dict:
            return []
        if start==end:
            return path
        
        shortestPath=None
        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.get_shortest_path(node,end,path)
            if sp:
                if shortestPath is None or len(sp)<len(shortestPath):
                    shortestPath=sp
        return shortestPath

if __name__=='__main__':
    routes=[
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","Newyork"),
        ("Dubai","Newyork"),
        ("Newyork","Torronto")
    ]
    g=graph(routes)
    print(g.getPath("Mumbai","Newyork"))
    print((g.get_shortest_path("Mumbai", "Dubai")))
