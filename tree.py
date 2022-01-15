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

    def print_tree(self,field):
        self.field=field
        spaces="\t"*self.get_level()
        prefix=spaces+"|---" if self.parent else ""
        if field=="Both":
            print(prefix+self.name+' '+self.designation)
        elif field=="name":
            print(prefix+self.name)
        elif field=="designation":
            print(prefix+self.designation)
        if self.children:
            for child in self.children:
                child.print_tree(field)

def build_product_tree():
    root=treenode("Nilupul","(CEO)")
    CTO=treenode("Chinmay","(CTO)")
    root.add_childern(CTO)
    CTO.add_childern(treenode("Vishwa","(Infrastructure Head)"))
    CTO.add_childern(treenode("Aamir","(Application Head)"))
    Hr=treenode("gels","(Hr)")
    root.add_childern(Hr)
    rm=treenode("Peter","(Recruitment Manager)")
    Hr.add_childern(rm)
    Hr.add_childern(treenode("Waqas","(Policy Manager)"))
    rm.add_childern(treenode("Waqas","(Intern)"))
    
    return root

if __name__=='__main__':
    root=build_product_tree()
    root.print_tree("name")
    pass