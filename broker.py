import queue

class Broker:
    def __init__(self):
        self.message_queue = queue.Queue()

    def publish(self, message):
        self.message_queue.put(message)
        print(f"Message published: {message}")

    def consume(self):
        if not self.message_queue.empty():
            message = self.message_queue.get()
            print(f"Message consumed: {message}")
            return message
        else:
            print("No messages to consume.")
            return None

# Example usage (for testing)
if __name__ == "__main__":
    broker = Broker()
    broker.publish("Hello, World!")
    broker.consume()
