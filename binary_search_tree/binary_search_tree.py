import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value

        current_node = self

        def insert_node(node, value):
                
            if value > node.value:
                if node.right is None:
                    node.right = BinarySearchTree(value)
                else:
                    insert_node(node.right, value)

            elif value < node.value:
                if node.left is None:
                    node.left = BinarySearchTree(value)
                else:
                    insert_node(node.left, value)
                
            else:
                print('Failed to Insert')
        
        insert_node(current_node, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None: 
            return False

        current_node = self

        while current_node is not None:
            if current_node.value == target:
                return True
            elif current_node.value > target:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return False
                

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return
        else:
            current_node = self
            max_val = current_node.value
            while current_node is not None:
                if current_node.value > max_val:
                    max_val = current_node.value
                
                current_node = current_node.right
            
            return max_val

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value is None:
            return
        
        def for_each_node(node):
            if node.value is not None:
                cb(node.value)
            
            if node.left is not None:
                for_each_node(node.left)
            
            if node.right is not None:
                for_each_node(node.right)

        for_each_node(self)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.value is None:
            return None
        
        def print_values(node):
            if node:
                print_values(node.left)
                print(node.value)
                print_values(node.right)
        
        print_values(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)

        while q.len() > 0:
            next_node = q.dequeue()
            print(next_node.value)

            if next_node.left is not None:
                q.enqueue(next_node.left)
            if next_node.right is not None:
                q.enqueue(next_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)

        while s.len() > 0:
            current_node = s.pop()
            print(current_node.value)

            if current_node.left is not None:
                s.push(current_node.left)
            if current_node.right is not None:
                s.push(current_node.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
