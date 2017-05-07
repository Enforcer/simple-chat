class Room:

    def __init__(self):
        self.clients = []

    def join(self, client):
        self.clients.append(client)

    def leave(self, client):
        try:
            self.clients.remove(client)
        except ValueError:
            pass  # already removed

    async def send_message(self, message, sender):
        for receiver in self.clients:
            try:
                await receiver.send(message)
            except ConnectionClosed:
                self.leave(receiver)

    def __len__(self):
        return len(self.clients)
