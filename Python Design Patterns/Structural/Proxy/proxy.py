import time

from producer import Producer


class Proxy:
    """"Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist checking if Producer is available ...")

        if self.occupied == 'No':
            # If the producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()

        # Make the producer meet the guest!
        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")
