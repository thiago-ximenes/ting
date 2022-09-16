class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def search(self, index):
        if 0 <= index <= (len(self.data) - 1):
            return self.data[index]
        else:
            raise IndexError
