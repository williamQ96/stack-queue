"""
Program: Project 1-Stacks and Queues
Author: William Qiu
Date: 02/02/2023
Description: This is an implementation of Node, Queue, and Stack in Python.
Notes: For CS 313, Winter 2023, University of Oregon.
"""

# ------------------------------ Exceptions -------------------------------------
class QueueCapacityTypeError(Exception):
    pass

class QueueCapacityBoundError(Exception):
    pass

class QueueIsFull(Exception):
    pass

class QueueIsEmpty(Exception):
    pass

class StackCapacityTypeError(Exception):
    pass

class StackCapacityBoundError(Exception):
    pass

class StackIsFull(Exception):
    pass

class StackIsEmpty(Exception):
    pass

# ---------------------------------- Classes -----------------------------------
class Node:
    """
    Description: This is a basic Node class. It stores any valid data and has points to the next node when applicable.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """
    Description: This is a Queue class. It creates a FIFO linked list.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        if type(capacity) != int:
            raise QueueCapacityTypeError("Error: QueueCapacityTypeError. The Queue capacity is of the wrong type")
        if capacity <= 0:
            raise QueueCapacityBoundError("Error: QueueCapacityBoundError. The capacity is negative or 0 ")
        self.head = None
        self.tail = None
        self.currentSize = 0

    def enqueue(self, item) -> bool:
        if self.isFull():
            raise QueueIsFull("Queue is full.")
        if self.isEmpty():
            temp = Node(item)
            self.head = temp
            self.tail = temp
            self.currentSize += 1
            return True
        temp = Node(item)
        self.tail.next = temp
        self.tail = temp
        self.currentSize += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            raise QueueIsEmpty("Queue is empty.")
        temp = self.head
        val = temp.data
        self.currentSize -= 1
        self.head = self.head.next
        temp.next = None
        return val

    def front(self):
        if self.isEmpty():
            raise QueueIsEmpty("Queue is empty.")
        return self.head.data

    def isEmpty(self) -> bool:
        return self.currentSize == 0

    def isFull(self) -> bool:
        return self.currentSize >= self.capacity

class Stack:
    """
    Description: This is a Stack class. It creates a LIFO linked list.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        if type(capacity) != int:
            raise StackCapacityTypeError("Error: StackCapacityTypeError. The Stack capacity is of the wrong type")
        if capacity <= 0:
            raise StackCapacityBoundError("Error: QueueCapacityBoundError. The capacity is negative or 0 ")
        self.head = None
        self.currentSize = 0

    def push(self, item) -> bool:
        if self.isFull():
            raise StackIsFull("The current stack is full.")
        if self.isEmpty():
            self.head = Node(item)
            self.currentSize += 1
            return True
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self.currentSize += 1
        return True

    def pop(self):
        if self.isEmpty():
            raise StackIsEmpty("Stack is Empty")
        temp = self.head
        val = temp.data
        self.currentSize -= 1
        self.head = self.head.next
        temp.next = None
        return val

    def peek(self):
        if self.isEmpty():
            raise StackIsEmpty("Stack is Empty")
        return self.head.data

    def isEmpty(self) -> bool:
        return self.currentSize == 0

    def isFull(self) -> bool:
        return self.currentSize >= self.capacity

