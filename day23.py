'''
Sample Input

7
3
5
2
1
4
6
7

Sample Output

3

        3

    2       5

1       4       6

                    7
'''


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

    def getHeight(self,root):
        if not root:
            return -1
        left_tree = self.getHeight(root.left)
        right_tree = self.getHeight(root.right)
        height = 1 + max([left_tree, right_tree])
        return height

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       