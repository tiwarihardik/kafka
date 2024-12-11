from broker import Broker

class Producer:
    def __init__(self, broker):
        self.broker = broker

    def send_message(self, message):
        self.broker.publish(message)

# Example usage
if __name__ == "__main__":
    while True:
        broker = Broker()
        producer = Producer(broker)
        producer.send_message("First Message")
        producer.send_message("Second Message")
