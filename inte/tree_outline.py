# Print the outline (boundary) of a complete binary tree 
# (every level, except possibly the last, is completely filled, 
# and all nodes are as far left as possible). 
# Start at the root and go anti-clockwise; do not print any node twice.
# Example:
# 
#            A
#          /   \
#         B     C
#       /  \   / \
#      D    E  F  G
#     / \  /
#    H  J  K
# 
# Expected output: ABDHJKFGC
"""
 root to left leaf node --
 all leaf nodes -- 
 rigt leaf node to root --

"""
def printLeftOutline(node):
  if(node):
    if(node.left):
      print(node.data)
      printLeftOutline(node.left)
    elif(node.right):
      print(node.data)
      printLeftOutline(node.right)

def printRightOutline(node):
  if(node):
    if(node.right):
      printRightOutline(node.right)
      print(node.data)
    elif(node.left):
      printRightOutline(node.left)
      print(node.data)

def printLeafNode(node):
  if(node):
    printLeafNode(node.left)
    if node.left is None and node.right is None:
      print(node.data)
    printLeafNode(node.right)

def printOutline(node):
  if(node):
    print(node.data)
    printLeftOutline(node.left)
    printLeafNode(node.left)
    printLeafNode(node.right)
    printRightOutline(node.right)


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


#            A
#          /   \
#         B     C
#       /  \   / \
#      D    E  F  G
#     / \  /
#    H  J  K


rootNode = Node('A')
rootNode.left = Node('B')
rootNode.left.left = Node("D")
rootNode.left.right = Node('E')
rootNode.left.right.left = Node('K')
rootNode.left.left.left = Node("H")
rootNode.left.left.right = Node("J")
rootNode.right = Node('C')
rootNode.right.left = Node('F')
rootNode.right.right = Node('G')


printOutline(rootNode)