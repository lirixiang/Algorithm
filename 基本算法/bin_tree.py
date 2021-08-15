class  Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            if cur_node is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preoder(self,node):
        if node is Node:
            return
        print(node.elem)
        self.preoder(node.lchild)
        self.preoder(node.rchild)

    def inoder(self,node):
        if node is Node:
            return
        self.inoder(node.lchild)
        print(node.elem)
        self.inoder(node.rchild)

    def postoder(self,node):
        if node is Node:
            return
        self.postoder(node.lchild)
        self.postoder(node.rchild)
        print(node.elem)












