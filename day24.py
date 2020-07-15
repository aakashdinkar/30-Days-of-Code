'''
Sample Input

6
3
5
4
7
2
1

Sample Output

3 2 5 1 4 7 
'''


import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    bst_list = ""
    def printLevel(self, root, level):
        if root == None:
            return
        if level == 1:
            self.bst_list += str(root.data) + " "
        elif level > 1:
            self.printLevel(root.left, level-1)
            self.printLevel(root.right, level-1)
    
    def height(self,root):
        if root == None:
            return 0
        left_tree_height = self.height(root.left)
        right_tree_height = self.height(root.right)
        if left_tree_height > right_tree_height:
            return left_tree_height + 1
        return right_tree_height + 1

    def levelOrder(self,root):
        #Write your code here
        h = self.height(root)
        for i in range(1, h+1):
            self.printLevel(root, i)
        print(self.bst_list)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)