class treenode:

    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None

    def add_childern(self,child):
        child.parent=self
        self.children.append(child)
    
    def get_level(self):
        l=0
        p=self.parent
        while p:
            l+=1
            p=p.parent
        return l

    def print_tree(self,level):
        self.level=level
        spaces=" "*self.get_level()*3
        prefix=spaces+"|---" if self.parent else ""
        print(prefix+self.name)
        if self.children:
            for child in self.children:
                if child.get_level()<=level:
                    child.print_tree(level)

def build_product_tree():
    root=treenode("Nilupul","(CEO)")
    CTO=treenode("Chinmay","(CTO)")
    root.add_childern(CTO)
    IH=treenode("Vishwa","(Infrastructure Head)")
    CTO.add_childern(IH)
    IH.add_childern(treenode("Dhaval", "(Cloud Manager)"))
    CTO.add_childern(treenode("Aamir","(Application Head)"))
    Hr=treenode("gels","(Hr)")
    root.add_childern(Hr)
    Hr.add_childern(treenode("Peter","(Recruitment Manager)"))
    Hr.add_childern(treenode("Waqas","(Policy Manager)"))
    a=IH.get_level()
    print(a)
    return root

if __name__=='__main__':
    root=build_product_tree()
    root.print_tree(3)
    
    pass