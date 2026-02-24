class queue:
    def __init__(self, data):
        self.data = []
        for x in list(data):
            self.data.append(x)

    def isEmpty(data):
        return not bool(data)

    def enqueue(data, entry):
        data.append(entry)

    def dequeue(self, data):
        if not self.isEmpty(data):
            data.pop(0)
        else:
            pass