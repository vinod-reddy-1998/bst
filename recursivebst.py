class Node:
    __slots__="element","left","right"

    def __init__(self,element,left=None,right=None):
        self.element=element
        self.left=left
        self.right=right

class Recbst:
    def __init__(self):
        self.root=None
    
    def rinsert(self,troot,e):
        if troot:
            if e<troot.element:
                troot.left=self.rinsert(troot.left,e)
            elif e>troot.element:
                troot.right=self.rinsert(troot.right,e)
        else:
            n=Node(e)
            troot=n
        return troot
    
    def rsearch(self,troot,key):
        if troot:
            if key==troot.element:
                return True
            elif key<troot.element:
                return self.rsearch(troot.left,key)
            else:
                return self.rsearch(troot.right,key)
        else:
            return False

        

    def inorder(self,troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element,end=' ')
            self.inorder(troot.right)



B = Recbst()
B.root=B.rinsert(B.root,50)
B.rinsert(B.root,30)
B.rinsert(B.root,80)
B.rinsert(B.root,60)
B.rinsert(B.root,40)
B.rinsert(B.root,60)
B.rinsert(B.root,90)
B.inorder(B.root)
print()
print(B.rsearch(B.root,60))
