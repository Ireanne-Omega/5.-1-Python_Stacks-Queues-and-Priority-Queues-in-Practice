from queues import Queue

print("\nRESULT OF TESTING")
fifo = Queue("1st", "2nd", "3rd")
print(len(fifo))
print("\n")

for element in fifo:
    print(element)

print("\n")
print(len(fifo))
