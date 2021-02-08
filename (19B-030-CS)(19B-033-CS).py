
"""Project"""

"""  Randomized Meldable Priority Queues """


"""
GitHub Reppo Link    
                    
"""

class MaxHeap:

    # Initialize the Maximum Heap Priority Queue
    def __init__(self, collection=None):
        self.Heap = []

        if collection != None:    # Checks whether the collection is given or not if yes then it will automatically enqueue the elements
            for i in collection:  # Loop to iterate the collections in the list and enqueue one by one in the heap
                self.En_queue(i)

    # Length function is used to find the total number of length or available elements in the queue
    def __len__(self):
        return len(self.Heap)

    # Enqueue function is used to Enqueue The values one by one when the function calls
    def En_queue(self, value):
        self.Heap.append(value)   # append the values in the self.heap list
        self.Move_Up(len(self) - 1)

    # Dequeue function is used to Dequeue the values and move or set the elements one by one  
    def De_queue(self):
        self.Swap_elemnt(len(self) - 1, 0)
        el = self.Heap.pop()
        self.Move_Down(0)
        return el

    # This function is used to print the queues one by one
    def Print_Queue(self, index=1):
        print(f"{self.Heap[index - 1]}")

        left_child = 2 * index
        right_child = 2 * index + 1

        if left_child <= len(self):
            self.Print_Queue(left_child)

        if right_child <= len(self):
            self.Print_Queue(right_child)

    # This function is used to print the Heap function as a binary search tree one by one 
    def Print_BST(self, index=1, indent=0):
        print("\t" * indent, f"{self.Heap[index - 1]}")

        left_child = 2 * index
        right_child = 2 * index + 1


        if left_child <= len(self):
            self.Print_BST(left_child, indent=indent + 1)
        if right_child <= len(self):
            self.Print_BST(right_child, indent=indent + 1)

    # This function is used to Swap the elements and consider the larger one by one 
    def Swap_elemnt(self,i, j):
        self.Heap[i], self.Heap[j] = self.Heap[j], self.Heap[i]


    def Move_Up(self, index):
        parent_index = (index - 1) // 2
        # If we've hit the root node, there's nothing left to do
        if parent_index < 0:
            return

        # If the current node is larger than the parent node, swap them
        if self.Heap[index] > self.Heap[parent_index]:
            self.Swap_elemnt(index, parent_index)
        self.Move_Up(parent_index)


    def Move_Down(self, index):
        child_index = 2 * index + 1
        # If we've hit the end of the heap, there's nothing left to do
        if child_index >= len(self.Heap):
            return

        # If the node has a both children, swap with the larger one
        if child_index + 1 < len(self.Heap) and self.Heap[child_index] < self.Heap[child_index + 1]:
            child_index += 1

        # If the child node is smaller than the current node, swap them
        if self.Heap[child_index] > self.Heap[index]:
            self.Swap_elemnt(child_index, index)
            self.Move_Down(child_index)
    
    # For finding the maximum numbers in the maxheap 
    def Find_Max(self):
        return self.Heap[0]

    # For Deleting the maximum numbers in the maxheap 
    def Delete_Max(self):
        return self.De_queue()

    # To delete the value from the self.heap 
    def Delete_By(self,value):
        for i in self.Heap:

            if i == value:
                self.Heap.remove(i)

        MaxHeap(self.Heap)

# Making an instance by calling the class MaxHeap
max_heap  = MaxHeap([1,12,23,2,3,4,5,5,6,7,8,9])

max_heap.En_queue(18)
max_heap.De_queue()

# Deleting the item 12 
max_heap.Delete_By(12)

max_heap.Print_Queue()

max_heap.Print_BST()


# ________________________________________________________________________________________
# The End
# ________________________________________________________________________________________
