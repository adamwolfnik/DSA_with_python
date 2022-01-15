class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return True
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinaryTreeNode(data)
        else:
            if self.right:
               self.right.add_child(data)
            else:
                 self.right=BinaryTreeNode(data)
    
    def in_order_traverse(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traverse()

        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_traverse()
        
        return elements

    def pre_order_traverse(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order_traverse()

        if self.right:
            elements+=self.right.pre_order_traverse()
        return elements
    
    def post_order_traverse(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traverse()
        
        if self.right:
            elements+=self.right.post_order_traverse()
        
        elements.append(self.data)
        return elements

    def search(self,value):
        if self.data==value:
            return True

        if value<self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        if value>self.data:
            if self.right:
               return self.right.search(value)
            else:
                return False
    
    def find_min(self):
        if self.left:
           return  self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
           return  self.right.find_max()
        else:
            return self.data

    def delete(self,node):
        if node<self.data:
            if self.left:
                self.left.delete(node)
        elif node>self.data:
            if self.right:
                self.right.delete(node)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)
        
        return self

def build_tree(elements):
    root=BinaryTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=="__main__":
    numbers=[17,4,1,20,9,23,18,34]
    number_tree=build_tree(numbers)
    number_tree.delete(18)
    print(number_tree.in_order_traverse())
    print(number_tree.pre_order_traverse())
    print(number_tree.post_order_traverse())
    print(number_tree.search(17))
    min=number_tree.find_min()
    max=number_tree.find_max()
    print(min)
    print(max)

