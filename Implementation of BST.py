class TreeNode: 

    def __init__(self, data, left=None, right=None):
        # initialization of the data, and left and right child for each node
        self.data = data 
        self.left = left
        self.right = right 
    

class Tree: 

    # creates root as object of Tree Node Class
    def __init__(self, rootValue = None):
        self.root = TreeNode(rootValue) 
    
    #inserts Node at correct location by traversing through tree
    def insertNode(self, cur, newData): 
        # Both children are empty, thus child is chosen by airthmetic
        if cur.left == None and cur.right == None:
            if newData < cur.data: 
                cur.left = TreeNode(newData)
            else:
                cur.right = TreeNode(newData)
        # Paramaters met to add to left child
        elif cur.left == None and newData < cur.data: 
            cur.left = TreeNode(newData)
        # Parameters met to add to right child
        elif cur.right == None and newData > cur.data: 
            cur.right = TreeNode(newData)
        # traverses left through recursion
        elif newData < cur.data: 
            self.insertNode(cur.left, newData)
        # traverses right through recursion
        elif newData > cur.data: 
            self.insertNode(cur.right, newData)


    def addNode(self, newData):
        # if three is no current root then the added data becomes new root  
        if self.root.data == None: 
            self.root = TreeNode(newData)
        # regularly inserts node
        else: 
            self.insertNode(self.root, newData)

    # recursively iterates by checking left, then visting, then checking right
    def inOrder(self, pos): 
        if pos.left != None:
            self.inOrder(pos.left)

        print(pos.data)

        if pos.right != None:
            self.inOrder(pos.right)

    # recursively iterates by visiting, then checking left, then checking right
    def preOrder(self, pos): 

        print(pos.data)

        if pos.left != None:
            self.preOrder(pos.left)

        if pos.right != None:
            self.preOrder(pos.right)

     # recursively iterates tree by checking left, then checking right, then visiting
    def postOrder(self, pos): 

        if pos.left != None:
            self.postOrder(pos.left)

        if pos.right != None:
            self.postOrder(pos.right)

        print(pos.data)
 

def main():
    tree = Tree(8)
    tree.addNode(5)
    tree.addNode(10)
    tree.addNode(9)
    tree.addNode(11)
    tree.addNode(3)
    tree.addNode(1)
    tree.addNode(2)
    print('In Order:')
    tree.inOrder(tree.root)




main()

    


        


        


            
    
