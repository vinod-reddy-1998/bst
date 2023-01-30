class Node:
    __slots__ = 'element', 'left', 'right'

    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,troot,e):
        temp = None
        while troot:
            temp = troot
            if e == troot.element:
                return
            elif e < troot.element:
                troot = troot.left
            elif e > troot.element:
                troot = troot.right
        n = Node(e)
        if self.root:
            if e < temp.element:
                temp.left = n
            else:
                temp.right = n
        else:
            self.root = n


    def search(self,key):
        troot=self.root
        while troot:
            if key==troot.element:
                return True
            elif key<troot.element:
                troot=troot.left
            elif key>troot.element:
                troot=troot.right
        
        return False 

    def delete(self,key):
        p=self.root
        pp=None
        while p and p.element!=None:
            pp=p
            if key<p.element:
                p=p.left
            elif key>p.element:
                p=p.right

        if not p:
            return False

        if p.left and p.right:
            s = p.left
            ps = p
            while s.right:
                ps = s
                s = s.right
            p.element = s.element
            p = s
            pp = ps
        c = None
        if p._left:
            c = p.left
        else:
            c = p.right
        if p == self.root:
            self.root = c
        else:
            if p == pp.left:
                pp.left = c
            else:
                pp.right = c

    def inorder(self,troot):
        # print("vinod")
        if troot:
            self.inorder(troot.left)
            print(troot.element,end=' ')
            self.inorder(troot.right)

B = BinarySearchTree()
B.insert(B.root,50)
B.insert(B.root,30)
B.insert(B.root,80)
B.insert(B.root,70)
B.insert(B.root,40)
B.insert(B.root,60)
B.insert(B.root,90)
B.inorder(B.root)
print()
print(B.search(80))
# B.delete(70)
B.inorder(B.root)