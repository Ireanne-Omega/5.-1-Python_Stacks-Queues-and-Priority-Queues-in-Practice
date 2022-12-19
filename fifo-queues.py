from queues import Queue

fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

# dequeue statement
print("\nRESULT OF TESTING")
print("\nfifo.dequeque()")
print(fifo.dequeue())
print("fifo.dequeque()")
print(fifo.dequeue())
print("fifo.dequeque()")
print(fifo.dequeue())


