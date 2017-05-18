class Node(object):
  """Binary search tree node."""

  def __init__(self, data, left=None, right=None):
    """Create node, with data and optional left/right."""

    self.left = left
    self.right = right
    self.data = data

  def is_valid(self):
    
    def _ok(n, lt, gt):
    
      if not n:
        return True

      if lt and n.data > lt:
        return False
        
      if gt and n.data < gt:
        return False
        
      if not _ok(n.left, n.data, gt):
        return False
        
      if not _ok(n.right, lt, n.data):
        return False
        
      return True
  
    return _ok(self, None, None)
  


t = Node(4,
  Node(2, Node(1), Node(3)),
  Node(6, Node(5), Node(7)))

print t.is_valid()
# True

t = Node(4,
  Node(2, Node(3), Node(3)),
  Node(6, Node(5), Node(7)))

print t.is_valid()
# False

t = Node(4,
  Node(2, Node(1), Node(3)),
  Node(6, Node(1), Node(7)))

print t.is_valid()
# False