from dataclasses import dataclass


@dataclass
class Message:
    event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")


messages = PriorityQueue()
messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)

print("messages.enqueue_with_priority(CRITICAL, Message(ABS engaged)")
messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))

