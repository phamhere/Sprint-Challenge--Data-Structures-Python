class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        current_node = self

        # creating helper function since I want to recurse using a node as a parameter
        def helper(node, cb):
            cb(node.value)
            # if node left or right exist, recurse with that left or right node
            if node.left:
                helper(node.left, cb)
            if node.right:
                helper(node.right, cb)

        helper(current_node, cb)

    def breadth_first_for_each(self, cb):
        # initializing variables
        node = self
        queue = []

        # pushing node to queue to start while loop
        queue.append(node)
        while len(queue) > 0:
            """changes node to start of queue and popping it off, resets with
            each loop to next node in line of queue"""
            node = queue.pop(0)
            cb(node.value)
            # adds onto queue if there is a left or right node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
