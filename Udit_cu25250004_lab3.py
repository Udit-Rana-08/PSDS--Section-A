#Q. Implement stack and queue operations Linked lists; demonstrate push, pop,
#enqueue,and dequeue operations.

# Stack using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return

        data = self.top.data
        self.top = self.top.next
        print(data, "popped from stack")

    # Display stack
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top
        print("Stack:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Demonstration
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()
stack.display()


# Queue using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "enqueued into queue")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(data, "dequeued from queue")

    # Display queue
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        print("Queue:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Demonstration
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()

queue.dequeue()
queue.display()
