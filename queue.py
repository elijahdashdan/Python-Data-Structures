from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()


    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    

foodOrder = Queue()

def placeOrder(orders):
    for order in orders:
        foodOrder.enqueue(order)
        time.sleep(2)

def serveOrder():
    time.sleep(1)
    while True:
        order = foodOrder.dequeue()
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=placeOrder, args=(orders,))
    t2 = threading.Thread(target=serveOrder)

    t1.start()
    t2.start()