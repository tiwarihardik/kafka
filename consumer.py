from broker import Broker

class Consumer:
    def __init__(self, broker):
        self.broker = broker

    def read_message(self):
        message = self.broker.consume()
        if message:
            # Process the message if needed
            print(f"Processed message: {message}")

# Example usage
if __name__ == "__main__":
        broker = Broker()
        consumer = Consumer(broker)
        consumer.read_message()  # Since no messages are published, it will show "No messages to consume."
