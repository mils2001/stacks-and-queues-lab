
import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if self.is_empty():
            return None

        return self.items.pop(0)

    def peek(self):
        """Return the first item without removing it."""
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly select a winner.
        Dequeue all customers up to and including the winner.
        Return the winning customer's name.
        """
        if self.is_empty():
            return None

        winner = random.choice(self.items)

        while not self.is_empty():
            customer = self.dequeue()

            if customer == winner:
                break

        print(f"Raffle winner: {winner}")
        print(f"Remaining customers: {self.items}")

        return winner
